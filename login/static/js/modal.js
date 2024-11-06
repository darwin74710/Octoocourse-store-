var modal = document.getElementById("forgot-password-modal");

var link = document.getElementById("forgot-password-link");

var span = document.getElementsByClassName("close")[0];

link.onclick = function (event) {
  event.preventDefault();
  modal.style.display = "block";
};

span.onclick = function () {
  modal.style.display = "none";
};

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

document.addEventListener("DOMContentLoaded", function () {
  const showPasswordCheckbox = document.getElementById("show-password");
  const passwordInput = document.getElementById("password");

  showPasswordCheckbox.addEventListener("change", function () {
    passwordInput.type = this.checked ? "text" : "password";
  });
});
