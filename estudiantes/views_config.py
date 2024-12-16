from estudiantes.models import Estudiantes, HojasDeVida, Idiomas, Aptitudes, FormacionesAcademicas, LenguajesProg, ExpLaborales
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from functools import wraps


def estudiante_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Verifica si el usuario tiene una sesión válida como empresa
        if request.session.get('id_estudiante'): 
            return view_func(request, *args, **kwargs)
        else:
            return redirect('acceso_denegado')  
    return wrapper

@login_required(login_url=reverse_lazy('inicioS'))
@estudiante_required
def Configuracion(request):
    id_Estudiante = request.session.get('id_estudiante')
    Tablas = obtenerTablasHV(id_Estudiante)

    return render(request, 'estudiantes/Configuracion.html', Tablas)

def obtenerTablasHV(id):
    #Elijo las tablas que quiero enviar al render filtrandola.
    estudiantes = Estudiantes.objects.filter(id_estudiante=id)

    #Condicional para encontrar el primer resultado o no enviar nada en caso de que no lo encuentre.
    if estudiantes.exists():
        estudiante = estudiantes[0]
    
        hojasDeVida = HojasDeVida.objects.filter(id_estudiante=estudiante.id_estudiante)

        if hojasDeVida.exists():
            hojaDeVida = hojasDeVida.first()
        else:
            hojaDeVida = HojasDeVida.objects.create(id_hoja_vida=estudiante.id_estudiante, id_estudiante=estudiante)

        aptitudes = Aptitudes.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        idiomas = Idiomas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        lenguajesProg = LenguajesProg.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        expLaborales = ExpLaborales.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        formaciones = FormacionesAcademicas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)

        if aptitudes.count() < 6:
            restantes = 6 - aptitudes.count()
            for _ in range(restantes):
                Aptitudes.objects.create(id_hojavida=hojaDeVida)
            aptitudes = Aptitudes.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)

        if idiomas.count() < 3:
            restantes = 3 - idiomas.count()
            for _ in range(restantes):
                Idiomas.objects.create(id_hojavida=hojaDeVida) 
            idiomas = Idiomas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)

        if lenguajesProg.count() < 6:
            restantes = 6 - lenguajesProg.count()
            for _ in range(restantes):
                LenguajesProg.objects.create(id_hojavida=hojaDeVida)
            lenguajesProg = LenguajesProg.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)

        if expLaborales.count() < 2:
            restantes = 2 - expLaborales.count()
            for _ in range(restantes):
                ExpLaborales.objects.create(id_hojavida=hojaDeVida)
            expLaborales = ExpLaborales.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)

        if formaciones.count() < 2:
            restantes = 2 - formaciones.count()
            for _ in range(restantes):
                FormacionesAcademicas.objects.create(id_hojavida=hojaDeVida) 
            formaciones = FormacionesAcademicas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
    
    else:
        estudiante = None
        hojaDeVida = None
        idiomas = None
        aptitudes = None
        lenguajesProg = None
        formaciones = None
        expLaborales = None
    
    #Esto es un diccionario para enviarle varias tablas a la vista
    Datos = {
        'estudiantes': estudiante,
        'hojasDeVida': hojaDeVida,
        'idiomas': idiomas,
        'aptitudes': aptitudes,
        'lenguajesProg': lenguajesProg,
        'formaciones': formaciones,
        'expLaborales': expLaborales,
    }

    return Datos


def acceso_denegado(request):
    return render(request, 'acceso_denegado.html', {'mensaje': 'No tienes permiso para acceder a esta sección.'})