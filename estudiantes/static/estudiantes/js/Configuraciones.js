function cambiarHV(tipoHV){
    const adjuntar = document.getElementById("hvElect1");
    const plantilla = document.getElementById("hvElect2");
    const btnAdjuntar = document.getElementById("btnAdjuntar");

    adjuntar.classList.remove("bi-circle", "bi-circle-fill");
    plantilla.classList.remove("bi-circle", "bi-circle-fill");

    if(tipoHV === "adjuntar"){ 
        adjuntar.classList.add("bi-circle-fill");
        plantilla.classList.add("bi-circle");

        btnAdjuntar.style.display = "inline";
    }else if(tipoHV === "plantilla"){
        plantilla.classList.add("bi-circle-fill");
        adjuntar.classList.add("bi-circle");

        btnAdjuntar.style.display = "none";
    }
}

function cambiarTema(tipoTema){
    if(tipoTema === "claro"){ 
        numTema = 1;
        localStorage.setItem('numTema', numTema);
        aplicarEstilos();
        seleccionTema();
    }else if(tipoTema === "oscuro"){
        numTema = 2;
        localStorage.setItem('numTema', numTema);
        aplicarEstilos();
        seleccionTema();
    }
}

function seleccionTema(){
    const claro = document.getElementById("temaElect1");
    const oscuro = document.getElementById("temaElect2");

    claro.classList.remove("bi-circle", "bi-circle-fill");
    oscuro.classList.remove("bi-circle", "bi-circle-fill");

    if(numTema === 1){
        claro.classList.add("bi-circle-fill");
        oscuro.classList.add("bi-circle");
    }else if(numTema === 2){
        oscuro.classList.add("bi-circle-fill");
        claro.classList.add("bi-circle");
    }
}