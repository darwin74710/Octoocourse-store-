/* ESTO ES PARA EL MENU DE INFORMACIÓN */
function activarInfo(elemento) {
    /* Verifica si la resolución de la pantalla es igual o menor a 1100px */
    const esMovil = window.matchMedia("(max-width: 1100px)").matches;

    if(esMovil){
        const idOferta = elemento.querySelector('h5').innerText;
        const idParametro = encodeURIComponent(idOferta);

        window.location.href = `${ofertasInfoUrl}?idOferta=${idParametro}`;
    }else{
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

    slideOfertas.querySelector('h1').innerText = titulo;
    slideOfertas.querySelector('p').innerText = descripcion;
    slideOfertas.querySelector('.bi-person').innerText = aplicados;
    slideOfertas.querySelector('.bi-terminal').innerText = conocimientos;
    slideOfertas.querySelector('.bi-cash').innerText = salario;
    slideOfertas.querySelector('.bi-briefcase').innerText = contrato;
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
    let checkButton;

    if(salario === '5_1'){
        checkButton = document.getElementById('5_1Filter');
    }else if(salario === '1_2'){
        checkButton = document.getElementById('1_2Filter');
    }else if(salario === '2_3'){
        checkButton = document.getElementById('2_3Filter');
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

function filtro_contrato(contrato) {
    let checkButton;

    if(contrato === 'Fijo'){
        checkButton = document.getElementById('FijoFilter');
    }else if(contrato === 'Indefinido'){
        checkButton = document.getElementById('IndefinidoFilter');
    }else if(contrato === 'ObraLabor'){
        checkButton = document.getElementById('ObraLaborFilter');
    }else if(contrato === 'Aprendizaje'){
        checkButton = document.getElementById('AprendizajeFilter');
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

/* Activar Modal Pago */
function modal_Pag(activador){
    const modal = document.getElementById("modalPago");

    if(activador === "activado"){
        modalPago.style.display = "flex";
    }else if (activador === "desactivado"){
        modalPago.style.display = "none";
    }
}