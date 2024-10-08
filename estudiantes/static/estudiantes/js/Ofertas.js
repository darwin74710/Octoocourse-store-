/* ESTO ES PARA EL MENU DE INFORMACIÓN */
function activarInfo() {
    /* Verifica si la resolución de la pantalla es igual o menor a 700px */
    const esMovil = window.matchMedia("(max-width: 700px)").matches;

    if(esMovil){
        /* Es mediante una variable global declarada en el codigo html */
        window.location.href = ofertasInfoUrl;
    }else{
        sliderInfo();
    }
}

function sliderInfo(){
    const slideOfertas = document.getElementById("infoOfertas");
    
    /*Para cambiar el tamaño de la información*/
    if (slideOfertas.style.width != "700px") {
        slideOfertas.style.width = "700px";
        slideOfertas.style.border = "1px solid gray";
    }
}

function cerrarInfo(){
    const slideOfertas = document.getElementById("infoOfertas");

    if (slideOfertas.style.width === "700px") {
        slideOfertas.style.width = "0";
        slideOfertas.style.border = "none";
    }
}