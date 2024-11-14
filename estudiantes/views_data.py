from estudiantes.models import Estudiantes, HojasDeVida, Idiomas, Aptitudes, FormacionesAcademicas, LenguajesProg, ExpLaborales
from estudiantes.models_cursos import CursosDisponibles
from estudiantes.models_Empresas import OfertasDisponibles, OfertasEmpleos
from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

#Con esto quitamos la seguridad de tokens por csrf
@csrf_exempt
def guardarContra(request):
    # Preguntamos si el metodo llamado es de tipo POST
    if request.method == 'POST':
        id_Estudiante = request.session.get('id_estudiante')
        # Busco la tabla de estudiantes
        estudiantes = Estudiantes.objects.filter(id_estudiante=id_Estudiante)
        if estudiantes.exists():
            estudiante = estudiantes[0]
        else:
            return JsonResponse({'status': 'error', 'message': 'Estudiante no encontrado.'})

        # Guardo los datos de los inputs en nuevas variables
        viejaContra = request.POST.get('old_contra').strip()
        nuevaContra1 = request.POST.get('nuv_contra1').strip()
        nuevaContra2 = request.POST.get('nuv_contra2').strip()

        #VALIDACIONES
        # En caso de que las contraseñas no tengan nada
        if viejaContra == "" or nuevaContra1 == "" or nuevaContra2 == "":
            # Enviamos una respuesta al JAVAX
            return JsonResponse({'status': 'error', 'message': 'No debe dejar ningún campo vacío.'})

        # Comparamos las dos contraseñas incluso si la de la base de datos se encuentra encriptada en caso de que no sean iguales
        if not check_password(viejaContra, estudiante.password_estudiante):
            return JsonResponse({'status': 'error', 'message': 'La contraseña actual es incorrecta.'})

        # Comparamos las dos contraseñas por si son iguales
        if nuevaContra1 != nuevaContra2:
            return JsonResponse({'status': 'error', 'message': 'Las contraseñas no coinciden.'})
        
        # Comparamos que no repita la misma contraseña que ya tiene
        if check_password(nuevaContra1, estudiante.password_estudiante):
            return JsonResponse({'status': 'error', 'message': 'La nueva contraseña debe ser diferente.'})

        try:
            # Guardamos la nueva contraseña de forma encriptada
            estudiante.password_estudiante = make_password(nuevaContra1)
            estudiante.save()
            return JsonResponse({'status': 'success', 'message': 'Su contraseña se a actualizado correctamente.'})
        except Exception as e:
            # Error por el cual no se pudo guardar
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    # En caso de que no se este realizando un post
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})


