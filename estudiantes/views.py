from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required 
def Inicio(request):
    return render(request, 'estudiantes/Inicio.html')

def Cursos(request):
    return render(request, 'estudiantes/Cursos.html')

def Ofertas(request):
    return render(request, 'estudiantes/Ofertas.html')

def Configuracion(request):
    return render(request, 'estudiantes/Configuracion.html')

def OfertasInfo(request):
    return render(request, 'estudiantes/OfertasInfo.html')


def logout_view(request):
    logout(request)  
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('home')  