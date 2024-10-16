function cambiarHV(tipoHV){
    const adjuntar = document.getElementById("hvElect1");
    const plantilla = document.getElementById("hvElect2");
    const btnAdjuntar = document.getElementById("btnAdjuntar");
    const btnPlantilla = document.getElementById("btnPlantilla");

    adjuntar.classList.remove("bi-circle", "bi-circle-fill");
    plantilla.classList.remove("bi-circle", "bi-circle-fill");

    if(tipoHV === "adjuntar"){ 
        adjuntar.classList.add("bi-circle-fill");
        plantilla.classList.add("bi-circle");

        btnAdjuntar.style.display = "inline";
        btnPlantilla.style.display = "none";
    }else if(tipoHV === "plantilla"){
        plantilla.classList.add("bi-circle-fill");
        adjuntar.classList.add("bi-circle");

        btnAdjuntar.style.display = "none";
        btnPlantilla.style.display = "inline";
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

function modalConfig(tipo){
    const mFondo = document.getElementById("modalConfig");
    const mUsu = document.getElementById("modalUsu");
    const mContra = document.getElementById("modalContra");
    const mHV = document.getElementById("modalHV");
    const mNoDocument = document.getElementById("modalNoDocument");

    mFondo.style.display = "none";
    mUsu.style.display = "none";
    mContra.style.display = "none";
    mHV.style.display = "none";
    mNoDocument.style.display = "none";

    if (tipo === "usuDesactive"){
        mFondo.style.display = "none";
        mUsu.style.display = "none";
    }else if (tipo === "contraDesactive"){
        mFondo.style.display = "none";
        mContra.style.display = "none";
    }else if (tipo === "hvDesactive"){
        mFondo.style.display = "none";
        mHV.style.display = "none";
    }else if (tipo === "NoDocumentDesactive"){
        mFondo.style.display = "none";
        mNoDocument.style.display = "none";
    }
    
    
    
    else if (tipo === "usuActive"){
        mFondo.style.display = "flex";
        mUsu.style.display = "flex";
    }else if (tipo === "contraActive"){
        mFondo.style.display = "flex";
        mContra.style.display = "flex";
    }else if (tipo === "hvActive"){
        mFondo.style.display = "flex";
        mHV.style.display = "flex";
    }else if (tipo === "NoDocumentActive"){
        mFondo.style.display = "flex";
        mNoDocument.style.display = "flex";
    }
}

function descargarPDF(){
    /* Variable para definir el div que voy a descargar */
    var elemento = document.getElementById('hojaVida');

    /* Opciones de html2pdf */
    var opt = {
        filename: 'Hoja_Vida.pdf',
        html2canvas:  { scale: 2 },
    };

    /* Desde aquí se convierte el div y se guarda como pdf */
    html2pdf().from(elemento).set(opt).save();
}