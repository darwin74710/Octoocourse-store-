function cambiarTema(){
    var numTema = localStorage.getItem('numTema') ? parseInt(localStorage.getItem('numTema')) : 1;

    if(numTema === 2){ 
        numTema = 1;
        localStorage.setItem('numTema', numTema);
        aplicarEstilos();
        location.reload();
    }else if(numTema === 1){
        numTema = 2;
        localStorage.setItem('numTema', numTema);
        aplicarEstilos();
        location.reload();
    }
}