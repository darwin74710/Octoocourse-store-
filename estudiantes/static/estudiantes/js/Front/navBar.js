/*ESTO ES PARA EL MENU DE HAMBURGUESA */
function activarMenu() {
    const sideMenu = document.getElementById("menuHamburguersa");
    /*Para cambiar el tamaño del slide menu*/
    if (sideMenu.style.width === "250px") {
        sideMenu.style.width = "0";
    } else {
        sideMenu.style.width = "250px";
    }
}