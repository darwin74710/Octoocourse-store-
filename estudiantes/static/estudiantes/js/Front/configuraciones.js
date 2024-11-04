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
    const mContra = document.getElementById("modalContra");
    const mHV = document.getElementById("modalHV");
    const mHVM = document.getElementById("modalHVM");
    const old_contra_input = document.getElementById("old_contra");
    const nuv_contra1_input = document.getElementById("nuv_contra1");
    const nuv_contra2_input = document.getElementById("nuv_contra2");

    mFondo.style.display = "none";
    mContra.style.display = "none";
    mHV.style.display = "none";
    mHVM.style.display = "none";

    if (tipo === "contraDesactive"){
        mFondo.style.display = "none";
        mContra.style.display = "none";
    }else if (tipo === "hvDesactive"){
        mFondo.style.display = "none";
        mHV.style.display = "none";
    }else if (tipo === "hvMDesactive"){
        mFondo.style.display = "none";
        mHVM.style.display = "none";
    }
    
    
    
    if (tipo === "contraActive"){
        mFondo.style.display = "flex";
        mContra.style.display = "flex";

        old_contra_input.value = "";
        nuv_contra1_input.value = "";
        nuv_contra2_input.value = "";
    }else if (tipo === "hvActive"){
        mFondo.style.display = "flex";
        mHV.style.display = "flex";
    }else if (tipo === "hvMActive"){
        mFondo.style.display = "flex";
        mHVM.style.display = "flex";
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