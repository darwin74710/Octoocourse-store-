import json
from estudiantes.models_Empresas import Conocimientos, OfertasEmpleos, TipoCont, OfertasDisponibles
from estudiantes.models import Estudiantes
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.conf import settings
import os
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect

@login_required(login_url=reverse_lazy('inicioS'))
def Ofertas(request):
    filtros = request.GET.get('filtros')
    ofertasEmpleos = OfertasEmpleos.objects.all()

    # Obtenemos los contratos
    contratos = TipoCont.objects.all()
    
    # Rangos de salarios según el dato recibido de filtros.
    salario_ranges = {
        "0_1": (0, 1000000),
        "1_2": (1000000, 2000000),
        "2_3": (2000000, 3000000),
        "3+": (3000000, None),
    }

    if filtros:
        lista_filtros = json.loads(filtros)
        q_objects = Q()  # Creamos un objeto Q para filtrar varias condiciones.

        for contrato in contratos:
        # Agrego condiciones según los filtros seleccionados.
            if contrato.nombre_tipo in lista_filtros:
                q_objects |= Q(id_tipo_cont_id=contrato.id_tipo_cont)  # Utilizamos OR para multiples filtros.
        
        # Filtramos los salarios.
        salario_q_objects = Q()

        for filtro in lista_filtros:
            if filtro in salario_ranges:
                min_sal, max_sal = salario_ranges[filtro]
                
                # Verificar si tiene limite.
                if max_sal is not None:
                    salario_q_objects |= Q(salario__gte=min_sal, salario__lte=max_sal)
                else:
                    # Si no tiene limite.
                    salario_q_objects |= Q(salario__gte=min_sal)

        # Añadir la condición de salarios al objeto q_objects principal.
        if salario_q_objects:
            q_objects &= salario_q_objects

        # Aplicamos los filtros a la consulta.
        ofertasEmpleos = ofertasEmpleos.filter(q_objects)


    # Utilizo paginator para divitir 5 tablas por pagina.
    paginator = Paginator(ofertasEmpleos, 5) #Especifico que solo quiero 5 tablas en la pagina.
    num_pag = request.GET.get('page') #Obtengo el numero de pagina.
    ofertas_data = paginator.get_page(num_pag) #Obtengo la pagina.

    for oferta in ofertas_data:
        oferta.conocimientos = Conocimientos.objects.filter(id_oferta=oferta.id_oferta)

    filtros_java = json.dumps(lista_filtros) if filtros else ""

    idStudent = request.session.get('id_estudiante')
    estudiantes = Estudiantes.objects.filter(id_estudiante = idStudent)[0]
    # Extraemos las ofertas de la pagina
    ofertasPag = ofertas_data.object_list

    # Obtenemos las tablas de ofertas disponibles
    ofertasDisponibles = OfertasDisponibles.objects.filter(id_estudiante=estudiantes, id_oferta__in=ofertasPag)

    if not ofertasDisponibles.exists():
        ofertasDisponibles = None

    
    for oferta in ofertasPag:
        ofertasDispoAux = OfertasDisponibles.objects.filter(id_oferta=oferta.id_oferta)
        oferta.contAplicados = ofertasDispoAux.count()

    Datos = {
        'ofertas_data': ofertas_data,
        'contratos': contratos,
        'filtros': filtros_java,
        'idEstudiante': idStudent,
        'ofertasDisponibles': ofertasDisponibles,
    }

    return render(request, 'estudiantes/Ofertas.html', Datos)

@login_required(login_url=reverse_lazy('inicioS'))
def OfertasInfo(request):
    idOferta = request.GET.get('idOferta')
    idEstudiante = request.GET.get('idEstudiante')

    ofertasEmpleos = OfertasEmpleos.objects.filter(id_oferta=idOferta)

    if ofertasEmpleos.exists():
        ofertasEmpleo = ofertasEmpleos.first()
    
    conocimientos = Conocimientos.objects.filter(id_oferta=idOferta)

    ofertasDisponibles = OfertasDisponibles.objects.filter(id_estudiante=idEstudiante, id_oferta=idOferta).first()

    ofertasDispoAux = OfertasDisponibles.objects.filter(id_oferta=ofertasEmpleo.id_oferta)
    ofertasEmpleo.contAplicados = ofertasDispoAux.count()
    
    Datos = {
        'ofertasEmpleos': ofertasEmpleo,
        'conocimientos': conocimientos,
        'idEstudiante': idEstudiante,
        'ofertasDisponibles': ofertasDisponibles,
    }

    return render(request, 'estudiantes/OfertasInfo.html', Datos)

