function ShowUser(){
    var usu_despleg = document.getElementsByClassName("desp-usuario")[0];
    var noti_despleg = document.getElementsByClassName("desp-notifi")[0];

    if(noti_despleg.style.display != "none"){
        noti_despleg.style.display = "none";
    }
    
    if(usu_despleg.style.display == "none" || usu_despleg.style.display != "block"){
        usu_despleg.style.display = "block";
    }else{
        usu_despleg.style.display = "none";
    }
}

function ShowNoti(){
    var usu_despleg = document.getElementsByClassName("desp-usuario")[0];
    var noti_despleg = document.getElementsByClassName("desp-notifi")[0];

    if(usu_despleg.style.display != "none"){
        usu_despleg.style.display = "none";
    }

    if(noti_despleg.style.display == "none" || noti_despleg.style.display != "block"){
        noti_despleg.style.display = "block";
    }else{
        noti_despleg.style.display = "none";
    }
}

function Exit(){
    var usu_despleg = document.getElementsByClassName("desp-usuario")[0];
    usu_despleg.style.display = "none";
}