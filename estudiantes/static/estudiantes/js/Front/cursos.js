/* ACTIVAR O DESACTIVAR LOS FILTROS */
function encontrar_filtros(tipoFiltro) {
    const filtrado = document.getElementById("filtrado");
    var dato;
    let checkButton;

    checkButton = document.getElementById(tipoFiltro + 'Filter');
    dato = "|" + tipoFiltro;

    change_filtros(checkButton, dato, filtrado);
}

function change_filtros(checkButton, dato, filtrado){
    if (checkButton) {
        if (checkButton.classList.contains('bi-check-square')) {
            checkButton.classList.remove('bi-check-square');
            checkButton.style.color = "var(--letra1)";
            checkButton.classList.add('bi-square');

            filtrado.innerHTML = filtrado.innerHTML.replace(dato, "");
        } else {
            checkButton.classList.remove('bi-square');
            checkButton.style.color = "#8021bb";
            checkButton.classList.add('bi-check-square');

            filtrado.innerHTML += dato;
        }
    }
}

function aplicarFiltros() {
    const filtrado = document.getElementById("filtrado").textContent;
    const filtros = filtrado.split("|").filter(f => f);

    const url = new URL(window.location.href);
    url.searchParams.set("filtros", JSON.stringify(filtros));
    window.location.href = url;
}

function ContenidoCursos(elementoSuperior){
    const divInferior = elementoSuperior.parentElement.querySelector('#inferior');

    if (divInferior.style.height === "0px" || divInferior.style.height === "") {
        divInferior.style.height = divInferior.scrollHeight + "px";
    } else {
        divInferior.style.height = "0px";
    }
}