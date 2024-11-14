from django.shortcuts import render
from administrator.models_estudiantes import Estudiantes, HojasDeVida, Idiomas, Aptitudes, FormacionesAcademicas, LenguajesProg, ExpLaborales
from django.db import connection, transaction
from django.http import HttpResponse
from django.shortcuts import redirect

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

def estudianteEliminar(request):
    idEstud = request.GET.get('idEstudiante')
    estudiante = Estudiantes.objects.filter(id_estudiante = idEstud).first()

    if estudiante is None:
        return HttpResponse("Estudiante no encontrado", status=404)
    else:
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM RESPUESTAS_OFERTAS WHERE ID_ESTUDIANTE = %s",
                    [idEstud]
                )
                cursor.execute(
                    "DELETE FROM OFERTAS_DISPONIBLES WHERE ID_ESTUDIANTE = %s",
                    [idEstud]
                )
                cursor.execute(
                    "DELETE FROM CURSOS_APROBADOS WHERE ID_ESTUDIANTE = %s",
                    [idEstud]
                )
                cursor.execute(
                    "DELETE FROM CURSOS_DISPONIBLES WHERE ID_ESTUDIANTE = %s",
                    [idEstud]
                )
        

            hojasDeVida = HojasDeVida.objects.filter(id_estudiante=estudiante.id_estudiante)
            if hojasDeVida.exists():
                hojaDeVida = hojasDeVida.first()
                aptitudes = Aptitudes.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
                idiomas = Idiomas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
                lenguajesProg = LenguajesProg.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
                expLaborales = ExpLaborales.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
                formaciones = FormacionesAcademicas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)

                with connection.cursor() as cursor:
                    for aptitud in aptitudes:
                        cursor.execute(
                            "DELETE FROM APTITUDES WHERE ID_APTITUDES = %s",
                            [aptitud.id_aptitudes]
                        )
                    for idioma in idiomas:
                        cursor.execute(
                            "DELETE FROM IDIOMAS WHERE ID_IDIOMA = %s",
                            [idioma.id_idioma]
                        )
                    for lenguaje in lenguajesProg:
                        cursor.execute(
                            "DELETE FROM LENGUAJES_PROG WHERE ID_LENGUAJE = %s",
                            [lenguaje.id_lenguaje]
                        )
                    for expLaboral in expLaborales:
                        cursor.execute(
                            "DELETE FROM EXP_LABORALES WHERE ID_EXP = %s",
                            [expLaboral.id_exp]
                        )
                    for formacion in formaciones:
                        cursor.execute(
                            "DELETE FROM FORMACIONES_ACADEMICAS WHERE ID_FORMACION = %s",
                            [formacion.id_formacion]
                        )
                    cursor.execute(
                        "DELETE FROM HOJAS_DE_VIDA WHERE ID_ESTUDIANTE = %s",
                        [idEstud]
                    )
                
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM ESTUDIANTES WHERE ID_ESTUDIANTE = %s",
                    [idEstud]
                )
    return redirect('estudiantesAdmin')