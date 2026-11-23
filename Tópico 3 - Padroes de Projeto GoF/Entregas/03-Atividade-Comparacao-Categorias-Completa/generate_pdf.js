const path = require('path');
const { renderSinglePdf } = require('../01-Padrao-Observer/Apresentacao-Web/pdf_renderer');

(async () => {
    try {
        console.log('Generating GoF Part 2 PDF (Individual)...');
        const outputPath = path.join(__dirname, 'Rafael_Feltrim_Atividade3_Comparacao_Categorias_GoF.pdf');
        await renderSinglePdf({
            inputHtml: path.join(__dirname, 'relatorio-gof-completo.html'),
            outputPdf: outputPath,
            pdfOptions: {
                format: 'A4',
                printBackground: true,
                margin: { top: '12mm', right: '12mm', bottom: '12mm', left: '12mm' },
            },
        });
        console.log('SUCCESS: Rafael_Feltrim_Atividade3_Comparacao_Categorias_GoF.pdf gerado com sucesso!');
    } catch (err) {
        console.error('Error generating PDF:', err);
        process.exitCode = 1;
    }
})();
