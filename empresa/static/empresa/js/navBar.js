function MenuPC() {
    var menu_pc = document.getElementsByClassName("menu-compu")[0];

    if (menu_pc.style.display == "none" || menu_pc.style.display != "block") {
        menu_pc.style.display = "block";
    } else {
        menu_pc.style.display = "none";
    }
}

function MenuMovil() {
    var menu_movil = document.getElementsByClassName("menu-movil")[0];

    if (menu_movil.style.display == "none" || menu_movil.style.display != "block") {
        menu_movil.style.display = "block";
    } else {
        menu_movil.style.display = "none";
    }
}

function MenuEstandar() {
    var estandar = document.getElementsByClassName("estandar")[0];
    var estudiantes = document.getElementsByClassName("listaEstud")[0];
    var empleo = document.getElementsByClassName("empleo")[0];
    var config = document.getElementsByClassName("config")[0];


    if (empleo.style.display != "none") {
        empleo.style.display = "none";
    }
    if (estudiantes.style.display != "none") {
        estudiantes.style.display = "none";
    }
    if (config.style.display != "none") {
        config.style.display = "none";
    }
    if (estandar.style.display == "none" || estandar.style.display != "block") {
        estandar.style.display = "block";
    }
}

function MenuCursos() {
    var estandar = document.getElementsByClassName("estandar")[0];
    var estudiantes = document.getElementsByClassName("listaEstud")[0];
    var empleo = document.getElementsByClassName("empleo")[0];
    var config = document.getElementsByClassName("config")[0];


    if (empleo.style.display != "none") {
        empleo.style.display = "none";
    }
    if (estandar.style.display != "none") {
        estandar.style.display = "none";
    }
    if (config.style.display != "none") {
        config.style.display = "none";
    }

    if (estudiantes.style.display == "none" || estudiantes.style.display != "block") {
        estudiantes.style.display = "block";
    }
}

function MenuEmpleo() {
    var estandar = document.getElementsByClassName("estandar")[0];
    var estudiantes = document.getElementsByClassName("listaEstud")[0];
    var empleo = document.getElementsByClassName("empleo")[0];
    var config = document.getElementsByClassName("config")[0];

    if (estandar.style.display != "none") {
        estandar.style.display = "none";
    }
    if (estudiantes.style.display != "none") {
        estudiantes.style.display = "none";
    }
    if (config.style.display != "none") {
        config.style.display = "none";
    }

    if (empleo.style.display == "none" || empleo.style.display != "block") {
        empleo.style.display = "block";
    }
}

function MenuConfig() {
    var estandar = document.getElementsByClassName("estandar")[0];
    var estudiantes = document.getElementsByClassName("listaEstud")[0];
    var empleo = document.getElementsByClassName("empleo")[0];
    var config = document.getElementsByClassName("config")[0];
    var perfil = document.getElementsByClassName("perfil")[0];


    if (estandar.style.display != "none") {
        estandar.style.display = "none";
    }
    if (estudiantes.style.display != "none") {
        estudiantes.style.display = "none";
    }
    if (empleo.style.display != "none") {
        empleo.style.display = "none";
    }
    
    if (config.style.display == "none" || config.style.display != "block") {
        config.style.display = "block";
    }
}


function Exit() {
    var menu_pc = document.getElementsByClassName("menu-compu")[0];
    var menu_movil = document.getElementsByClassName("menu-movil")[0];

    menu_pc.style.display = "none";
    menu_movil.style.display = "none";
}