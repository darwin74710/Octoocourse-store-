function MenuPC(){
    var menu_pc = document.getElementsByClassName("menu-compu")[0];
    var menu_movil = document.getElementsByClassName("menu-movil")[0];

    if(menu_movil.style.display != "none"){
        menu_movil.style.display = "none";
    }

    if(menu_pc.style.display == "none" || menu_pc.style.display != "block"){
        menu_pc.style.display = "block";
    }else{
        menu_pc.style.display = "none";
    }
}

function MenuMovil(){
    var menu_pc = document.getElementsByClassName("menu-compu")[0];
    var menu_movil = document.getElementsByClassName("menu-movil")[0];

    if(menu_pc.style.display != "none"){
        menu_pc.style.display = "none";
    }

    if(menu_movil.style.display == "none" || menu_movil.style.display != "block"){
        menu_movil.style.display = "block";
    }else{
        menu_movil.style.display = "none";
    }
}

function Navegacion(nav){
    var estandar = document.getElementsByClassName("estandar")[0];
    var listaEstud = document.getElementsByClassName("listaEstud")[0];
    var empleo = document.getElementsByClassName("empleo")[0];
    var config = document.getElementsByClassName("config")[0];
    var des_ofertas = document.getElementsByClassName("des_ofertas")[0];

    estandar.style.display = "none";
    listaEstud.style.display = "none";
    empleo.style.display = "none";
    config.style.display = "none";
    des_ofertas.style.display = "none";

    if(nav === 'estandar'){
        estandar.style.display = "block";
    }else if(nav === 'listaEstud'){
        listaEstud.style.display = "block";
    }else if(nav === 'empleo'){
        empleo.style.display = "block";
    }else if(nav === 'config'){
        config.style.display = "block";
    }else if(nav === 'des_ofertas'){
        des_ofertas.style.display = "block";
    }
}


function Exit() {
    var menu_pc = document.getElementsByClassName("menu-compu")[0];
    var menu_movil = document.getElementsByClassName("menu-movil")[0];

    menu_pc.style.display = "none";
    menu_movil.style.display = "none";
}


/*NavBar ali*/ 
function mostrarPublicarOferta() {
    ocultarTodasLasSecciones();
    document.querySelector('.publicar-oferta').style.display = 'block';
}

function mostrarOferta() {
    ocultarTodasLasSecciones();
    document.querySelector('.veroferta').style.display = 'block';
}

function ocultarTodasLasSecciones() {
    document.querySelector('.hola').style.display = 'none';
    document.querySelector('.publicar-oferta').style.display = 'none';
    document.querySelector('.veroferta').style.display = 'none';
}

window.onload = function () {
    document.querySelector('.hola').style.display = 'block';
};