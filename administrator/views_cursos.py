from django.shortcuts import render
from administrator.models_cursos import Cursos, TipoContenido, TipoDificultad, TipoDuracion, TipoCertificado, Contenidos, SubContenidos, PreguntasCurso, RespuestasCurso
from django.db import connection, transaction
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.urls import reverse

def cursoAdmin(request):
    cursos = Cursos.objects.all()
    tipoContenido = TipoContenido.objects.all()
    tipoDificultad = TipoDificultad.objects.all()
    tipoDuracion = TipoDuracion.objects.all()
    tipoCertificado = TipoCertificado.objects.all()

    Datos = {
        'cursos': cursos,
        'tipoContenido': tipoContenido,
        'tipoDificultad': tipoDificultad,
        'tipoDuracion': tipoDuracion,
        'tipoCertificado': tipoCertificado,
    }

    return render(request, 'administrator/modifiCursos.html', Datos)

@csrf_exempt
def cursoAñadir(request):
    nombreCursoDato = request.POST.get('nombreCurso').strip()
    precioDato = request.POST.get('precio')
    contenidoDato = request.POST.get('contenido')
    dificultadDato = request.POST.get('dificultad')
    tiempoDato = request.POST.get('tiempo')
    certificadoDato = request.POST.get('certificado')
    descripcionDato = request.POST.get('descripcion').strip()

    urlImagenDato = "html.jpg"
    if contenidoDato == 1:
         urlImagenDato = "html.jpg"

    # Validaciones
    if nombreCursoDato == "":
        return JsonResponse({'status': 'error', 'message': 'El curso necesita un nombre.'})
    if precioDato == "":
        return JsonResponse({'status': 'error', 'message': 'El curso necesita un precio, puede dejarlo sin costo con el valor 0.'})
    
    try:
        with transaction.atomic():
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "INSERT INTO CURSOS (nom_curso, precio, id_tipo_contenido, id_tipo_dificultad, id_tipo_duracion, id_tipo_certificado, descripcion, url_imagen) " +
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                            [nombreCursoDato, precioDato, contenidoDato, dificultadDato, tiempoDato, certificadoDato, descripcionDato, urlImagenDato]
                        )
        return JsonResponse({'status': 'success', 'message': 'El curso se añadio correctamente.'})
    except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

def cursoEditar(request):
    idCurso = request.GET.get('idCurso')
    curso = Cursos.objects.filter(id_curso = idCurso).first()

    tipoContenido = TipoContenido.objects.all()
    tipoDificultad = TipoDificultad.objects.all()
    tipoDuracion = TipoDuracion.objects.all()
    tipoCertificado = TipoCertificado.objects.all()

    Datos = {
        'curso': curso,
        'tipoContenido': tipoContenido,
        'tipoDificultad': tipoDificultad,
        'tipoDuracion': tipoDuracion,
        'tipoCertificado': tipoCertificado,
    }

    return render(request, 'administrator/cursoEditar.html', Datos)

def cursoEliminar(request):
    idCurso = request.GET.get('idCurso')
    curso = Cursos.objects.filter(id_curso = idCurso).first()

    if curso is None:
        return HttpResponse("Curso no encontrado", status=404)
    else:
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM CURSOS_DISPONIBLES WHERE ID_CURSO = %s",
                    [idCurso]
                )
                cursor.execute(
                    "DELETE FROM CURSOS_APROBADOS WHERE ID_CURSO = %s",
                    [idCurso]
                )
                cursor.execute(
                    "DELETE FROM CONTENIDOS WHERE ID_CURSO = %s",
                    [idCurso]
                )
                cursor.execute(
                    "DELETE FROM PREGUNTAS_CURSO WHERE ID_CURSO = %s",
                    [idCurso]
                )
                cursor.execute(
                    "DELETE FROM CURSOS WHERE ID_CURSO = %s",
                    [idCurso]
                )

    return redirect('cursoAdmin')

