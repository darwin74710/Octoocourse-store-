var numTema = localStorage.getItem('numTema') ? parseInt(localStorage.getItem('numTema')) : 1;

function aplicarEstilos() {
    var style = document.createElement('style');

    if (numTema === 1){
        style.innerHTML = `
        :root {
            /*Tema Claro*/
            --fondo1: #dbdbdb;
        
            --borde1: gray;
            --letra1: black;
        
            --letratitulo1: #8021bb;
            --fondoTitulo2: #250338;
            --letraTitulo2: #dbdbdb;
            
            --fondoBotones1: #8021bb;
            --letraBotones1: #dbdbdb;
            --hFondoBotones1: #560581;
            --hLetraBotones1: #2e0346;
        
            --fondoBotones2: #dbdbdb;
        }
        `;
    }else if (numTema === 2){
        style.innerHTML = `
        :root {
            /*Tema Oscuro*/
            --fondo1: #0a0523;
        
            --borde1: #540f79;
            --letra1: #dbdbdb;
        
            --letratitulo1: #8021bb;
            --fondoTitulo2: #3c0d55;
            --letraTitulo2: #b84ffa;
            
            --fondoBotones1: #8021bb;
            --letraBotones1: #dbdbdb;
            --hFondoBotones1: #560581;
            --hLetraBotones1: #2e0346;
        
            --fondoBotones2: #29063d;
        }
        `;
    }

    document.head.appendChild(style);
}

aplicarEstilos();