@login_required(login_url=reverse_lazy('inicioS'))
def Pruebas(request, idEstudiante, idOferta):
    estudiante = Estudiantes.objects.filter(id_estudiante = idEstudiante)[0]
    ofertaEmpleo = OfertasEmpleos.objects.filter(id_oferta = idOferta)[0]

    ofertasDisponibles = OfertasDisponibles.objects.filter(id_estudiante=estudiante, id_oferta=ofertaEmpleo)

    if ofertasDisponibles.exists():
        ofertaActiva = 1
    else:
        ofertaActiva = 0

    idStudent = request.session.get('id_estudiante')

    # Ruta del archivo PDF EXAMEN OFERTA
    nombreArchivoExamen = 'OfertasExamenes/Examenes/' + str(ofertaEmpleo.nit.nit) + '/' + str(ofertaEmpleo.id_oferta) + '.pdf'
    urlPDFExamen = f"{settings.DATA_URL}{nombreArchivoExamen}"

    # Verificados si el pdf existe
    examenPDF = os.path.join(settings.DATA_ROOT, nombreArchivoExamen.strip('/'))
    if not os.path.exists(examenPDF):
        urlPDFExamen = None

    
    # Ruta del archivo PDF ESTUDIANTE
    nombreArchivoEstudiante = 'OfertasExamenes/Respuestas/' + str(ofertaEmpleo.nit.nit) + '/' + str(ofertaEmpleo.id_oferta) + '/' + str(estudiante.id_estudiante) + '.pdf'
    urlPDFRespuesta = f"{settings.DATA_URL}{nombreArchivoEstudiante}"

    # Verificados si el pdf existe
    respuestaPDF = os.path.join(settings.DATA_ROOT, nombreArchivoEstudiante.strip('/'))
    if not os.path.exists(respuestaPDF):
        urlPDFRespuesta = None
        
    Datos = {
        'ofertaActiva': ofertaActiva,
        'usuarioActual': idStudent,
        'usuarioURL': idEstudiante,
        'estudiante': estudiante,
        'ofertaEmpleo': ofertaEmpleo,
        'urlPDFExamen': urlPDFExamen,
        'urlPDFRespuesta': urlPDFRespuesta,
        'idOferta': idOferta,
    }

    return render(request, 'estudiantes/PruebasOfertas.html', Datos)

def GuardarRespuesta(request):
    if request.method == 'POST' and request.FILES.get('urlArchivo'):
        id_Estudiante = request.session.get('id_estudiante')
        idOferta = request.POST.get('idOfertaInput')
        urlArchivo = request.FILES.get('urlArchivo')

        oferta = OfertasEmpleos.objects.filter(id_oferta = idOferta).first()

        # Ruta del archivo PDF ESTUDIANTE
        nombreArchivoEstudiante = 'OfertasExamenes/Respuestas/' + str(oferta.nit.nit) + '/' + str(idOferta) + '/' + str(id_Estudiante) + '.pdf'

        # Verificados si el pdf existe y eliminarlo
        respuestaPDF = os.path.join(settings.DATA_ROOT, nombreArchivoEstudiante.strip('/'))
        if os.path.exists(respuestaPDF):
            os.remove(respuestaPDF)

        # Ruta para guardar el arhivo
        rutaCrearArchivo = os.path.join(settings.DATA_ROOT, f'OfertasExamenes/Respuestas/' + str(oferta.nit.nit) + '/' + str(idOferta) + '/')
        if not os.path.exists(rutaCrearArchivo):
            os.makedirs(rutaCrearArchivo)

        try:
            archivoGuardado = os.path.join(rutaCrearArchivo, f'{id_Estudiante}.pdf')

            with open(archivoGuardado, 'wb') as archivo_destino:
                for chunk in urlArchivo.chunks():
                    archivo_destino.write(chunk)

            messages.success(request, "El archivo se subió correctamente.")
            return redirect('PruebasOfertas', idEstudiante=id_Estudiante, idOferta=idOferta)
        except Exception as e:
            messages.error(request, str(e))
            return redirect('PruebasOfertas', idEstudiante=id_Estudiante, idOferta=idOferta)

    messages.error(request, "No se subió ningún archivo.")
    return redirect('PruebasOfertas', idEstudiante=id_Estudiante, idOferta=idOferta)