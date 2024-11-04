from django.shortcuts import render
from administrator.models_estudiantes import Estudiantes

def estudiantesAdmin(request):
    estudiantes = Estudiantes.objects.all()
    
    return render(request, 'administrator/modifiEstudiantes.html',{'estudiantes': estudiantes})