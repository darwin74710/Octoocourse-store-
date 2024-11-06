from django.shortcuts import render
from administrator.models_cursos import Cursos

def cursoAdmin(request):
    cursos = Cursos.objects.all()

    return render(request, 'administrator/modifiCursos.html', {'cursos': cursos})

def cursoEditar(request):
    idCurso = request.GET.get('idCurso')
    curso = Cursos.objects.filter(id_curso = idCurso).first()

    return render(request, 'administrator/cursoEditar.html', {'curso': curso})