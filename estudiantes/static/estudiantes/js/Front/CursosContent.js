function abrirContent(url, elemento){
    const enlaceContent = elemento.querySelector('h5').innerText;
    const idCurso = elemento.querySelector('h6').innerText;

    const powerpointContent = encodeURIComponent(enlaceContent);

    /* Guardo la url del powerpoint y el idCurso para regresar a infoCurso */
    window.location.href = `${url}?urlPower=${powerpointContent}&idCurso=${idCurso}`;
}