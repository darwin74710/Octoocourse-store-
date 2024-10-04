function NavegacionAdmin(nav){
    console.log("click a " + nav);
    var marcoCV = document.getElementsByClassName("marcoCV")[0];
    var marcoOfertas = document.getElementsByClassName("marcoOfertas")[0];
    var marcoUsuarios = document.getElementsByClassName("marcoUsuarios")[0];

    marcoCV.style.display = "none";
    marcoOfertas.style.display = "none";
    marcoUsuarios.style.display = "none";

    if(nav === 'marcoCV'){
        marcoCV.style.display = "block";
    }else if(nav === 'marcoOfertas'){
        marcoOfertas.style.display = "block";
    }else if(nav === 'marcoUsuarios'){
        marcoUsuarios.style.display = "block";
    }
}