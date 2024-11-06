from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from estudiantes.models_cursos import Cursos, Contenidos, SubContenidos, CursosDisponibles, CursosAprobados
from estudiantes.models import Estudiantes
from django.contrib import messages
from django.db.models import Q
import json
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required 
def Inicio(request):
    return render(request, 'estudiantes/Inicio.html')

def logout_view(request):
    logout(request)  
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('home')  

@login_required
def CursosPrincipal(request):
    filtros = request.GET.get('filtros')
    cursos = Cursos.objects.all()

    if filtros:
        lista_filtros = json.loads(filtros)
        print("Filtros recibidos:", lista_filtros)
        q_objects = Q()  # Creamos un objeto Q para filtrar varias condiciones.
        q_objects_nivel = Q()
        q_objects_tiempo = Q()
        q_objects_certificado = Q()


        # Agrego condiciones según los filtros seleccionados.
        if "HTML" in lista_filtros:
            q_objects |= Q(lenguaje="HTML")  # Utilizamos OR para multiples filtros.
        if "Básico" in lista_filtros:
            q_objects_nivel |= Q(dificultad="Básico")
        if "Medio" in lista_filtros:
            q_objects_nivel |= Q(dificultad="Medio")
        if "Avanzado" in lista_filtros:
            q_objects_nivel |= Q(dificultad="Avanzado")
        if "0-5 Horas" in lista_filtros:
            q_objects_tiempo |= Q(tiempo="0-5 Horas")
        if "6-10 Horas" in lista_filtros:
            q_objects_tiempo |= Q(tiempo="6-10 Horas")
        if "11-15 Horas" in lista_filtros:
            q_objects_tiempo |= Q(tiempo="11-15 Horas")
        if "15+ Horas" in lista_filtros:
            q_objects_tiempo |= Q(tiempo="15+ Horas")
        if "Con Certificado" in lista_filtros:
            q_objects_certificado |= Q(certificado=1)
        if "Sin Certificado" in lista_filtros:
            q_objects_certificado |= Q(certificado=0)

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
    }

    return render(request, 'estudiantes/Cursos.html', Datos)

@login_required
def CursosInfo(request):
    id_curso = request.GET.get('idCurso')
    idStudent = request.session.get('id_estudiante')

    cursos = Cursos.objects.filter(id_curso=id_curso)

    if cursos.exists():
        curso = cursos[0]
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
        if curso:
            estudiante = Estudiantes.objects.get(id_estudiante=idStudent)
            cursoDisponible = CursosDisponibles.objects.create(id_curso=curso, id_estudiante=estudiante, activacion = 0)
        else:
            cursoDisponible = None

    cursosAprobados = CursosAprobados.objects.filter(id_curso=curso.id_curso, id_estudiante=idStudent)
    if cursosAprobados.exists():
        cursoAprobado = cursosAprobados[0]
    else:
        cursoAprobado = None

    Datos = {
        'curso': curso,
        'contenidos': contenidos,
        'subcontenidos': subcontenidos,
        'cursoDisponible': cursoDisponible,
        'cursoAprobado': cursoAprobado,
    }

    return render(request, 'estudiantes/CursosInfo.html', Datos)

@login_required 
def CursosContent(request):
    id_curso = request.GET.get('idCurso')
    idSubCont = request.GET.get('idSubContent')
    subcontents = SubContenidos.objects.filter(id_subcont=idSubCont)

    if subcontents.exists():
        subcontent = subcontents[0]
    else:
        subcontent = None


    Datos = {
        'id_curso': id_curso,
        'subcontent': subcontent,
    }
    return render(request, 'estudiantes/CursosContent.html', Datos)