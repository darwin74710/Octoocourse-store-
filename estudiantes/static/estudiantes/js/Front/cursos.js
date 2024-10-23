/* ACTIVAR O DESACTIVAR LOS FILTROS */
function filtro_lenguaje(Lenguaje) {
    let checkButton;

    /* Mediante un string que recibimos comprobamos cual boton es*/
    if(Lenguaje === 'Html'){
        checkButton = document.getElementById('HtmlFilter');
    }
    
    /* Verificamos si el boton se encuentra activado o no mediante el font del Bootstrap*/
    if (checkButton) {
        if (checkButton.classList.contains('bi-check-square')) {
            checkButton.classList.remove('bi-check-square');
            checkButton.style.color = "var(--letra1)";
            checkButton.classList.add('bi-square');
        } else {
            checkButton.classList.remove('bi-square');
            checkButton.style.color = "#8021bb";
            checkButton.classList.add('bi-check-square');
        }
    }
}

/* LO MISMO DE ARRIBA PERO SE DIVIDE PARA OPTIMIZAR */
function filtro_dificultad(Dificultad) {
    let checkButton;

    if(Dificultad === 'Basico'){
        checkButton = document.getElementById('BasicoFilter');
    }else if(Dificultad === 'Medio'){
        checkButton = document.getElementById('MedioFilter');
    }else if(Dificultad === 'Avanzado'){
        checkButton = document.getElementById('AvanzadoFilter');
    }
    
    if (checkButton) {
        if (checkButton.classList.contains('bi-check-square')) {
            checkButton.classList.remove('bi-check-square');
            checkButton.style.color = "var(--letra1)";
            checkButton.classList.add('bi-square');
        } else {
            checkButton.classList.remove('bi-square');
            checkButton.style.color = "#8021bb";
            checkButton.classList.add('bi-check-square');
        }
    }
}

function filtro_tiempo(Tiempo) {
    let checkButton;

    if(Tiempo === '0-5Filter'){
        checkButton = document.getElementById('0-5Filter');
    }else if(Tiempo === '6-10Filter'){
        checkButton = document.getElementById('6-10Filter');
    }else if(Tiempo === '11-15Filter'){
        checkButton = document.getElementById('11-15Filter');
    }else if(Tiempo === '15+Filter'){
        checkButton = document.getElementById('15+Filter');
    }
    
    if (checkButton) {
        if (checkButton.classList.contains('bi-check-square')) {
            checkButton.classList.remove('bi-check-square');
            checkButton.style.color = "var(--letra1)";
            checkButton.classList.add('bi-square');
        } else {
            checkButton.classList.remove('bi-square');
            checkButton.style.color = "#8021bb";
            checkButton.classList.add('bi-check-square');
        }
    }
}

function filtro_Certificado(Certificado) {
    let checkButton;

    if(Certificado === 'ConCertificado'){
        checkButton = document.getElementById('ConCertificado');
    }else if(Certificado === 'SinCertificado'){
        checkButton = document.getElementById('SinCertificado');
    }
    
    if (checkButton) {
        if (checkButton.classList.contains('bi-check-square')) {
            checkButton.classList.remove('bi-check-square');
            checkButton.style.color = "var(--letra1)";
            checkButton.classList.add('bi-square');
        } else {
            checkButton.classList.remove('bi-square');
            checkButton.style.color = "#8021bb";
            checkButton.classList.add('bi-check-square');
        }
    }
}

function ContenidoCursos(elementoSuperior){
    const divInferior = elementoSuperior.parentElement.querySelector('#inferior');

    if (divInferior.style.height === "0px" || divInferior.style.height === "") {
        divInferior.style.height = divInferior.scrollHeight + "px";
    } else {
        divInferior.style.height = "0px";
    }
}