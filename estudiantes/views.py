from django.shortcuts import render

def home_estudiantes(request):
    return render(request, 'estudiantes/index.html')