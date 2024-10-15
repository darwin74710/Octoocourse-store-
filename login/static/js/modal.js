 var modal = document.getElementById("forgot-password-modal");

 var link = document.getElementById("forgot-password-link");

 var span = document.getElementsByClassName("close")[0];

 link.onclick = function(event) {
     event.preventDefault();
     modal.style.display = "block";
 }

 span.onclick = function() {
     modal.style.display = "none";
 }

 window.onclick = function(event) {
     if (event.target == modal) {
         modal.style.display = "none";
     }
 }