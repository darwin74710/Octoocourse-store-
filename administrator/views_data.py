from estudiantes.models import Estudiantes, HojasDeVida, Idiomas, Aptitudes, FormacionesAcademicas, LenguajesProg, ExpLaborales
from estudiantes.models_cursos import Cursos
from estudiantes.models_Empresas import OfertasEmpleos, Empresas, TipoCont
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#Con esto quitamos la seguridad de tokens por csrf
@csrf_exempt
def guardarHVAdmin(request):
    
    # Preguntamos si el metodo llamado es de tipo POST
    if request.method == 'POST':
        id_Estudiante = request.session.get('id_estudiante')

        #OBTENEMOS TODAS LAS TABLAS QUE VAMOS A ACTUALIZAR
        hojasDeVida = HojasDeVida.objects.filter(id_estudiante=id_Estudiante)

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


# Esta función es para guardar los estudiantes
@csrf_exempt
def guardarEstudianteAdmin(request, idStudent):
    if request.method == 'POST':
        estudiante = Estudiantes.objects.filter(id_estudiante=idStudent).first()

        tipo_id = request.POST.get('tipo_id').strip()
        correo = request.POST.get('correo').strip()
        nombre = request.POST.get('nombre').strip()
        apellido = request.POST.get('apellido').strip()
        contraseña = request.POST.get('contraseña').strip()
        fechaNac = request.POST.get('fechaNac')

        # Validaciones
        if contraseña == "" or correo == "" or tipo_id == "" or nombre == "" or apellido == "":
            # Enviamos una respuesta al JAVAX
            return JsonResponse({'status': 'error', 'message': 'No debe dejar ningún campo vacío.'})

        try:
            # Guardamos los datos
            estudiante.tipo_id = tipo_id
            estudiante.correo_estudiante = correo
            estudiante.nom_estudiante = nombre
            estudiante.apellido = apellido
            estudiante.password_estudiante = make_password(contraseña)
            estudiante.fecha_nac = fechaNac
            estudiante.save()
            return JsonResponse({'status': 'success', 'message': 'El estudiante se modificó correctamente.'})
        except Exception as e:
            # Error por el cual no se pudo guardar
            return JsonResponse({'status': 'error', 'message': str(e)})
    # En caso de que no se este realizando un post
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})



@csrf_exempt
def guardarEmpresaAdmin(request, idEmpres):
    if request.method == 'POST':
        empresa = Empresas.objects.filter(nit=idEmpres).first()

        nombre = request.POST.get('nombre').strip()
        direccion = request.POST.get('dirección').strip()
        correo = request.POST.get('correo').strip()
        telefono = request.POST.get('telefono')
        contraseña = request.POST.get('contraseña').strip()

        # Validaciones
        if nombre == "" or direccion == "" or correo == "" or telefono == "" or contraseña == "":
            # Enviamos una respuesta al JAVAX
            return JsonResponse({'status': 'error', 'message': 'No debe dejar ningún campo vacío.'})
        
        try:
            # Guardamos los datos
            empresa.nom_empresa = nombre
            empresa.direccion = direccion
            empresa.correo_emp = correo
            empresa.telefono = telefono
            empresa.password_emp = make_password(contraseña)
            empresa.save()
            return JsonResponse({'status': 'success', 'message': 'La empresa se modificó correctamente.'})
        except Exception as e:
            # Error por el cual no se pudo guardar
            return JsonResponse({'status': 'error', 'message': str(e)})
    # En caso de que no se este realizando un post
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})

@csrf_exempt
def guardarCursoAdmin(request, idCurse):
    if request.method == 'POST':
        curso = Cursos.objects.filter(id_curso=idCurse).first()

        nombre = request.POST.get('nombre').strip()
        precio = request.POST.get('precio')
        dificultad = request.POST.get('dificultad').strip()
        lenguaje = request.POST.get('lenguaje').strip()
        tiempo = request.POST.get('tiempo').strip()
        certificado = request.POST.get('certificado')
        descripcion = request.POST.get('descripcion').strip()

        if lenguaje == "HTML":
            urlImage = "html.jpg"

        # Validaciones
        if nombre == "" or precio == "" or descripcion == "":
            # Enviamos una respuesta al JAVAX
            return JsonResponse({'status': 'error', 'message': 'No debe dejar ningún campo vacío.'})
        
        try:
            # Guardamos los datos
            curso.nom_curso = nombre
            curso.precio = precio
            curso.dificultad = dificultad
            curso.lenguaje = lenguaje
            curso.tiempo = tiempo
            curso.certificado = certificado
            curso.descripcion = descripcion
            curso.url_imagen = urlImage
            curso.save()
            return JsonResponse({'status': 'success', 'message': 'El curso se modificó correctamente.'})
        except Exception as e:
            # Error por el cual no se pudo guardar
            return JsonResponse({'status': 'error', 'message': str(e)})
    # En caso de que no se este realizando un post
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})


@csrf_exempt
def guardarOfertaAdmin(request, idOfert):
    if request.method == 'POST':
        oferta = OfertasEmpleos.objects.filter(id_oferta=idOfert).first()
        oferta = OfertasEmpleos.objects.filter(id_oferta=idOfert).first()

        nombre = request.POST.get('nombre').strip()
        salario = request.POST.get('salario')
        estado = request.POST.get('estado')
        descripcion = request.POST.get('descripcion').strip()

        # Validaciones
        if nombre == "" or salario == "" or descripcion == "":
            # Enviamos una respuesta al JAVAX
            return JsonResponse({'status': 'error', 'message': 'No debe dejar ningún campo vacío.'})
        
        try:
            # Guardamos los datos
            oferta.nombre_oferta = nombre
            oferta.salario = salario
            oferta.estado = estado
            oferta.descripcion = descripcion
            oferta.save()
            return JsonResponse({'status': 'success', 'message': 'La oferta se modificó correctamente.'})
        except Exception as e:
            # Error por el cual no se pudo guardar
            return JsonResponse({'status': 'error', 'message': str(e)})
    # En caso de que no se este realizando un post
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})