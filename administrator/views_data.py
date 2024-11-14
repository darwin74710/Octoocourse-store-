from administrator.models_estudiantes import Estudiantes, HojasDeVida, Idiomas, Aptitudes, FormacionesAcademicas, LenguajesProg, ExpLaborales
from administrator.models_cursos import Cursos
from administrator.models_empresas import OfertasEmpleos, Empresas, TipoCont
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection, transaction

#Con esto quitamos la seguridad de tokens por csrf
@csrf_exempt
def guardarHVAdmin(request):
    # Preguntamos si el metodo llamado es de tipo POST
    if request.method == 'POST':
        id_Estudiante = request.POST.get('idEstudianteInput')
        

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
        
        i = 0
        for _ in range(expLaborales.count()):
            if tiempoIniArray[i] == "":
                tiempoIniArray[i] = None
            if tiempoFinArray[i] == "":
                tiempoFinArray[i] = None
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

        i = 0
        for _ in range(formaciones.count()):
            if fechaIniArray[i] == "":
                fechaIniArray[i] = None
            if fechaFinArray[i] == "":
                fechaFinArray[i] = None
            i = i + 1

        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE HOJAS_DE_VIDA SET TELEFONO = %s, DIRECCION = %s WHERE ID_HOJA_VIDA = %s",
                        [telefonoDato, direccionDato, hojaDeVida.id_hoja_vida]
                    )

                    i = 0
                    for aptitud in aptitudes:
                        cursor.execute(
                            "UPDATE APTITUDES SET NOMBRE_APT = %s WHERE ID_APTITUDES = %s",
                            [aptitudesArray[i], aptitud.id_aptitudes]
                        )
                        i = i + 1
                    
                    i = 0
                    for idioma in idiomas:
                        cursor.execute(
                            "UPDATE IDIOMAS SET IDIOMA = %s, NIVEL = %s WHERE ID_IDIOMA = %s",
                            [idiomasArray[i], nivelArray[i], idioma.id_idioma]
                        )
                        i = i + 1
                    
                    i = 0
                    for lenguaje in lenguajesProg:
                        cursor.execute(
                            "UPDATE LENGUAJES_PROG SET NOMBRE_LENG = %s WHERE ID_LENGUAJE = %s",
                            [lenguajeArray[i], lenguaje.id_lenguaje]
                        )
                        i = i + 1

                    i = 0
                    for expLaboral in expLaborales:
                        cursor.execute(
                            "UPDATE EXP_LABORALES SET NOM_EMPRESAS = %s, CARGO = %s, DESCRIPCION = %s, " +
                              "TIEMPO_INICIO = %s, TIEMPO_FINAL = %s WHERE ID_EXP = %s",
                            [empresaArray[i], cargoArray[i], descriptionArray[i], tiempoIniArray[i],
                             tiempoFinArray[i], expLaboral.id_exp]
                        )
                        i = i + 1

                    i = 0
                    for formacion in formaciones:
                        cursor.execute(
                            "UPDATE FORMACIONES_ACADEMICAS SET TITULO = %s, NOM_INSTITUCION = %s, " +
                              "FECHA_INICIO = %s, FECHA_FINAL = %s WHERE ID_FORMACION = %s",
                            [tituloArray[i], institutoArray[i], fechaIniArray[i], fechaFinArray[i],
                             formacion.id_formacion]
                        )
                        i = i + 1

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
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE ESTUDIANTES SET TIPO_ID = %s, CORREO_ESTUDIANTE = %s, NOM_ESTUDIANTE = %s, " +
                        "APELLIDO = %s, PASSWORD_ESTUDIANTE = %s, FECHA_NAC = %s WHERE ID_ESTUDIANTE = %s",
                        [tipo_id, correo, nombre, apellido, contraseña, fechaNac, idStudent]
                    )
            return JsonResponse({'status': 'success', 'message': 'El estudiante se modificó correctamente.'})
        except Exception as e:
            # Error por el cual no se pudo guardar
            return JsonResponse({'status': 'error', 'message': str(e)})
    # En caso de que no se este realizando un post
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})



@csrf_exempt
def guardarEmpresaAdmin(request, idEmpres):
    if request.method == 'POST':
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
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE EMPRESAS SET NOM_EMPRESA = %s, DIRECCION = %s, CORREO_EMP = %s, " +
                        "PASSWORD_EMP = %s, TELEFONO = %s WHERE NIT = %s",
                        [nombre, direccion, correo, contraseña, telefono, idEmpres]
                    )
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
        dificultad = request.POST.get('dificultad')
        lenguaje = request.POST.get('lenguaje')
        tiempo = request.POST.get('tiempo')
        certificado = request.POST.get('certificado')
        descripcion = request.POST.get('descripcion').strip()

        print(dificultad)
        print(lenguaje)
        print(tiempo)
        print(certificado)

        if lenguaje == 1:
            urlImage = "html.jpg"

        # Validaciones
        if nombre == "" or precio == "" or descripcion == "":
            # Enviamos una respuesta al JAVAX
            return JsonResponse({'status': 'error', 'message': 'No debe dejar ningún campo vacío.'})
        
        try:
            # Guardamos los datos
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE CURSOS SET NOM_CURSO = %s, PRECIO = %s, ID_TIPO_DIFICULTAD = %s, " +
                        "ID_TIPO_CONTENIDO = %s, ID_TIPO_DURACION = %s, ID_TIPO_CERTIFICADO = %s, " +
                        "DESCRIPCION = %s WHERE ID_CURSO = %s",
                        [nombre, precio, dificultad, lenguaje, tiempo, certificado, descripcion, idCurse]
                    )

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

        fechaPub = request.POST.get('fechaPub')
        nombre = request.POST.get('nombre').strip()
        salario = request.POST.get('salario')
        tipoCont = request.POST.get('tipoCont')
        estado = request.POST.get('estado')
        descripcion = request.POST.get('descripcion').strip()

        # Validaciones
        if nombre == "" or salario == "" or descripcion == "":
            # Enviamos una respuesta al JAVAX
            return JsonResponse({'status': 'error', 'message': 'No debe dejar ningún campo vacío.'})
        
        try:
            # Guardamos los datos
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE OFERTAS_EMPLEOS SET nombre_oferta = %s, salario = %s, estado = %s, " +
                        "descripcion = %s, id_tipo_cont = %s, fecha_pub = %s WHERE id_oferta = %s",
                        [nombre, salario, estado, descripcion, tipoCont, fechaPub, idOfert]
                    )
            return JsonResponse({'status': 'success', 'message': 'La oferta se modificó correctamente.'})
        except Exception as e:
            # Error por el cual no se pudo guardar
            return JsonResponse({'status': 'error', 'message': str(e)})
    # En caso de que no se este realizando un post
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})