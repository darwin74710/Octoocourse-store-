from estudiantes.models import Estudiantes, HojasDeVida, Idiomas, Aptitudes, FormacionesAcademicas, LenguajesProg, ExpLaborales
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def Configuracion(request):
    Tablas = obtenerTablasHV()
    return render(request, 'estudiantes/Configuracion.html', Tablas)

def obtenerTablasHV():
    #Elijo las tablas que quiero enviar al render filtrandola.
    estudiantes = Estudiantes.objects.filter(id_estudiante=1)

    #Condicional para encontrar el primer resultado o no enviar nada en caso de que no lo encuentre.
    if estudiantes.exists():
        estudiante = estudiantes[0]
    else:
        estudiante = None
    
    hojasDeVida = HojasDeVida.objects.filter(id_estudiante=estudiante.id_estudiante)

    if hojasDeVida.exists():
        hojaDeVida = hojasDeVida[0]
    else:
        hojaDeVida = None
    
    idiomas = Idiomas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
    aptitudes = Aptitudes.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
    lenguajesProg = LenguajesProg.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
    formaciones = FormacionesAcademicas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
    expLaborales = ExpLaborales.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
    
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