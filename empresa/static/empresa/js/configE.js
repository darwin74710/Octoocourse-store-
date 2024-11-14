function cambiarTema(tipoTema) {
  if (tipoTema === "claro") {
    numTema = 1;
    localStorage.setItem("numTema", numTema);
    aplicarEstilos();
    seleccionTema();
  } else if (tipoTema === "oscuro") {
    numTema = 2;
    localStorage.setItem("numTema", numTema);
    aplicarEstilos();
    seleccionTema();
  }
}

function seleccionTema() {
  const claro = document.getElementById("temaElect1");
  const oscuro = document.getElementById("temaElect2");

  claro.classList.remove("bi-circle", "bi-circle-fill");
  oscuro.classList.remove("bi-circle", "bi-circle-fill");

  if (numTema === 1) {
    claro.classList.add("bi-circle-fill");
    oscuro.classList.add("bi-circle");
  } else if (numTema === 2) {
    oscuro.classList.add("bi-circle-fill");
    claro.classList.add("bi-circle");
  }
}



function modalConfig(action) {
  const modal = document.getElementById("modalConfig"); 
  const overlay = document.getElementById("modalOverlay");

  if (action === "contraActive") {
    modal.style.display = "block"; 
    overlay.style.display = "block"; 
  } else if (action === "contraDesactive") {
    modal.style.display = "none"; 
    overlay.style.display = "none"; 
  }
}

function cerrarModal() {
  const modalMisDatos = document.getElementById("modalMisDatos");
  const overlay = document.getElementById("modalOverlay");
  modalMisDatos.style.display = "none";
  overlay.style.display = "none";
}

function abrirModal() {
  const modalMisDatos = document.getElementById('modalMisDatos');
  const overlay = document.getElementById('modalOverlay');
  modalMisDatos.style.display = 'block';
  overlay.style.display = 'block';
}

function cerrarModal() {
  document.getElementById('modalMisDatos').style.display = 'none';
  document.getElementById('modalOverlay').style.display = 'none';
}
