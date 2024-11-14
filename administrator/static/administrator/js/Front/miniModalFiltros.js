function cerrarModals(){
    const fondo = document.getElementById("fondoModals");
    const modal1 = document.getElementById("modal1");
    const modal2 = document.getElementById("modal2");

    fondo.style.display = "none";
    modal1.style.display = "none";
    modal2.style.display = "none";
}

function editarFiltro(elemento){
    const fondo = document.getElementById("fondoModals");
    const modal = document.getElementById("modal1");

    fondo.style.display = "flex";
    modal.style.display = "flex";

    const documentoInfo = elemento.querySelector("#documentoInfo");
    const nombreInfo = elemento.querySelector("#nombreInfo");

    const idFiltro = document.getElementById("idFiltro");
    const inputNombre = document.getElementById("inputNombre1");

    idFiltro.value = documentoInfo.innerText;
    inputNombre.value = nombreInfo.innerText;
}

function agregarFiltro(){
    const fondo = document.getElementById("fondoModals");
    const modal = document.getElementById("modal2");

    cerrarModals();

    fondo.style.display = "flex";
    modal.style.display = "flex";
}