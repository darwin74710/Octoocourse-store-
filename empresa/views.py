from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from login.models import Conocimiento, TipoCont, OfertaEmpleo, Empresa, Estudiante, OfertaDisponible
from estudiantes.models import Estudiantes, HojasDeVida, Idiomas, Aptitudes, LenguajesProg, FormacionesAcademicas, ExpLaborales
from datetime import date
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, make_password




@login_required
def crearOferta(request):
    if request.method == 'POST':
        nombre_oferta = request.POST.get('nombre_oferta')
        salario = request.POST.get('salario')
        descripcion = request.POST.get('descripcion')
        conocimientos_text = request.POST.get('conocimientos')
        tipo_cont_id = request.POST.get('tipo_cont')  

        estado = 1 if request.POST.get('estado') == 'on' else 0
        nit_empresa = request.session.get('nit')
        fecha_pub = date.today()

        with connection.cursor() as cursor:
            cursor.execute("SELECT oferta_id_seq.NEXTVAL FROM dual")
            id_oferta = cursor.fetchone()[0]

        oferta = OfertaEmpleo(
            id_oferta=id_oferta,
            nit=nit_empresa,
            nombre_oferta=nombre_oferta,
            salario=salario,
            descripcion=descripcion,
            estado=estado,
            fecha_pub=fecha_pub,
            id_tipo_cont_id=tipo_cont_id  
        )
        oferta.save()

        conocimientos_list = conocimientos_text.split(',')
        for conocimiento_nombre in conocimientos_list:
            if conocimiento_nombre.strip():
                Conocimiento.objects.create(
                    id_oferta=oferta,
                    nom_con=conocimiento_nombre.strip()
                )

        return render(request, 'empresa/publicaro.html')

    return render(request, 'empresa/publicaro.html')




@login_required 
def inicioE(request):
    return render(request, 'empresa/inicioE.html')

@login_required 
def logout_view(request):
    logout(request)  
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('home')  

@login_required
def detalle_estudiante(request, id_estudiante):
    estudiante = get_object_or_404(Estudiantes, id_estudiante=id_estudiante)  
    Tablas = obtenerTablasHV(id_estudiante)  
    
    nit_empresa = request.session.get('nit')
    
    context = {
        'estudiante': estudiante,
        'nit_empresa': nit_empresa  
    }
    context.update(Tablas)  
    
    return render(request, 'empresa/aboutMeStudent.html', context)

def obtenerTablasHV(id_estudiante):
    estudiantes = Estudiantes.objects.filter(id_estudiante=id_estudiante)

    if estudiantes.exists():
        estudiante = estudiantes[0]
    else:
        estudiante = None

    if estudiante:
        hojasDeVida = HojasDeVida.objects.filter(id_estudiante=estudiante.id_estudiante)

        if hojasDeVida.exists():
            hojaDeVida = hojasDeVida[0]
        else:
            hojaDeVida = None

        idiomas = Idiomas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida) if hojaDeVida else []
        aptitudes = Aptitudes.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida) if hojaDeVida else []
        lenguajesProg = LenguajesProg.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida) if hojaDeVida else []
        formaciones = FormacionesAcademicas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida) if hojaDeVida else []
        expLaborales = ExpLaborales.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida) if hojaDeVida else []
    else:
        idiomas = aptitudes = lenguajesProg = formaciones = expLaborales = []

    Datos = {
        'estudiante': estudiante,
        'hojasDeVida': hojaDeVida,
        'idiomas': idiomas,
        'aptitudes': aptitudes,
        'lenguajesProg': lenguajesProg,
        'formaciones': formaciones,
        'expLaborales': expLaborales,
    }

    return Datos


