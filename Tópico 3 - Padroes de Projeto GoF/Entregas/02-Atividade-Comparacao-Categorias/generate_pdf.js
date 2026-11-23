const path = require('path');
const { renderSinglePdf } = require('../01-Padrao-Observer/Apresentacao-Web/pdf_renderer');

(async () => {
    try {
        console.log('Generating Relatório Discussão Comportamentais PDF...');
        const outputPath = path.join(__dirname, 'Relatorio_Discussao_Comportamentais_Grupo.pdf');
        await renderSinglePdf({
            inputHtml: path.join(__dirname, 'relatorio-discussao.html'),
            outputPdf: outputPath,
            pdfOptions: {
                format: 'A4',
                printBackground: true,
                margin: { top: '15mm', right: '15mm', bottom: '15mm', left: '15mm' },
            },
        });
        console.log('SUCCESS: Relatorio_Discussao_Comportamentais_Grupo.pdf gerado com sucesso!');
    } catch (err) {
        console.error('Error generating PDF:', err);
        process.exitCode = 1;
    }
})();
