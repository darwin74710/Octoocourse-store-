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

function modalRespuestas(elemento, nombrePregunta){
    const fondo = document.getElementById("fondoModals");
    const modal = document.getElementById("modal1");

    const idPreguntaInfo = elemento.querySelector("#idPreguntaInfo");

    const tituloPregunta = document.getElementById("tituloPregunta");
    const repListMore = document.getElementsByClassName("respuestasList");
    const repList = repListMore[0];
    const repContents = elemento.getElementsByClassName("respuestas");
    repList.innerHTML = "";

    const idPreguntaEdit = document.getElementById("idPreguntaEdit");
    idPreguntaEdit.value = idPreguntaInfo.innerText;

    cerrarModals();

    fondo.style.display = "flex";
    modal.style.display = "flex";

    tituloPregunta.value = nombrePregunta;

    for (const elemento of repContents) {
        const ArrayRespuestas = elemento.innerText.split("|");
        
        // Crea un nuevo div
        const div = document.createElement("div");
        div.classList.add("marcoOpcion");

        // le meto un H3 al div
        const h3 = document.createElement("h3");
        h3.id = "respuestaInfoText";
        h3.innerText = ArrayRespuestas[1];
        div.appendChild(h3);

        // le meto varios P al div con la info del subContenido
        const p1 = document.createElement("p");
        p1.id = "idRespuestaInfo";
        p1.innerText = ArrayRespuestas[0];
        div.appendChild(p1);

        const p2 = document.createElement("p");
        p2.id = "validacionInfo";
        p2.innerText = ArrayRespuestas[2];
        div.appendChild(p2);

        // le meto una función al subContenido para editarlo
        div.onclick = function() {
            modificarResp(this);
        };

        repList.appendChild(div);
    }
}

function agregarPregunta(){
    const fondo = document.getElementById("fondoModals");
    const modal = document.getElementById("modal2");

    cerrarModals();

    fondo.style.display = "flex";
    modal.style.display = "flex";
}

function crearRespuesta(){
    const fondo = document.getElementById("fondoModals");
    const modal = document.getElementById("modal3");
    
    const idPreguntaCrearResp = document.getElementById("idPreguntaCrearResp");
    const idPreguntaEdit = document.getElementById("idPreguntaEdit");

    idPreguntaCrearResp.value = idPreguntaEdit.value;

    cerrarModals();

    fondo.style.display = "flex";
    modal.style.display = "flex";
}

function modificarResp(elemento){
    const fondo = document.getElementById("fondoModals");
    const modal = document.getElementById("modal4");
    
    const respuestaInfoText = elemento.querySelector("#respuestaInfoText");
    const idRespuestaInfo = elemento.querySelector("#idRespuestaInfo");
    const validacionInfo = elemento.querySelector("#validacionInfo");

    const modifiRespuestaText = document.getElementById("modifiRespuestaText");
    const modifiRespuestaId = document.getElementById("modifiRespuestaId");
    const modifiRespuestaValidacion = document.getElementById("modifiRespuestaValidacion");
    
    if (validacionInfo.innerText === "True"){
        validacion = 1;
    }else if(validacionInfo.innerText === "False"){
        validacion = 0;
    }

    modifiRespuestaText.innerText = respuestaInfoText.innerText;
    modifiRespuestaValidacion.value = validacion;
    modifiRespuestaId.value = idRespuestaInfo.innerText;

    cerrarModals();

    fondo.style.display = "flex";
    modal.style.display = "flex";
}