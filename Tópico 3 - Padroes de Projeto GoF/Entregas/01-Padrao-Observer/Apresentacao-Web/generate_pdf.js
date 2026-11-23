const path = require('path');
const { renderAndMergePdfs } = require('./pdf_renderer');

(async () => {
    try {
        console.log('Generating and merging Observer PDFs...');
        const outputPath = path.join(__dirname, 'Rafael_Feltrim_Entrega_Observer.pdf');
        await renderAndMergePdfs({
            inputs: [
                {
                    inputHtml: path.join(__dirname, 'index.html'),
                    pdfOptions: {
                        format: 'A4',
                        landscape: true,
                        printBackground: true,
                        margin: { top: 0, right: 0, bottom: 0, left: 0 },
                    },
                },
                {
                    inputHtml: path.join(__dirname, 'documento-apoio.html'),
                    pdfOptions: {
                        format: 'A4',
                        printBackground: true,
                        margin: { top: '20px', right: '20px', bottom: '20px', left: '20px' },
                    },
                },
            ],
            outputPdf: outputPath,
        });
        console.log('SUCCESS: Rafael_Feltrim_Entrega_Observer.pdf');
    } catch (err) {
        console.error('Error generating PDF:', err);
        process.exitCode = 1;
    }
})();
