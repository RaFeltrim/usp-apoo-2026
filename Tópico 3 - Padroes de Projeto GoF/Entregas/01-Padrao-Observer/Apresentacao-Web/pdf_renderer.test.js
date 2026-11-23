const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('path');

const {
    toFileUrl,
    resolveChromeExecutable,
    renderSinglePdf,
    renderAndMergePdfs,
} = require('./pdf_renderer');

test('toFileUrl realiza percent-encoding de caminhos com espacos e acentos', () => {
    const samplePath = path.join(__dirname, '..', '..', 'Tópico 3 - Exemplo', 'arquivo de teste.html');
    const url = toFileUrl(samplePath);
    assert.ok(url.startsWith('file:///'), `Esperado prefixo file:///, obtido: ${url}`);
    assert.ok(url.includes('T%C3%B3pico%203%20-%20Exemplo'), `Acento/espaco nao codificado em: ${url}`);
    assert.ok(url.endsWith('/arquivo%20de%20teste.html'));
});

test('resolveChromeExecutable aceita CHROME_PATH existente', () => {
    const resolved = resolveChromeExecutable({ CHROME_PATH: __filename });
    assert.equal(resolved, __filename);
});

test('resolveChromeExecutable rejeita CHROME_PATH inexistente com erro descritivo', () => {
    assert.throws(
        () => resolveChromeExecutable({ CHROME_PATH: path.join(__dirname, 'nao-existe-chrome.exe') }),
        /nao encontrado/i
    );
});

test('renderSinglePdf falha antes de abrir navegador quando HTML de entrada nao existe', async () => {
    const missingHtml = path.join(__dirname, 'inexistente.html');
    const outputPdf = path.join(__dirname, 'saida-nao-gerada.pdf');
    await assert.rejects(
        () => renderSinglePdf({ inputHtml: missingHtml, outputPdf }),
        /Arquivo HTML de entrada nao encontrado/i
    );
});

test('renderAndMergePdfs valida todos os inputs antes de iniciar o navegador', async () => {
    const missingHtml = path.join(__dirname, 'inexistente-merge.html');
    const outputPdf = path.join(__dirname, 'saida-merge-nao-gerada.pdf');
    await assert.rejects(
        () => renderAndMergePdfs({ inputs: [{ inputHtml: missingHtml }], outputPdf }),
        /Arquivo HTML de entrada nao encontrado/i
    );
});
