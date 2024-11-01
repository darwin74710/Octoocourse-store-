from django.shortcuts import render, redirect
from estudiantes.models import Estudiantes, HojasDeVida, Idiomas, Aptitudes, FormacionesAcademicas, LenguajesProg, ExpLaborales
from estudiantes.models_Empresas import Conocimientos, OfertasEmpleos, TipoCont
from django.core.paginator import Paginator
import os
from django.conf import settings
from urllib.parse import unquote
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



@login_required 
def Inicio(request):
    return render(request, 'estudiantes/Inicio.html')



def logout_view(request):
    logout(request)  
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('home')  



def Ofertas(request):
    ofertasEmpleos = OfertasEmpleos.objects.all()
    
    # Utilizo paginator para divitir 5 tablas por pagina.
    paginator = Paginator(ofertasEmpleos, 5) #Especifico que solo quiero 5 tablas en la pagina.
    num_pag = request.GET.get('page') #Obtengo el numero de pagina.
    ofertas_data = paginator.get_page(num_pag) #Obtengo la pagina.

    for oferta in ofertas_data:
        oferta.conocimientos = Conocimientos.objects.filter(id_oferta=oferta.id_oferta)
        oferta.tipoCont = TipoCont.objects.filter(id_oferta=oferta.id_oferta).first()

    Datos = {
        'ofertas_data': ofertas_data,
    }

    return render(request, 'estudiantes/Ofertas.html', Datos)

def OfertasInfo(request):
    idOferta = request.GET.get('idOferta')

    ofertasEmpleos = OfertasEmpleos.objects.filter(id_oferta=idOferta)

    if ofertasEmpleos.exists():
        ofertasEmpleo = ofertasEmpleos[0]
    
    conocimientos = Conocimientos.objects.filter(id_oferta=idOferta)
    tipoCont = TipoCont.objects.filter(id_oferta=idOferta)

    if tipoCont.exists():
        contrato = tipoCont[0]
    else:
        contrato = None

    Datos = {
        'ofertasEmpleos': ofertasEmpleo,
        'conocimientos': conocimientos,
        'contrato': contrato,
    }

    return render(request, 'estudiantes/OfertasInfo.html', Datos)



# Aplico metodo similar al del segundo semestre para leer archivos planos.
def cargar_cursos():
    cursos = []
    # Busco la ruta del archivo
    ruta_archivo = os.path.join(settings.BASE_DIR, 'estudiantes/cursosData/cursos.txt')
    
    #Recorro cada linea para ir guardandola en el array de cursos
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            # Elimino el salto de lineas y divido cada elemento del array por un "|"
            datos = linea.strip().split('|')
            cursos.append(datos)
    
    return cursos

def Cursos(request):
    cursos = cargar_cursos()

    paginator = Paginator(cursos, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'estudiantes/Cursos.html', {'page_obj': page_obj})

def CursosInfo(request):
    idCurso = request.GET.get('idCurso')
    cursos = cargar_cursos()

    # Busco el curso dentro del array con el mismo id que guarde en la pagina dinamica.
    cursoCorrespondiente = None
    for curso in cursos:
        if curso[0] == idCurso:
            cursoCorrespondiente = curso

    cursos_content = contenidoCursos(idCurso)

    DataCurso = {
        'curso': cursoCorrespondiente,
        'contentCursos' : cursos_content,
    }


    return render(request, 'estudiantes/CursosInfo.html', DataCurso)

def CursosContent(request):
    urlPower = request.GET.get('urlPower')
    idCurso = request.GET.get('idCurso')

    # Descodifico la url
    if urlPower:
        urlPower = unquote(urlPower)

    # Envio la url y el idCurso
    return render(request, 'estudiantes/CursosContent.html', {'urlPower': urlPower, 'idCurso': idCurso})



def contenidoCursos(idCurso):
    # Ruta de las carpetas en donde tengo guardado los temas de los cursos
    rutaCarpetaId = os.path.join(settings.BASE_DIR, 'estudiantes/cursosData/ContenidoCursos/' + idCurso)

    # Verificamos que si sea una carpeta
    if os.path.isdir(rutaCarpetaId):
        # Aquí voy a guardar el nombre de cada archivo de texto junto a su contenido
        archivosContent = []

        # Recorremos los archivos dentro de cada carpeta
        for archivo in os.listdir(rutaCarpetaId):
            # Comprobamos que sean archivos de texto.
            if archivo.endswith('.txt'):
                # Elimino el .txt para guardar solo los nombres.
                nombreNormal = os.path.splitext(archivo)[0]
                
                # Leo el contenido de los enlaces.
                rutaArchivoContent = os.path.join(rutaCarpetaId, archivo)
                textoContentTema = []

                # Es el mismo metodo del segundo semestre para los archivos planos pero en js
                with open(rutaArchivoContent, 'r', encoding='utf-8') as f:
                    lineas = f.readlines()
                    for linea in lineas:
                        tema, enlace = linea.strip().split('|')
                        textoContentTema.append({'tema': tema, 'enlace': enlace})

                # Agregamos el nombre de los archivos de texto y el contenido dentro de ellos al array.
                archivosContent.append({'nombre': nombreNormal, 'temas': textoContentTema})

        #Se viene tremendo voleo de arrays.

    return archivosContent

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
