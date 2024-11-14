function modalConfig(tipo){
    const mFondo = document.getElementById("modalConfig");
    const mHVM = document.getElementById("modalHVM");

    mFondo.style.display = "none";
    mHVM.style.display = "none";

    if (tipo === "hvMDesactive"){
        mFondo.style.display = "none";
        mHVM.style.display = "none";
    }
    
    if (tipo === "hvMActive"){
        mFondo.style.display = "flex";
        mHVM.style.display = "flex";
    }
}

function navSuperior(dato){
    document.getElementById("datosPersonales").style.display = "none";
    document.getElementById("aptitudes").style.display = "none";
    document.getElementById("idiomas").style.display = "none";
    document.getElementById("lenguajesProg").style.display = "none";
    document.getElementById("expLaboral").style.display = "none";
    document.getElementById("formAcademica").style.display = "none";
    
    document.getElementById(dato).style.display = "block";
}