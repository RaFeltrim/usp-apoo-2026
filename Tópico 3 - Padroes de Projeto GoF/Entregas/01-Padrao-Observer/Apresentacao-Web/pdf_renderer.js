const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');
const puppeteer = require('puppeteer-core');
const { PDFDocument } = require('pdf-lib');

/**
 * Converte um caminho local (inclusive com espacos e acentos) para URL file:// segura.
 * @param {string} filePath
 * @returns {string}
 */
function toFileUrl(filePath) {
    return pathToFileURL(path.resolve(filePath)).href;
}

/**
 * Resolve o executavel do Chrome/Chromium priorizando CHROME_PATH ou PUPPETEER_EXECUTABLE_PATH.
 * @param {NodeJS.ProcessEnv} [env]
 * @returns {string}
 */
function resolveChromeExecutable(env = process.env) {
    const configured = (env.CHROME_PATH || env.PUPPETEER_EXECUTABLE_PATH || '').trim();
    if (configured) {
        if (!fs.existsSync(configured)) {
            throw new Error(`Executavel do navegador configurado nao encontrado em CHROME_PATH/PUPPETEER_EXECUTABLE_PATH: ${configured}`);
        }
        return configured;
    }

    const candidates = [
        'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
        'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
        env.LOCALAPPDATA ? path.join(env.LOCALAPPDATA, 'Google', 'Chrome', 'Application', 'chrome.exe') : '',
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '/usr/bin/google-chrome',
        '/usr/bin/chromium',
        '/usr/bin/chromium-browser',
    ].filter(Boolean);

    const found = candidates.find((candidate) => fs.existsSync(candidate));
    if (!found) {
        throw new Error(
            'Nenhum executavel do Chrome/Chromium encontrado. Defina a variavel de ambiente CHROME_PATH.'
        );
    }
    return found;
}

/**
 * Valida que o arquivo HTML de entrada existe antes de iniciar o navegador.
 * @param {string} inputHtml
 */
function assertInputExists(inputHtml) {
    if (!inputHtml || !fs.existsSync(inputHtml)) {
        throw new Error(`Arquivo HTML de entrada nao encontrado: ${inputHtml}`);
    }
}

/**
 * Renderiza um unico arquivo HTML em PDF garantindo fechamento do navegador em finally.
 * @param {{ inputHtml: string, outputPdf: string, pdfOptions?: object, executablePath?: string }} options
 */
async function renderSinglePdf({ inputHtml, outputPdf, pdfOptions = {}, executablePath }) {
    assertInputExists(inputHtml);
    const resolvedExe = executablePath ? resolveChromeExecutable({ CHROME_PATH: executablePath }) : resolveChromeExecutable();

    let browser;
    try {
        browser = await puppeteer.launch({
            executablePath: resolvedExe,
            headless: true,
        });
        const page = await browser.newPage();
        await page.goto(toFileUrl(inputHtml), { waitUntil: 'networkidle0' });
        fs.mkdirSync(path.dirname(outputPdf), { recursive: true });
        await page.pdf({
            path: outputPdf,
            ...pdfOptions,
        });
    } finally {
        await browser?.close();
    }
}

/**
 * Renderiza multiplos HTMLs em uma unica sessao headless e concatena as paginas no PDF final.
 * @param {{ inputs: Array<{ inputHtml: string, pdfOptions?: object }>, outputPdf: string, executablePath?: string }} options
 */
async function renderAndMergePdfs({ inputs, outputPdf, executablePath }) {
    if (!Array.isArray(inputs) || inputs.length === 0) {
        throw new Error('A lista de inputs para renderAndMergePdfs nao pode ser vazia.');
    }
    for (const item of inputs) {
        assertInputExists(item.inputHtml);
    }

    const resolvedExe = executablePath ? resolveChromeExecutable({ CHROME_PATH: executablePath }) : resolveChromeExecutable();
    const buffers = [];

    let browser;
    try {
        browser = await puppeteer.launch({
            executablePath: resolvedExe,
            headless: true,
        });
        const page = await browser.newPage();
        for (const item of inputs) {
            await page.goto(toFileUrl(item.inputHtml), { waitUntil: 'networkidle0' });
            const pdfBuffer = await page.pdf(item.pdfOptions || {});
            buffers.push(pdfBuffer);
        }
    } finally {
        await browser?.close();
    }

    const mergedPdf = await PDFDocument.create();
    for (const buffer of buffers) {
        const doc = await PDFDocument.load(buffer);
        const pages = await mergedPdf.copyPages(doc, doc.getPageIndices());
        pages.forEach((p) => mergedPdf.addPage(p));
    }

    fs.mkdirSync(path.dirname(outputPdf), { recursive: true });
    const mergedBytes = await mergedPdf.save();
    fs.writeFileSync(outputPdf, mergedBytes);
}

module.exports = {
    toFileUrl,
    resolveChromeExecutable,
    renderSinglePdf,
    renderAndMergePdfs,
};
