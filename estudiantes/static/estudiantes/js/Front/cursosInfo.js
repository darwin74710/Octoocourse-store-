function descargarCertificado(){
    /* Variable para definir el div que voy a descargar */
    var elemento = document.getElementById('certificado');

    /* Opciones de html2pdf */
    var opt = {
        filename: 'certificado.pdf',
        html2canvas:  { scale: 2 },
    };

    /* Desde aquí se convierte el div y se guarda como pdf */
    html2pdf().from(elemento).set(opt).save();
}