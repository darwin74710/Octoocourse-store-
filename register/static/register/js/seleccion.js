function mostrarFormulario(tipo) {
    // Hide both forms and images
    document.getElementById('form-estudiante').style.display = 'none';
    document.getElementById('form-empresa').style.display = 'none';
    document.getElementById('img-estudiante').style.display = 'none';
    document.getElementById('img-empresa').style.display = 'none';

    // Show the selected form and image
    if (tipo === 'estudiante') {
        document.getElementById('form-estudiante').style.display = 'block';
        document.getElementById('img-estudiante').style.display = 'inline-block';
    } else if (tipo === 'empresa') {
        document.getElementById('form-empresa').style.display = 'block';
        document.getElementById('img-empresa').style.display = 'inline-block';
    }

    // Update the title
    document.getElementById('titulo-principal').innerHTML = tipo === 'estudiante' ? 
        '<span>Estudiante</span>' : '<span>Empresa</span>';
}