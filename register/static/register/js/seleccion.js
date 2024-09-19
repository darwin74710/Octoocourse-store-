function mostrarFormulario(tipo) {
    document.getElementById('form-estudiante').style.display = 'none';
    document.getElementById('form-empresa').style.display = 'none';
    if (tipo === 'estudiante') {
        document.getElementById('form-estudiante').style.display = 'block';
        document.getElementById('titulo-principal').innerHTML = '<span>Estudiante</span>';
    } else if (tipo === 'empresa') {
        document.getElementById('form-empresa').style.display = 'block';
        document.getElementById('titulo-principal').innerHTML = '<span>Empresa</span>';
    }
}