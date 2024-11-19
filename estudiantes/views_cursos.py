from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from estudiantes.models_cursos import Cursos, Contenidos, SubContenidos, CursosDisponibles, CursosAprobados, TipoContenido, TipoCertificado, TipoDificultad, TipoDuracion, PreguntasCurso, RespuestasCurso
from estudiantes.models import Estudiantes, HojasDeVida
from django.contrib import messages
from django.db.models import Q
import json
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from datetime import date

@login_required(login_url=reverse_lazy('inicioS'))
def Inicio(request):
    idStudent = request.session.get('id_estudiante')
    estudiantes = Estudiantes.objects.filter(id_estudiante=idStudent).first()

    hojasDeVida = HojasDeVida.objects.filter(id_estudiante=idStudent)

    if not hojasDeVida.exists():
        hojasDeVida= HojasDeVida.objects.create(id_hoja_vida=idStudent ,id_estudiante=estudiantes)

    return render(request, 'estudiantes/Inicio.html')

def logout_view(request):
    logout(request)  
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('home')  

@login_required(login_url=reverse_lazy('inicioS'))
def CursosPrincipal(request):
    filtros = request.GET.get('filtros')
    cursos = Cursos.objects.all()
    tipoContenido = TipoContenido.objects.all()
    tipoDificultad = TipoDificultad.objects.all()
    tipoDuracion = TipoDuracion.objects.all()
    tipoCertificado = TipoCertificado.objects.all()


    if filtros:
        lista_filtros = json.loads(filtros)
        print("Filtros recibidos:", lista_filtros)
        q_objects = Q()  # Creamos un objeto Q para filtrar varias condiciones.
        q_objects_nivel = Q()
        q_objects_tiempo = Q()
        q_objects_certificado = Q()

        for contenido in tipoContenido:
        # Agrego condiciones según los filtros seleccionados.
            if contenido.nombre_tipo in lista_filtros:
                q_objects |= Q(id_tipo_contenido_id=contenido.id_tipo_contenido)  # Utilizamos OR para multiples filtros.
        
        for dificultad in tipoDificultad:
            if dificultad.nombre_tipo in lista_filtros:
                q_objects_nivel |= Q(id_tipo_dificultad_id=dificultad.id_tipo_dificultad)

        for duracion in tipoDuracion:
            if duracion.nombre_tipo in lista_filtros:
                q_objects_tiempo |= Q(id_tipo_duracion_id=duracion.id_tipo_duracion)

        for certificado in tipoCertificado:
            if certificado.nombre_tipo in lista_filtros:
                q_objects_certificado |= Q(id_tipo_certificado_id=certificado.id_tipo_certificado)


        # Añadimos cada sub conjunto de condiciones
        if q_objects_nivel:
            q_objects &= q_objects_nivel
        if q_objects_tiempo:
            q_objects &= q_objects_tiempo
        if q_objects_certificado:
            q_objects &= q_objects_certificado

        # Aplicamos los filtros a la consulta.
        cursos = cursos.filter(q_objects)

    # Utilizo paginator para divitir 5 tablas por pagina.
    paginator = Paginator(cursos, 5) #Especifico que solo quiero 5 tablas en la pagina.
    num_pag = request.GET.get('page') #Obtengo el numero de pagina.
    cursos_data = paginator.get_page(num_pag) #Obtengo la pagina.

    filtros_java = json.dumps(lista_filtros) if filtros else ""

    Datos = {
        'cursos_data': cursos_data,
        'filtros': filtros_java,
        'tipoContenido': tipoContenido,
        'tipoDificultad': tipoDificultad,
        'tipoDuracion': tipoDuracion,
        'tipoCertificado': tipoCertificado,
    }

    return render(request, 'estudiantes/Cursos.html', Datos)

@login_required(login_url=reverse_lazy('inicioS'))
def CursosInfo(request):
    id_curso = request.GET.get('idCurso')
    idStudent = request.session.get('id_estudiante')

    if id_curso != None:
        cursos = Cursos.objects.filter(id_curso=id_curso)

        if cursos.exists():
            curso = cursos.first()
        else:
            curso = None

        contenidos = Contenidos.objects.filter(id_curso=curso.id_curso)

        # Al utilizar in estoy haciendo referencia a todas las tablas de contenidos
        if contenidos.exists():
            subcontenidos = SubContenidos.objects.filter(id_contenido__in=contenidos)
        else:
            contenidos = None
            subcontenidos = None
        
        cursosDisponibles = CursosDisponibles.objects.filter(id_curso=curso.id_curso, id_estudiante=idStudent)
        if cursosDisponibles.exists():
            cursoDisponible = cursosDisponibles[0]
        else:
            cursoDisponible = None

        cursosAprobados = CursosAprobados.objects.filter(id_curso=curso.id_curso, id_estudiante=idStudent)
        if cursosAprobados.exists():
            cursoAprobado = cursosAprobados[0]
        else:
            cursoAprobado = None

        estudiante = Estudiantes.objects.filter(id_estudiante = idStudent).first()
        fehaActual = date.today()

        Datos = {
            'curso': curso,
            'contenidos': contenidos,
            'subcontenidos': subcontenidos,
            'cursoDisponible': cursoDisponible,
            'cursoAprobado': cursoAprobado,
            'idStudent': idStudent,
            'estudiante': estudiante,
            'fehaActual': fehaActual,
        }
    else:
        Datos = {
            'curso': None,
        }

    return render(request, 'estudiantes/CursosInfo.html', Datos)

@login_required(login_url=reverse_lazy('inicioS'))
def CursosContent(request):
    id_curso = request.GET.get('idCurso')
    idSubCont = request.GET.get('idSubContent')
    subcontents = SubContenidos.objects.filter(id_subcont=idSubCont)

    if id_curso != None:

        if subcontents.exists():
            subcontent = subcontents[0]
        else:
            subcontent = None

        
        Datos = {
            'id_curso': id_curso,
            'subcontent': subcontent,
        }
    else:
        Datos = {
            'id_curso': None,
        }

    return render(request, 'estudiantes/CursosContent.html', Datos)

@login_required(login_url=reverse_lazy('inicioS'))
def Pruebas(request, idEstudiante, idCurso):
    estudiante = Estudiantes.objects.filter(id_estudiante = idEstudiante)[0]
    curso = Cursos.objects.filter(id_curso = idCurso)[0]

    cursosDisponibles = CursosDisponibles.objects.filter(id_estudiante=estudiante, id_curso=idCurso)

    if cursosDisponibles.exists():
        cursoActivo = 1
    else:
        cursoActivo = 0

    idStudent = request.session.get('id_estudiante')

    #Realizo la busqueda de las preguntas.
    preguntasCurso = PreguntasCurso.objects.filter(id_curso=idCurso)
    respuestasCurso = RespuestasCurso.objects.filter(id_pregunta__in=preguntasCurso)

    #Tablas para verificar si el curso está aprobado.
    cursosAprobados = CursosAprobados.objects.filter(id_curso=curso, id_estudiante=estudiante).first()


    Datos = {
        'cursoActivo': cursoActivo,
        'usuarioActual': idStudent,
        'usuarioURL': idEstudiante,
        'estudiante': estudiante,
        'curso': curso,
        'preguntasCurso': preguntasCurso,
        'respuestasCurso': respuestasCurso,
        'cursosAprobados': cursosAprobados,
    }

    return render(request, 'estudiantes/PruebasCursos.html', Datos)