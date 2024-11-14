/* ESTO ES PARA EL MENU DE INFORMACIÓN */
function activarInfo(elemento) {
    /* Verifica si la resolución de la pantalla es igual o menor a 1100px */
    const esMovil = window.matchMedia("(max-width: 1100px)").matches;

    if(esMovil){
        const idOferta = elemento.querySelector('h5').innerText;
        const idParametro = encodeURIComponent(idOferta);

        window.location.href = `${ofertasInfoUrl}?idOferta=${idParametro}`;
    }else{
        /* Le paso el id al input para aplicar al curso */
        const idOferta = elemento.querySelector('h5').innerText;
        const inputIdOferta = document.getElementById('inputIdOferta');
        inputIdOferta.value =  idOferta;

        extraerInfo(elemento);
        sliderInfo();
    }
}

function extraerInfo(elemento){
    const slideOfertas = document.getElementById("elementsOferta");

    const titulo = elemento.querySelector('h1').innerText;
    const descripcion = elemento.querySelector('p').innerText;
    const aplicados = elemento.querySelector('.bi-person').innerText;
    const conocimientos = elemento.querySelector('.bi-terminal').innerText;
    const salario = elemento.querySelector('.bi-cash').innerText;
    const contrato = elemento.querySelector('.bi-briefcase').innerText;

    if (elemento.querySelector('h6')) {
        opcionPrincipal = "Realizar Prueba"
    } else {
        opcionPrincipal = "Aplicar"
    }
    
    slideOfertas.querySelector('h1').innerText = titulo;
    slideOfertas.querySelector('p').innerText = descripcion;
    slideOfertas.querySelector('.bi-person').innerText = aplicados;
    slideOfertas.querySelector('.bi-terminal').innerText = conocimientos;
    slideOfertas.querySelector('.bi-cash').innerText = salario;
    slideOfertas.querySelector('.bi-briefcase').innerText = contrato;
    slideOfertas.querySelector('#opcionPrincipal').textContent = opcionPrincipal;
}

function sliderInfo(){
    const slideOfertas = document.getElementById("infoOfertas");

    /*Para cambiar el tamaño de la información*/
    if (slideOfertas.style.width != "700px") {
        slideOfertas.style.width = "700px";
        slideOfertas.style.padding = "5px";
        slideOfertas.style.border = "1px solid var(--borde1)";
        slideOfertas.style.overflow = "auto";
    }
}

function cerrarInfo(){
    const slideOfertas = document.getElementById("infoOfertas");

    if (slideOfertas.style.width === "700px") {
        slideOfertas.style.width = "0";
        slideOfertas.style.padding = "0";
        slideOfertas.style.border = "none";
        slideOfertas.style.overflow = "hidden";
    }
}

function filtro_salario(salario) {
    const filtrado = document.getElementById("filtrado");
    var dato;
    let checkButton;

    if(salario === '0_1'){
        checkButton = document.getElementById('0_1Filter');
        dato = "|0_1";
    }else if(salario === '1_2'){
        checkButton = document.getElementById('1_2Filter');
        dato = "|1_2";
    }else if(salario === '2_3'){
        checkButton = document.getElementById('2_3Filter');
        dato = "|2_3";
    }else if(salario === '3+'){
        checkButton = document.getElementById('3+Filter');
        dato = "|3+";
    }
    
    change_filtros(checkButton, dato, filtrado);
}

function filtro_contrato(contrato) {
    const filtrado = document.getElementById("filtrado");
    var dato;
    let checkButton;

    checkButton = document.getElementById(contrato + 'Filter');
    dato = "|" + contrato;

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