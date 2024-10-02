from django.shortcuts import render

def estudiantes(request):
    return render(request, 'estudiantes/estudiantes.html')

def curso(request):
    return render(request, 'estudiantes/curso.html')