def cursoContenidos(request):
    idCurso = request.GET.get('idCurso')
    curso = Cursos.objects.filter(id_curso = idCurso).first()

    contenidos = Contenidos.objects.filter(id_curso = curso)
    subcontenidos = SubContenidos.objects.filter(id_contenido__in=contenidos)

    Datos = {
        'curso': curso,
        'contenidos': contenidos,
        'subcontenidos': subcontenidos,
    }

    return render(request, 'administrator/modifiContenidos.html', Datos)

def cursoPreguntas(request):
    idCurso = request.GET.get('idCurso')
    curso = Cursos.objects.filter(id_curso = idCurso).first()

    preguntas = PreguntasCurso.objects.filter(id_curso = curso)
    respuestas = RespuestasCurso.objects.filter(id_pregunta__in=preguntas)

    Datos = {
        'curso': curso,
        'preguntas': preguntas,
        'respuestas': respuestas,
    }

    return render(request, 'administrator/modifiPreguntas.html', Datos)

@csrf_exempt
def crearContenido(request):
    if request.method == 'POST':
        nombreContenido = request.POST.get('contentNombre').strip()
        cursoIdCrearContent = request.POST.get('cursoIdCrearContent')

        # Validaciones
        if nombreContenido == "":
            return JsonResponse({'status': 'error', 'message': 'El contenido necesita un nombre.'})
        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO CONTENIDOS (nom_contenido, id_curso) " +
                        "VALUES (%s, %s)",
                        [nombreContenido, cursoIdCrearContent]
                    )
            return JsonResponse({'status': 'success', 'message': 'El contenido se añadio correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        
@csrf_exempt
def editarContenido(request):
    if request.method == 'POST':
        nombreContenido = request.POST.get('contentNombre').strip()
        idContent = request.POST.get('idContentInput')

        # Validaciones
        if nombreContenido == "":
            return JsonResponse({'status': 'error', 'message': 'El contenido necesita un nombre.'})
        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE CONTENIDOS SET nom_contenido = %s WHERE id_contenido = %s",
                        [nombreContenido, idContent]
                    )
            return JsonResponse({'status': 'success', 'message': 'El contenido se modificó correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        
@csrf_exempt
def eliminarContenido(request):
    idContenido = request.GET.get('idContenido')
    idCurso = request.GET.get('idCurso')

    with transaction.atomic():
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM CONTENIDOS WHERE id_contenido = %s",
                [idContenido]
            )
    
    return redirect(f'{reverse("cursoContenidos")}?idCurso={idCurso}')

@csrf_exempt
def crearSubContenido(request):
    if request.method == 'POST':
        nombreSubContenido = request.POST.get('nombreSubContenido').strip()
        urlSubContenido = request.POST.get('urlSubContenido').strip()
        idContenido = request.POST.get('idContenido')

        # Validaciones
        if nombreSubContenido == "":
            return JsonResponse({'status': 'error', 'message': 'El sub contenido necesita un nombre.'})
        if urlSubContenido == "":
            return JsonResponse({'status': 'error', 'message': 'El sub contenido necesita una url para el powerpoint de OneDrive.'})
        
        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO SUB_CONTENIDOS (nom_subcont, url_cont, id_contenido) " +
                        "VALUES (%s, %s, %s)",
                        [nombreSubContenido, urlSubContenido, idContenido]
                    )
            return JsonResponse({'status': 'success', 'message': 'El sub contenido se añadio correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        
@csrf_exempt
def editarSubContenido(request):
    if request.method == 'POST':
        nombreSubContenido = request.POST.get('nombreSubContenido').strip()
        urlSubContenido = request.POST.get('urlSubContenido').strip()
        idSubContenido = request.POST.get('idSubContenido')

        # Validaciones
        if nombreSubContenido == "":
            return JsonResponse({'status': 'error', 'message': 'El sub contenido necesita un nombre.'})
        if urlSubContenido == "":
            return JsonResponse({'status': 'error', 'message': 'El sub contenido necesita una url para el powerpoint de OneDrive.'})
        
        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE SUB_CONTENIDOS SET nom_subcont = %s, url_cont = %s WHERE id_subcont = %s",
                        [nombreSubContenido, urlSubContenido, idSubContenido]
                    )
            return JsonResponse({'status': 'success', 'message': 'El sub contenido se modificó correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        
@csrf_exempt
def eliminarSubContenido(request):
    idSubContenido = request.GET.get('idSubContenido')
    idCurso = request.GET.get('idCurso')

    with transaction.atomic():
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM SUB_CONTENIDOS WHERE id_subcont = %s",
                [idSubContenido]
            )
    
    return redirect(f'{reverse("cursoContenidos")}?idCurso={idCurso}')

@csrf_exempt
def crearPregunta(request):
    if request.method == 'POST':
        textPregunta = request.POST.get('contentPregunta').strip()
        cursoIdCrearContent = request.POST.get('cursoIdCrearContent')

        # Validaciones
        if textPregunta == "":
            return JsonResponse({'status': 'error', 'message': 'La pregunta no se puede dejar vacía.'})
        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO PREGUNTAS_CURSO (pregunta_text, id_curso) " +
                        "VALUES (%s, %s)",
                        [textPregunta, cursoIdCrearContent]
                    )
            return JsonResponse({'status': 'success', 'message': 'La pregunta se añadio correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        
@csrf_exempt
def editarPregunta(request):
    if request.method == 'POST':
        textoPregunta = request.POST.get('contentPregunta').strip()
        idPregunta = request.POST.get('idPreguntaInput')
        print('almeja')

        # Validaciones
        if textoPregunta == "":
            return JsonResponse({'status': 'error', 'message': 'La pregunta no se puede dejar vacía.'})
        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE PREGUNTAS_CURSO SET pregunta_text = %s WHERE id_pregunta = %s",
                        [textoPregunta, idPregunta]
                    )
            return JsonResponse({'status': 'success', 'message': 'La pregunta se modificó correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        
@csrf_exempt
def eliminarPregunta(request):
    idPregunta = request.GET.get('idPregunta')
    idCurso = request.GET.get('idCurso')

    with transaction.atomic():
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM PREGUNTAS_CURSO WHERE id_pregunta = %s",
                [idPregunta]
            )
    
    return redirect(f'{reverse("cursoPreguntas")}?idCurso={idCurso}')
        
@csrf_exempt
def crearRespuesta(request):
    if request.method == 'POST':
        textRespuesta = request.POST.get('textRespuesta').strip()
        validacionRespuesta = request.POST.get('validacionRespuesta').strip()
        idPregunta = request.POST.get('idPregunta')

        # Validaciones
        if textRespuesta == "":
            return JsonResponse({'status': 'error', 'message': 'La respuesta no se puede dejar vacía.'})
        
        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO RESPUESTAS_CURSO (respuesta_text, validacion, id_pregunta) " +
                        "VALUES (%s, %s, %s)",
                        [textRespuesta, validacionRespuesta, idPregunta]
                    )
            return JsonResponse({'status': 'success', 'message': 'La respuesta se añadio correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        
@csrf_exempt
def editarRespuesta(request):
    if request.method == 'POST':
        textoRespuesta = request.POST.get('textoRespuesta').strip()
        validacionRespuesta = request.POST.get('validacionRespuesta').strip()
        idRespuesta = request.POST.get('idRespuesta')

        # Validaciones
        if textoRespuesta == "":
            return JsonResponse({'status': 'error', 'message': 'La respuesta no se puede dejar vacía.'})
        
        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE RESPUESTAS_CURSO SET respuesta_text = %s, validacion = %s WHERE id_respuesta = %s",
                        [textoRespuesta, validacionRespuesta, idRespuesta]
                    )
            return JsonResponse({'status': 'success', 'message': 'El sub contenido se modificó correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

@csrf_exempt
def eliminarRespuesta(request):
    idRespuesta = request.GET.get('idRespuesta')
    idCurso = request.GET.get('idCurso')

    with transaction.atomic():
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM RESPUESTAS_CURSO WHERE id_respuesta = %s",
                [idRespuesta]
            )
    
    return redirect(f'{reverse("cursoPreguntas")}?idCurso={idCurso}')