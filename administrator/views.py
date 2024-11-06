from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from administrator.models_estudiantes import Estudiantes
from administrator.models_empresas import Empresas, OfertasEmpleos
from administrator.models_cursos import Cursos

def administratorAdmin(request):
    numEstud = Estudiantes.objects.count()
    numEmpresas = Empresas.objects.count()
    numCursos = Cursos.objects.count()
    numOfertas = OfertasEmpleos.objects.count()
    
    Datos = {
        'numEstud': numEstud,
        'numEmpresas': numEmpresas,
        'numCursos': numCursos,
        'numOfertas': numOfertas,
    }

    return render(request, 'administrator/administrator.html', Datos)

def logout_view(request):
    logout(request)  
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('home')  