#Con esto quitamos la seguridad de tokens por csrf
@csrf_exempt
def guardarHV(request):
    
    # Preguntamos si el metodo llamado es de tipo POST
    if request.method == 'POST':
        id_Estudiante = request.session.get('id_estudiante')

        #OBTENEMOS TODAS LAS TABLAS QUE VAMOS A ACTUALIZAR
        hojasDeVida = HojasDeVida.objects.filter(id_estudiante=id_Estudiante)

        if hojasDeVida.exists():
            hojaDeVida = hojasDeVida[0]
        else:
            hojaDeVida = None
        
        aptitudes = Aptitudes.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        idiomas = Idiomas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        lenguajesProg = LenguajesProg.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        expLaborales = ExpLaborales.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        formaciones = FormacionesAcademicas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)

        # Guardo los datos de los inputs en nuevas variables
        #--- DATOS PERSONALES ---
        telefonoDato = request.POST.get('telefono')
        direccionDato = request.POST.get('direccion').strip()

        #--- APTITUDES ---
        aptitudesArray = []
        i = 1
        for _ in range(aptitudes.count()):
            aptitud = request.POST.get('aptitud_' + str(i)).strip()
            aptitudesArray.append(aptitud)
            i = i + 1

        #--- IDIOMAS ---
        idiomasArray = []
        nivelArray = []
        i = 1
        for _ in range(idiomas.count()):
            idioma = request.POST.get('idioma_' + str(i)).strip()
            nivel = request.POST.get('nivel_' + str(i)).strip()
            idiomasArray.append(idioma)
            nivelArray.append(nivel)
            i = i + 1

        #--- LENGUAJES PROG ---
        lenguajeArray = []
        i = 1
        for _ in range(lenguajesProg.count()):
            lenguaje = request.POST.get('lenguajeProg_' + str(i)).strip()
            lenguajeArray.append(lenguaje)
            i = i + 1

        #--- EXP PROFESIONALES ---
        cargoArray = []
        empresaArray = []
        tiempoIniArray = []
        tiempoFinArray = []
        descriptionArray = []

        i = 1
        for _ in range(expLaborales.count()):
            cargo = request.POST.get('exp_cargo_' + str(i)).strip()
            empresa = request.POST.get('exp_empresa_' + str(i)).strip()
            tiempoIni = request.POST.get('exp_tiempoIni_' + str(i)).strip()
            tiempoFin = request.POST.get('exp_tiempoFin_' + str(i)).strip()
            description = request.POST.get('exp_description_' + str(i)).strip()

            cargoArray.append(cargo)
            empresaArray.append(empresa)
            tiempoIniArray.append(tiempoIni)
            tiempoFinArray.append(tiempoFin)
            descriptionArray.append(description)
            i = i + 1
        
        #--- FORMACIÓN ACADEMICA ---
        tituloArray = []
        institutoArray = []
        fechaIniArray = []
        fechaFinArray = []
        i = 1

        for _ in range(formaciones.count()):
            titulo = request.POST.get('academ_titulo_' + str(i)).strip()
            instituto = request.POST.get('academ_institu_' + str(i)).strip()
            fechaIni = request.POST.get('academ_fechaIni_' + str(i)).strip()
            fechaFin = request.POST.get('academ_fechaFin_' + str(i)).strip()

            tituloArray.append(titulo)
            institutoArray.append(instituto)
            fechaIniArray.append(fechaIni)
            fechaFinArray.append(fechaFin)
            i = i + 1

        try:
            # Actualizamos los datos
            if not telefonoDato == "":
                hojaDeVida.telefono = telefonoDato
            hojaDeVida.direccion = direccionDato

            i = 0
            for aptitud in aptitudes:
                aptitud.nombre_apt = aptitudesArray[i]
                i += 1
            
            i = 0
            for idioma in idiomas:
                idioma.idioma = idiomasArray[i]
                idioma.nivel = nivelArray[i]
                i += 1
            
            i = 0
            for lenguaje in lenguajesProg:
                lenguaje.nombre_leng = lenguajeArray[i]
                i += 1
            
            i = 0
            for expLaboral in expLaborales:
                expLaboral.nom_empresas = empresaArray[i]
                expLaboral.cargo = cargoArray[i]
                expLaboral.descripcion = descriptionArray[i]

                if not tiempoIniArray[i] == "":
                    expLaboral.tiempo_inicio = tiempoIniArray[i]
                if not tiempoFinArray[i] == "":
                    expLaboral.tiempo_final = tiempoFinArray[i]
                i += 1
            
            i = 0
            for formacion in formaciones:
                formacion.titulo = tituloArray[i]
                formacion.nom_institucion = institutoArray[i]

                if not fechaIniArray[i] == "":
                    formacion.fecha_inicio = fechaIniArray[i]
                if not fechaFinArray[i] == "":
                    formacion.fecha_final = fechaFinArray[i]
                i += 1

            # Guardamos los datos
            hojaDeVida.save()
            for idioma in idiomas:
                idioma.save()
            for aptitud in aptitudes:
                aptitud.save()
            for lenguaje in lenguajesProg:
                lenguaje.save()
            for formacion in formaciones:
                formacion.save()
            for expLaboral in expLaborales:
                expLaboral.save()

            return JsonResponse({'status': 'success', 'message': 'Su hoja de vida se actualizo correctamente.'})
        except Exception as e:
            # Error por el cual no se pudo guardar
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    # En caso de que no se este realizando un post
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})


# Esta función es para aplicar a los cursos
@csrf_exempt
def aplicarCurso(request):
    if request.method == 'POST':
        # Busco la tabla de cursosDisponibles
        idCurso = request.POST.get('idCurso')
        idEstudiante = request.POST.get('idEstudiante')

        cursosDisponibles = CursosDisponibles.objects.filter(id_estudiante=idEstudiante, id_curso=idCurso)
        if cursosDisponibles.exists():
            cursoDisponible = cursosDisponibles[0]
        else:
            return JsonResponse({'status': 'error', 'message': 'Curso no encontrado.'})
        try:
            # Guardamos la activación
            cursoDisponible.activacion = 1
            cursoDisponible.save()
            return JsonResponse({'status': 'success', 'message': 'Aplicaste al curso correctamente.'})
        except Exception as e:
            # Error por el cual no se pudo guardar
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    # En caso de que no se este realizando un post
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})

# Esta función es para aplicar a las ofertas
@csrf_exempt
def aplicarOferta(request):
    if request.method == 'POST':
        # Busco la tabla de ofertasDisponibles
        idOferta = request.POST.get('idOferta')
        idEstudiante = request.POST.get('idEstudiante')

        ofertasDisponibles = OfertasDisponibles.objects.filter(id_estudiante=idEstudiante, id_oferta=idOferta)
        if ofertasDisponibles.exists():
            ofertaDisponible = ofertasDisponibles.first()
        else:
            estudiantes = Estudiantes.objects.filter(id_estudiante = idEstudiante).first()
            ofertasEmpleos = OfertasEmpleos.objects.filter(id_oferta = idOferta).first()
            try:
                ofertaDisponible = OfertasDisponibles.objects.create(id_estudiante=estudiantes, id_oferta=ofertasEmpleos, activacion = 1)
                return JsonResponse({'status': 'success', 'message': 'Aplicaste a la oferta correctamente.'})
            except Exception as e:
                # Error por el cual no se pudo crear
                return JsonResponse({'status': 'error', 'message': str(e)})
            
        if ofertaDisponible.activacion == 1:
            # Lo dirijimos a pruebas en caso de que ya este aplicado a la oferta junto al id del estudiante y de la oferta.
            url_pruebas = reverse('Pruebas', kwargs={'idEstudiante': idEstudiante, 'idOferta': idOferta})
            return JsonResponse({'status': 'redirect', 'url': url_pruebas})
    
    # En caso de que no se este realizando un post
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})