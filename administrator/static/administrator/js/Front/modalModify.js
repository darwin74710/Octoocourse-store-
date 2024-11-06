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