from django.shortcuts import render
from administrator.models_cursos import Cursos

def cursoAdmin(request):
    cursos = Cursos.objects.all()

    return render(request, 'administrator/modifiCursos.html', {'cursos': cursos})