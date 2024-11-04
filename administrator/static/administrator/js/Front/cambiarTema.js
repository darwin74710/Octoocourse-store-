function changeTema(tipoTema){
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