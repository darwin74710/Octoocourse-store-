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
  const modal = document.getElementById("modalMisDatos");
  const overlay = document.getElementById("modalOverlay");

  if (action === "misDatosActive") {
    modal.style.display = "flex";
    overlay.style.display = "block";
  } else if (action === "misDatosDesactive") {
    modal.style.display = "none";
    overlay.style.display = "none";
  }
}

function cerrarModal() {
  document.getElementById("modalMisDatos").style.display = "none";
  document.getElementById("modalOverlay").style.display = "none";
}

function cargarDatosEmpresa() {
    fetch('/mis-datos/', {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Llenar el contenido del modal con los datos recibidos
        document.getElementById('contenidoMisDatos').innerHTML = `
            <div class="campo"><label>Nombre:</label><span>${data.nombre}</span></div>
            <div class="campo"><label>Correo:</label><span>${data.correo}</span></div>
            <div class="campo"><label>NIT:</label><span>${data.nit}</span></div>
            <div class="campo"><label>Ofertas Creadas:</label><span>${data.ofertas_creadas}</span></div>
            <div class="campo"><label>Ofertas Activas:</label><span>${data.ofertas_activas}</span></div>
            <div class="campo"><label>Ofertas Desactivadas:</label><span>${data.ofertas_desactivadas}</span></div>
        `;
        // Mostrar el modal
        document.getElementById('modalMisDatos').style.display = 'block';
    })
    .catch(error => console.error('Error:', error));
}

