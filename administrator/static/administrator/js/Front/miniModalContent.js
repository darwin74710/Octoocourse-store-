function cerrarModals(){
    const fondo = document.getElementById("fondoModals");
    const modal1 = document.getElementById("modal1");
    const modal2 = document.getElementById("modal2");
    const modal3 = document.getElementById("modal3");
    const modal4 = document.getElementById("modal4");

    fondo.style.display = "none";
    modal1.style.display = "none";
    modal2.style.display = "none";
    modal3.style.display = "none";
    modal4.style.display = "none";
}

function modalSubContenidos(elemento, nombreContent){
    const fondo = document.getElementById("fondoModals");
    const modal = document.getElementById("modal1");

    const idContInfo = elemento.querySelector("#idContInfo");
    const tituloSubContent = document.getElementById("tituloSubContent");
    const subListMore = document.getElementsByClassName("subContenidosList");
    const subList = subListMore[0];
    const subContents = elemento.getElementsByClassName("subContenidos");
    subList.innerHTML = "";

    const idContenidoEdit = document.getElementById("idContenidoEdit");
    idContenidoEdit.value = idContInfo.innerText;

    cerrarModals();

    fondo.style.display = "flex";
    modal.style.display = "flex";

    tituloSubContent.value = nombreContent;

    for (const elemento of subContents) {
        const ArraySubContents = elemento.innerText.split("|");
        
        // Crea un nuevo div
        const div = document.createElement("div");
        div.classList.add("marcoOpcion");

        // le meto un H3 al div
        const h3 = document.createElement("h3");
        h3.id = "nomSubContInfo";
        h3.innerText = ArraySubContents[1];
        div.appendChild(h3);

        // le meto varios P al div con la info del subContenido
        const p1 = document.createElement("p");
        p1.id = "idSubContInfo";
        p1.innerText = ArraySubContents[0];
        div.appendChild(p1);

        const p2 = document.createElement("p");
        p2.id = "urlSubContInfo";
        p2.innerText = ArraySubContents[2];
        div.appendChild(p2);

        // le meto una función al subContenido para editarlo
        div.onclick = function() {
            modificarSub(this);
        };

        subList.appendChild(div);
    }
}

function agregarContenido(){
    const fondo = document.getElementById("fondoModals");
    const modal = document.getElementById("modal2");

    cerrarModals();

    fondo.style.display = "flex";
    modal.style.display = "flex";
}

function crearSubContenido(){
    const fondo = document.getElementById("fondoModals");
    const modal = document.getElementById("modal3");
    
    const idContenidoCrearSub = document.getElementById("idContenidoCrearSub");
    const idContenidoEdit = document.getElementById("idContenidoEdit");

    idContenidoCrearSub.value = idContenidoEdit.value;

    cerrarModals();

    fondo.style.display = "flex";
    modal.style.display = "flex";
}

function modificarSub(elemento){
    const fondo = document.getElementById("fondoModals");
    const modal = document.getElementById("modal4");
    
    const nomSubContInfo = elemento.querySelector("#nomSubContInfo");
    const idSubContInfo = elemento.querySelector("#idSubContInfo");
    const urlSubContInfo = elemento.querySelector("#urlSubContInfo");

    const modifiSubContNomb = document.getElementById("modifiSubContNomb");
    const modifiSubContId = document.getElementById("modifiSubContId");
    const modifiSubContUrl = document.getElementById("modifiSubContUrl");

    modifiSubContNomb.value = nomSubContInfo.innerText;
    modifiSubContUrl.value = urlSubContInfo.innerText;
    modifiSubContId.value = idSubContInfo.innerText;

    cerrarModals();

    fondo.style.display = "flex";
    modal.style.display = "flex";
}