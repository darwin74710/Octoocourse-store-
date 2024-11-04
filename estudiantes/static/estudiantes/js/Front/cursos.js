/* ACTIVAR O DESACTIVAR LOS FILTROS */
function filtro_lenguaje(Lenguaje) {
    const filtrado = document.getElementById("filtrado");
    var dato;
    let checkButton;

    /* Mediante un string que recibimos comprobamos cual boton es*/
    if(Lenguaje === 'Html'){
        checkButton = document.getElementById('HtmlFilter');
        dato = "|HTML";
    }
    
    /* Verificamos si el boton se encuentra activado o no mediante el font del Bootstrap*/
    change_filtros(checkButton, dato, filtrado);
}

/* LO MISMO DE ARRIBA PERO SE DIVIDE PARA OPTIMIZAR */
function filtro_dificultad(Dificultad) {
    const filtrado = document.getElementById("filtrado");
    var dato;
    let checkButton;

    if(Dificultad === 'Basico'){
        checkButton = document.getElementById('BasicoFilter');
        dato = "|Básico";
    }else if(Dificultad === 'Medio'){
        checkButton = document.getElementById('MedioFilter');
        dato = "|Medio";
    }else if(Dificultad === 'Avanzado'){
        checkButton = document.getElementById('AvanzadoFilter');
        dato = "|Avanzado";
    }
    
    change_filtros(checkButton, dato, filtrado);
}

function filtro_tiempo(Tiempo) {
    const filtrado = document.getElementById("filtrado");
    var dato;
    let checkButton;

    if(Tiempo === '0-5Filter'){
        checkButton = document.getElementById('0-5Filter');
        dato = "|0-5 Horas";
    }else if(Tiempo === '6-10Filter'){
        checkButton = document.getElementById('6-10Filter');
        dato = "|6-10 Horas";
    }else if(Tiempo === '11-15Filter'){
        checkButton = document.getElementById('11-15Filter');
        dato = "|11-15 Horas";
    }else if(Tiempo === '15+Filter'){
        checkButton = document.getElementById('15+Filter');
        dato = "|15+ Horas";
    }
    
    change_filtros(checkButton, dato, filtrado);
}

function filtro_Certificado(Certificado) {
    const filtrado = document.getElementById("filtrado");
    var dato;
    let checkButton;

    if(Certificado === 'ConCertificado'){
        checkButton = document.getElementById('ConCertificado');
        dato = "|Con Certificado";
    }else if(Certificado === 'SinCertificado'){
        checkButton = document.getElementById('SinCertificado');
        dato = "|Sin Certificado";
    }
    
    change_filtros(checkButton, dato, filtrado);
}

function change_filtros(checkButton, dato, filtrado){
    if (checkButton) {
        if (checkButton.classList.contains('bi-check-square')) {
            checkButton.classList.remove('bi-check-square');
            checkButton.style.color = "var(--letra1)";
            checkButton.classList.add('bi-square');

            filtrado.innerHTML = filtrado.innerHTML.replace(dato, "");
        } else {
            checkButton.classList.remove('bi-square');
            checkButton.style.color = "#8021bb";
            checkButton.classList.add('bi-check-square');

            filtrado.innerHTML += dato;
        }
    }
}

function aplicarFiltros() {
    const filtrado = document.getElementById("filtrado").textContent;
    const filtros = filtrado.split("|").filter(f => f);

    const url = new URL(window.location.href);
    url.searchParams.set("filtros", JSON.stringify(filtros));
    window.location.href = url;
}

function ContenidoCursos(elementoSuperior){
    const divInferior = elementoSuperior.parentElement.querySelector('#inferior');

    if (divInferior.style.height === "0px" || divInferior.style.height === "") {
        divInferior.style.height = divInferior.scrollHeight + "px";
    } else {
        divInferior.style.height = "0px";
    }
}