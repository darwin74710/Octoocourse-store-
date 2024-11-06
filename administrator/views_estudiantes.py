from django.shortcuts import render
from estudiantes.models import Estudiantes, HojasDeVida, Idiomas, Aptitudes, FormacionesAcademicas, LenguajesProg, ExpLaborales

def estudiantesAdmin(request):
    estudiantes = Estudiantes.objects.all()
    
    return render(request, 'administrator/modifiEstudiantes.html',{'estudiantes': estudiantes})

def hojaVidaVisualizar(request):
    idEstud = request.GET.get('idEstudiante')

    estudiantes = Estudiantes.objects.filter(id_estudiante = idEstud)

    #Condicional para encontrar el primer resultado o no enviar nada en caso de que no lo encuentre.
    if estudiantes.exists():
        estudiante = estudiantes[0]
    else:
        estudiante = None

    hojasDeVida = HojasDeVida.objects.filter(id_estudiante=estudiante.id_estudiante)

    if hojasDeVida.exists():
        hojaDeVida = hojasDeVida[0]
        idiomas = Idiomas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        aptitudes = Aptitudes.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        lenguajesProg = LenguajesProg.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        formaciones = FormacionesAcademicas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        expLaborales = ExpLaborales.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
    else:
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

    return render(request, 'administrator/hojaVidaVisualizar.html', Datos)

def estudianteEditar(request):
    idEstud = request.GET.get('idEstudiante')
    estudiante = Estudiantes.objects.filter(id_estudiante = idEstud).first()


    return render(request, 'administrator/estudianteEditar.html', {'estudiante': estudiante})