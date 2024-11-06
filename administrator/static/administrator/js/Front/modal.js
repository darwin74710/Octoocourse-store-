function modalOpenExit(tipo, ventana, elemento){
    const Modal = document.getElementById("modalOpciones");
    const marco = document.getElementById("marcoModal");

    Modal.style.display = "none";
    marco.style.display = "none";

    if (tipo === "desactive"){
        Modal.style.display = "none";
        marco.style.display = "none";
    }
    
    if (tipo === "active"){
        Modal.style.display = "flex";
        marco.style.display = "flex";

        if(ventana === 'estudiantes'){
            estudiantes(elemento);
        }else if(ventana === 'empresas'){
            empresas(elemento);
        }else if(ventana === 'cursos'){
            cursos(elemento);
        }else if(ventana === 'ofertas'){
            ofertas(elemento);
        }
    }
}

function estudiantes(elemento){
    var nombreInfo = elemento.querySelector("#nombreInfo");
    var correoInfo = elemento.querySelector("#correoInfo");
    var documentoInfo = elemento.querySelector("#documentoInfo");
    var fechaNacInfo = elemento.querySelector("#fechaNacInfo");
    
    var nombreRecib = document.getElementById("nombreRecib");
    var correoRecib = document.getElementById("correoRecib");
    var documentoRecib = document.getElementById("documentoRecib");
    var fechaRecib = document.getElementById("fechaRecib");

    if (nombreInfo && correoInfo && documentoInfo && fechaNacInfo) {
        nombreRecib.textContent = nombreInfo.textContent;
        correoRecib.textContent = correoInfo.textContent;
        documentoRecib.textContent = documentoInfo.textContent;
        fechaRecib.textContent = fechaNacInfo.textContent;
    }
}

function empresas(elemento){
    var nombreInfo = elemento.querySelector("#nombreInfo");
    var correoInfo = elemento.querySelector("#correoInfo");
    var documentoInfo = elemento.querySelector("#documentoInfo");
    var telefonoInfo = elemento.querySelector("#telefonoInfo");
    
    var nombreRecib = document.getElementById("nombreRecib");
    var correoRecib = document.getElementById("correoRecib");
    var documentoRecib = document.getElementById("documentoRecib");
    var telefonoRecib = document.getElementById("telefonoRecib");

    if (nombreInfo && correoInfo && documentoInfo && telefonoInfo) {
        nombreRecib.textContent = nombreInfo.textContent;
        correoRecib.textContent = correoInfo.textContent;
        documentoRecib.textContent = documentoInfo.textContent;
        telefonoRecib.textContent = telefonoInfo.textContent;
    }
}

function cursos(elemento){
    var nombreInfo = elemento.querySelector("#nombreInfo");
    var documentoInfo = elemento.querySelector("#documentoInfo");
    var precioInfo = elemento.querySelector("#precioInfo");
    var lenguajeInfo = elemento.querySelector("#lenguajeInfo");
    var nivelInfo = elemento.querySelector("#nivelInfo");
    var tiempoInfo = elemento.querySelector("#tiempoInfo");
    var certificadoInfo = elemento.querySelector("#certificadoInfo");
    
    var nombreRecib = document.getElementById("nombreRecib");
    var documentoRecib = document.getElementById("documentoRecib");
    var precioRecib = document.getElementById("precioRecib");
    var lenguajeRecib = document.getElementById("lenguajeRecib");
    var nivelRecib = document.getElementById("nivelRecib");
    var tiempoRecib = document.getElementById("tiempoRecib");
    var certificadoRecib = document.getElementById("certificadoRecib");

    if (nombreInfo && documentoInfo && precioInfo && lenguajeInfo && nivelInfo && tiempoInfo && certificadoInfo) {
        nombreRecib.textContent = nombreInfo.textContent;
        documentoRecib.textContent = documentoInfo.textContent;
        precioRecib.textContent = precioInfo.textContent;
        lenguajeRecib.textContent = lenguajeInfo.textContent;
        nivelRecib.textContent = nivelInfo.textContent;
        tiempoRecib.textContent = tiempoInfo.textContent;
        certificadoRecib.textContent = certificadoInfo.textContent;
    }
}

function ofertas(elemento){
    var nombreInfo = elemento.querySelector("#nombreInfo");
    var documentoInfo = elemento.querySelector("#documentoInfo");
    var salarioInfo = elemento.querySelector("#salarioInfo");
    var estadoInfo = elemento.querySelector("#estadoInfo");
    
    var nombreRecib = document.getElementById("nombreRecib");
    var documentoRecib = document.getElementById("documentoRecib");
    var salarioRecib = document.getElementById("salarioRecib");
    var estadoRecib = document.getElementById("estadoRecib");

    if (nombreInfo && documentoInfo && salarioInfo && estadoInfo) {
        nombreRecib.textContent = nombreInfo.textContent;
        documentoRecib.textContent = documentoInfo.textContent;
        salarioRecib.textContent = salarioInfo.textContent;
        estadoRecib.textContent = estadoInfo.textContent;
    }
}