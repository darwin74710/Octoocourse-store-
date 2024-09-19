 // Obtener el modal
 var modal = document.getElementById("forgot-password-modal");

 // Obtener el enlace que abre el modal
 var link = document.getElementById("forgot-password-link");

 // Obtener el elemento <span> que cierra el modal
 var span = document.getElementsByClassName("close")[0];

 // Cuando el usuario hace clic en el enlace, abre el modal
 link.onclick = function(event) {
     event.preventDefault();
     modal.style.display = "block";
 }

 // Cuando el usuario hace clic en <span> (x), cierra el modal
 span.onclick = function() {
     modal.style.display = "none";
 }

 // Cuando el usuario hace clic en cualquier lugar fuera del modal, cierra el modal
 window.onclick = function(event) {
     if (event.target == modal) {
         modal.style.display = "none";
     }
 }