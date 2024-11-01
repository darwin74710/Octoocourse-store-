from estudiantes.models import Estudiantes, HojasDeVida, Idiomas, Aptitudes, FormacionesAcademicas, LenguajesProg, ExpLaborales
from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#Con esto quitamos la seguridad de tokens por csrf
@csrf_exempt
def guardarContra(request):
    # Preguntamos si el metodo llamado es de tipo POST
    if request.method == 'POST':
        # Busco la tabla de estudiantes
        estudiantes = Estudiantes.objects.filter(id_estudiante=1)
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
        #OBTENEMOS TODAS LAS TABLAS QUE VAMOS A ACTUALIZAR
        hojasDeVida = HojasDeVida.objects.filter(id_estudiante=1)

        if hojasDeVida.exists():
            hojaDeVida = hojasDeVida[0]
        else:
            hojaDeVida = None
        
        idiomas = Idiomas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        aptitudes = Aptitudes.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        lenguajesProg = LenguajesProg.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        formaciones = FormacionesAcademicas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)
        expLaborales = ExpLaborales.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida)

        # Guardo los datos de los inputs en nuevas variables
        #--- DATOS PERSONALES ---
        telefonoDato = request.POST.get('telefono')
        direccionDato = request.POST.get('direccion').strip()

        #--- APTITUDES ---
        aptitud1 = request.POST.get('aptitud_1').strip()
        aptitud2 = request.POST.get('aptitud_2').strip()
        aptitud3 = request.POST.get('aptitud_3').strip()
        aptitud4 = request.POST.get('aptitud_4').strip()
        aptitud5 = request.POST.get('aptitud_5').strip()
        aptitudesArray = [aptitud1, aptitud2, aptitud3, aptitud4, aptitud5]

        #--- IDIOMAS ---
        idioma1 = request.POST.get('idioma_1').strip()
        idioma2 = request.POST.get('idioma_2').strip()
        idioma3 = request.POST.get('idioma_3').strip()
        nivel1 = request.POST.get('nivel_1').strip()
        nivel2 = request.POST.get('nivel_2').strip()
        nivel3 = request.POST.get('nivel_3').strip()
        idiomasArray = [idioma1, idioma2, idioma3]
        nivelArray = [nivel1, nivel2, nivel3]

        #--- LENGUAJES PROG ---
        lenguaje1 = request.POST.get('lenguajeProg_1').strip()
        lenguaje2 = request.POST.get('lenguajeProg_2').strip()
        lenguaje3 = request.POST.get('lenguajeProg_3').strip()
        lenguaje4 = request.POST.get('lenguajeProg_4').strip()
        lenguaje5 = request.POST.get('lenguajeProg_5').strip()
        lenguaje6 = request.POST.get('lenguajeProg_6').strip()
        lenguajeArray = [lenguaje1, lenguaje2, lenguaje3, lenguaje4, lenguaje5, lenguaje6]

        #--- EXP PROFESIONALES ---
        #exp 1
        cargo1 = request.POST.get('exp_cargo_1').strip()
        empresa1 = request.POST.get('exp_empresa_1').strip()
        tiempoIni1 = request.POST.get('exp_tiempoIni_1').strip()
        tiempoFin1 = request.POST.get('exp_tiempoFin_1').strip()
        description1 = request.POST.get('exp_description_1').strip()

        #exp 2
        cargo2 = request.POST.get('exp_cargo_2').strip()
        empresa2 = request.POST.get('exp_empresa_2').strip()
        tiempoIni2 = request.POST.get('exp_tiempoIni_2').strip()
        tiempoFin2 = request.POST.get('exp_tiempoFin_2').strip()
        description2 = request.POST.get('exp_description_2').strip()

        cargoArray = [cargo1, cargo2]
        empresaArray = [empresa1, empresa2]
        tiempoIniArray = [tiempoIni1, tiempoIni2]
        tiempoFinArray = [tiempoFin1, tiempoFin2]
        descriptionArray = [description1, description2]
        
        #--- FORMACIÓN ACADEMICA ---
        #form 1
        titulo1 = request.POST.get('academ_titulo_1').strip()
        instituto1 = request.POST.get('academ_institu_1').strip()
        fechaIni1 = request.POST.get('academ_fechaIni_1').strip()
        fechaFin1 = request.POST.get('academ_fechaFin_1').strip()

        #form 2
        titulo2 = request.POST.get('academ_titulo_2').strip()
        instituto2 = request.POST.get('academ_institu_2').strip()
        fechaIni2 = request.POST.get('academ_fechaIni_2').strip()
        fechaFin2 = request.POST.get('academ_fechaFin_2').strip()

        tituloArray = [titulo1, titulo2]
        institutoArray = [instituto1, instituto2]
        fechaIniArray = [fechaIni1, fechaIni2]
        fechaFinArray = [fechaFin1, fechaFin2]

        #VALIDACIONES
        

        try:
            # Actualizamos los datos
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
                expLaboral.tiempo_inicio = tiempoIniArray[i]
                expLaboral.tiempo_final = tiempoFinArray[i]
                expLaboral.cargo = cargoArray[i]
                expLaboral.descripcion = descriptionArray[i]
                i += 1
            
            i = 0
            for formacion in formaciones:
                formacion.titulo = tituloArray[i]
                formacion.nom_institucion = institutoArray[i]
                formacion.fecha_inicio = fechaIniArray[i]
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