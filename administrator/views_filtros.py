from administrator.models_cursos import TipoCertificado, TipoContenido, TipoDificultad, TipoDuracion
from administrator.models_empresas import TipoCont
from django.db import connection, transaction
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

@superuser_required
def contenidoAdmin(request):
    tipoContenido = TipoContenido.objects.all()

    return render(request, 'administrator/filtrosContenido.html', {'tipoContenido': tipoContenido})

@superuser_required
def dificultadAdmin(request):
    tipoDificultad = TipoDificultad.objects.all()

    return render(request, 'administrator/filtrosDificultad.html', {'tipoDificultad': tipoDificultad})

@superuser_required
def duracionAdmin(request):
    tipoDuracion = TipoDuracion.objects.all()

    return render(request, 'administrator/filtrosDuracion.html', {'tipoDuracion': tipoDuracion})

@superuser_required
def certificadoAdmin(request):
    tipoCertificado = TipoCertificado.objects.all()

    return render(request, 'administrator/filtrosCertificado.html', {'tipoCertificado': tipoCertificado})

@superuser_required
def contratoAdmin(request):
    tipoContrato = TipoCont.objects.all()

    return render(request, 'administrator/filtrosTipoContrato.html', {'tipoContrato': tipoContrato})

@superuser_required
@csrf_exempt
def crearFiltro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre').strip()
        filtro = request.POST.get('filtro').strip()

        # Validaciones
        if nombre == "":
            return JsonResponse({'status': 'error', 'message': 'El filtro necesita un nombre.'})
        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    if(filtro =='contenido'):
                        cursor.execute(
                            "INSERT INTO TIPO_CONTENIDO (nombre_tipo) " +
                            "VALUES (%s)",
                            [nombre]
                        )
                    elif(filtro =='dificultad'):
                        cursor.execute(
                            "INSERT INTO TIPO_DIFICULTAD (nombre_tipo) " +
                            "VALUES (%s)",
                            [nombre]
                        )
                    elif(filtro =='duracion'):
                        cursor.execute(
                            "INSERT INTO TIPO_DURACION (nombre_tipo) " +
                            "VALUES (%s)",
                            [nombre]
                        )
                    elif(filtro =='certificado'):
                        cursor.execute(
                            "INSERT INTO TIPO_CERTIFICADO (nombre_tipo) " +
                            "VALUES (%s)",
                            [nombre]
                        )
                    elif(filtro =='contrato'):
                        cursor.execute(
                            "INSERT INTO TIPO_CONT (nombre_tipo) " +
                            "VALUES (%s)",
                            [nombre]
                        )
            return JsonResponse({'status': 'success', 'message': 'El filtro se añadio correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

@superuser_required
@csrf_exempt
def editarOferta(request):
    if request.method == 'POST':
        inputNombre = request.POST.get('inputNombre').strip()
        idFiltro = request.POST.get('idFiltro')
        filtro = request.POST.get('filtro').strip()

        # Validaciones
        if inputNombre == "":
            return JsonResponse({'status': 'error', 'message': 'El filtro necesita un nombre.'})
        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    if(filtro =='contenido'):
                        cursor.execute(
                            "UPDATE TIPO_CONTENIDO SET nombre_tipo = %s WHERE id_tipo_contenido = %s",
                            [inputNombre, idFiltro]
                        )
                    elif(filtro =='dificultad'):
                        cursor.execute(
                            "UPDATE TIPO_DIFICULTAD SET nombre_tipo = %s WHERE id_tipo_dificultad = %s",
                            [inputNombre, idFiltro]
                        )
                    elif(filtro =='duracion'):
                        cursor.execute(
                            "UPDATE TIPO_DURACION SET nombre_tipo = %s WHERE id_tipo_duracion = %s",
                            [inputNombre, idFiltro]
                        )
                    elif(filtro =='certificado'):
                        cursor.execute(
                            "UPDATE TIPO_CERTIFICADO SET nombre_tipo = %s WHERE id_tipo_certificado = %s",
                            [inputNombre, idFiltro]
                        )
                    elif(filtro =='contrato'):
                        cursor.execute(
                            "UPDATE TIPO_CONT SET nombre_tipo = %s WHERE id_tipo_cont = %s",
                            [inputNombre, idFiltro]
                        )
            return JsonResponse({'status': 'success', 'message': 'El filtro se modificó correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

@superuser_required
@csrf_exempt
def eliminarFiltro(request):
    idFiltro = request.GET.get('idFiltro')
    filtro = request.GET.get('filtro')
    
    try:
        with transaction.atomic():
            with connection.cursor() as cursor:
                if(filtro =='contenido'):
                    cursor.execute(
                        "DELETE FROM TIPO_CONTENIDO WHERE id_tipo_contenido = %s",
                        [idFiltro]
                    )
                    return redirect(reverse("contenidoAdmin"))
                
                elif(filtro =='dificultad'):
                    cursor.execute(
                        "DELETE FROM TIPO_DIFICULTAD WHERE id_tipo_dificultad = %s",
                        [idFiltro]
                    )
                    return redirect(reverse("dificultadAdmin"))
                
                elif(filtro =='duracion'):
                    cursor.execute(
                        "DELETE FROM TIPO_DURACION WHERE id_tipo_duracion = %s",
                        [idFiltro]
                    )
                    return redirect(reverse("duracionAdmin"))
                
                elif(filtro =='certificado'):
                    cursor.execute(
                        "DELETE FROM TIPO_CERTIFICADO WHERE id_tipo_certificado = %s",
                        [idFiltro]
                    )
                    return redirect(reverse("certificadoAdmin"))
                
                elif(filtro =='contrato'):
                    cursor.execute(
                        "DELETE FROM TIPO_CONT WHERE id_tipo_cont = %s",
                        [idFiltro]
                    )
                    return redirect(reverse("contratoAdmin"))
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': 'No puedes eliminar un filtro que se encuentre vinculado a una oferta o un curso.'})
            
    return redirect(reverse("administratorAdmin"))