@login_required 
def estudiantesE(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT ID_ESTUDIANTE, TIPO_ID, NOM_ESTUDIANTE, APELLIDO, CORREO_ESTUDIANTE, FECHA_NAC FROM ESTUDIANTES")
        estudiantes = [
            {
                'id': row[0],
                'tipo_id': row[1],
                'nombre': row[2],
                'apellido': row[3],
                'correo': row[4],
                'fecha_nac': row[5]
            }
            for row in cursor.fetchall()
        ]
    return render(request, 'empresa/estudiantesE.html', {'estudiantes': estudiantes})


@login_required
def configE(request):
    nit_empresa = request.session.get('nit')
    empresa_data = None
    conteo_ofertas_creadas = 0  
    conteo_ofertas_activas = 0
    conteo_ofertas_inactivas = 0

    if nit_empresa:
        empresa_data = Empresa.objects.filter(nit=nit_empresa).values(
            'nom_empresa', 'correo_emp', 'nit', 'direccion', 'telefono'
        ).first()

        conteo_ofertas_creadas = OfertaEmpleo.objects.filter(nit=nit_empresa).count()
        conteo_ofertas_activas = OfertaEmpleo.objects.filter(nit=nit_empresa, estado=1).count()
        conteo_ofertas_inactivas = OfertaEmpleo.objects.filter(nit=nit_empresa, estado=0).count()


    data = {
        'empresa': empresa_data,
        'conteo_ofertas_creadas': conteo_ofertas_creadas,
        'conteo_ofertas_activas': conteo_ofertas_activas,
        'conteo_ofertas_inactivas': conteo_ofertas_inactivas
    }

    return render(request, 'empresa/configE.html', data)


@login_required
def ofertasE(request):
    nit_empresa = request.session.get('nit')
    
    ofertas = OfertaEmpleo.objects.filter(nit=nit_empresa)
    
    for oferta in ofertas:
        conteo_aplicantes = OfertaDisponible.objects.filter(id_oferta=oferta.id_oferta).count()
        oferta.conteo_aplicantes = conteo_aplicantes  
    
    return render(request, 'empresa/ofertasE.html', {'ofertas': ofertas})


@login_required
def detalle_oferta(request, id_oferta):
    oferta = get_object_or_404(OfertaEmpleo, id_oferta=id_oferta)
    
    datos_adicionales = obtener_tablas_tc(id_oferta)

    nit_empresa = request.session.get('nit')

    request.session['current_id_oferta'] = id_oferta
    id_oferta = request.session.get('current_id_oferta')

    oferta_actual = OfertaEmpleo.objects.filter(nit=nit_empresa, id_oferta=id_oferta).first()

    estudiantes_aplicados = OfertaDisponible.objects.filter(id_oferta=id_oferta).values_list('id_estudiante', flat=True)
    
    estudiantes = Estudiante.objects.filter(id_estudiante__in=estudiantes_aplicados).values('nom_estudiante', 'apellido', 'id_estudiante')


    context = {
        'oferta': oferta,
        'oferta_actual': oferta_actual,
        'estudiantes': estudiantes, 
        'tipo_contrato': datos_adicionales.get('tipo_contrato'),
        'conocimientos': datos_adicionales.get('conocimientos'),
    }
    

    return render(request, 'empresa/DetallesOferta.html', context)

@login_required
def eliminar_oferta(request, id_oferta):
    oferta = get_object_or_404(OfertaEmpleo, id_oferta=id_oferta)
    
    OfertaDisponible.objects.filter(id_oferta=id_oferta).delete()
    
    oferta.delete()
    messages.success(request, "Oferta eliminada con éxito.")

    return redirect('ofertasE')

@login_required
def editar_oferta(request, id_oferta):
    oferta = get_object_or_404(OfertaEmpleo, id_oferta=id_oferta)

    if request.method == 'POST':
        oferta.nombre_oferta = request.POST.get('nombre_oferta', oferta.nombre_oferta)
        oferta.salario = request.POST.get('salario', oferta.salario)
        oferta.descripcion = request.POST.get('descripcion', oferta.descripcion)

        tipo_contrato = request.POST.get('tipo_contrato')
        if tipo_contrato:
            tipo_cont, created = TipoCont.objects.update_or_create(
                id_oferta=oferta,
                defaults={'tipo_cont': tipo_contrato}
            )

        conocimientos_existentes = list(Conocimiento.objects.filter(id_oferta=oferta).values_list('nom_con', flat=True))

        nuevos_conocimientos = request.POST.getlist('conocimientos')  

        for nom_con in nuevos_conocimientos:
            if nom_con and nom_con not in conocimientos_existentes: 
                Conocimiento.objects.create(id_oferta=oferta, nom_con=nom_con)

        oferta.estado = '1' if 'estado' in request.POST else '0'
        oferta.save()
        messages.success(request, "Oferta actualizada con éxito.")
        return redirect('ofertasE')  

    conocimientos_existentes = Conocimiento.objects.filter(id_oferta=oferta).values_list('nom_con', flat=True)
    tipo_contrato_existente = TipoCont.objects.filter(id_oferta=oferta).first()

    return render(request, 'empresa/editar_oferta.html', {
        'oferta': oferta,
        'conocimientos_existentes': conocimientos_existentes,
        'tipo_contrato_existente': tipo_contrato_existente,
    })



def obtener_tablas_tc(id_oferta):
    oferta = get_object_or_404(OfertaEmpleo, id_oferta=id_oferta)

    tipo_cont = oferta.id_tipo_cont.nombre_tipo if oferta.id_tipo_cont else None
    conocimientos = Conocimiento.objects.filter(id_oferta=oferta).values_list('nom_con', flat=True)

    datos = {
        'tipo_contrato': tipo_cont,
        'conocimientos': list(conocimientos),
    }

    return datos


def des_ofertas(request):
    return render(request, 'empresa/des_ofertas.html')

@login_required
def listEAp(request):
    nit_empresa = request.session.get('nit')
    id_oferta = request.session.get('current_id_oferta')  
    
    oferta_actual = OfertaEmpleo.objects.filter(nit=nit_empresa, id_oferta=id_oferta).first()

    estudiantes_aplicados = OfertaDisponible.objects.filter(id_oferta=id_oferta).values_list('id_estudiante', flat=True)
    
    estudiantes = Estudiante.objects.filter(id_estudiante__in=estudiantes_aplicados).values('nom_estudiante', 'apellido', 'id_estudiante')
    ofertas = OfertaEmpleo.objects.filter(nit=nit_empresa, id_oferta=id_oferta).values('nombre_oferta').first()

    return render(request, 'empresa/listEAp.html', {
        'oferta_actual': oferta_actual,
        'estudiantes': estudiantes, 
        'ofertas': ofertas
    })


def mis_datos(request):
    nit_empresa = request.session.get('nit')
    if nit_empresa:
        try:
            empresa = Empresa.objects.get(nit=nit_empresa)
            data = {
                'nombre': empresa.nom_empresa,
                'correo': empresa.correo_emp,
                'nit': empresa.nit,
                'ofertas_creadas': empresa.ofertas_creadas.count(),
                'ofertas_activas': empresa.ofertas_activas.count(),
                'ofertas_desactivadas': empresa.ofertas_desactivadas.count(),
            }
            print(data)
            return JsonResponse(data)
        except Empresa.DoesNotExist:
            return JsonResponse({'error': 'Empresa no encontrada'}, status=404)
    return JsonResponse({'error': 'No autenticado'}, status=401)

@csrf_exempt
def guardarContra(request):
    if request.method == 'POST':
        nit = request.session.get('nit')
        # Busco la tabla de estudiantes
        empresas = Empresa.objects.filter(nit=nit)
        if empresas.exists():
            empresa = empresas[0]
        else:
            return JsonResponse({'status': 'error', 'message': 'Empresa no encontrado.'})

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
        if not check_password(viejaContra, empresa.password_emp):
            return JsonResponse({'status': 'error', 'message': 'La contraseña actual es incorrecta.'})

        # Comparamos las dos contraseñas por si son iguales
        if nuevaContra1 != nuevaContra2:
            return JsonResponse({'status': 'error', 'message': 'Las contraseñas no coinciden.'})
        
        # Comparamos que no repita la misma contraseña que ya tiene
        if check_password(nuevaContra1, empresa.password_emp):
            return JsonResponse({'status': 'error', 'message': 'La nueva contraseña debe ser diferente.'})

        try:
            # Guardamos la nueva contraseña de forma encriptada
            empresa.password_emp = make_password(nuevaContra1)
            empresa.save()
            return JsonResponse({'status': 'success', 'message': 'Su contraseña se a actualizado correctamente.'})
        except Exception as e:
            # Error por el cual no se pudo guardar
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    # En caso de que no se este realizando un post
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})
