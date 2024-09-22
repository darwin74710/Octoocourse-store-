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
    var cursos = document.getElementsByClassName("cursos")[0];
    var empleo = document.getElementsByClassName("empleo")[0];
    var hojaVida = document.getElementsByClassName("hojaVida")[0];
    var config = document.getElementsByClassName("config")[0];
    var des_ofertas = document.getElementsByClassName("des_ofertas")[0];
    var des_cursos = document.getElementsByClassName("des_cursos")[0];

    estandar.style.display = "none";
    cursos.style.display = "none";
    empleo.style.display = "none";
    hojaVida.style.display = "none";
    config.style.display = "none";
    des_ofertas.style.display = "none";
    des_cursos.style.display = "none";

    if(nav === 'estandar'){
        estandar.style.display = "block";
    }else if(nav === 'cursos'){
        cursos.style.display = "block";
    }else if(nav === 'empleo'){
        empleo.style.display = "block";
    }else if(nav === 'hojaVida'){
        hojaVida.style.display = "block";
    }else if(nav === 'config'){
        config.style.display = "block";
    }else if(nav === 'des_ofertas'){
        des_ofertas.style.display = "block";
    }else if(nav === 'des_cursos'){
        des_cursos.style.display = "block";
    }
}