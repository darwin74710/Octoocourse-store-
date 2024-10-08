from django.shortcuts import render

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