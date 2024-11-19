from administrator.models_empresas import OfertasEmpleos, TipoCont, Conocimientos
from django.db import connection, transaction
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.urls import reverse
import os
import shutil
from django.conf import settings

def ofertaAdmin(request):
    ofertas = OfertasEmpleos.objects.all()

    return render(request, 'administrator/modifiOfertas.html', {'ofertas': ofertas})

def ofertaEditar(request):
    idOferta = request.GET.get('idOferta')
    tipoCont = TipoCont.objects.all()

    oferta = OfertasEmpleos.objects.filter(id_oferta = idOferta).first()

    Datos = {
        'oferta': oferta,
        'tipoCont': tipoCont,
    }

    return render(request, 'administrator/ofertaEditar.html', Datos)

def ofertaEliminar(request):
    idOferta = request.GET.get('idOferta')
    oferta = OfertasEmpleos.objects.filter(id_oferta = idOferta).first()

    if oferta is None:
        return HttpResponse("Oferta no encontrada", status=404)
    else:
        # Elimino todas las carpetas de los pdfs
        carpetaPDF1 = 'OfertasExamenes/Examenes/' + str(oferta.nit.nit) + '/' + str(oferta.id_oferta)
        ExamenPDF = os.path.join(settings.DATA_ROOT, carpetaPDF1)

        carpetaPDF2 = 'OfertasExamenes/Respuestas/' + str(oferta.nit.nit) + '/' + str(oferta.id_oferta)
        RespuestasPDF = os.path.join(settings.DATA_ROOT, carpetaPDF2)

        if os.path.exists(ExamenPDF):
            shutil.rmtree(ExamenPDF)
        
        if os.path.exists(RespuestasPDF):
            shutil.rmtree(RespuestasPDF)

        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM CONOCIMIENTOS WHERE ID_OFERTA = %s",
                    [idOferta]
                )
                cursor.execute(
                    "DELETE FROM OFERTAS_DISPONIBLES WHERE ID_OFERTA = %s",
                    [idOferta]
                )
                cursor.execute(
                    "DELETE FROM OFERTAS_EMPLEOS WHERE ID_OFERTA = %s",
                    [idOferta]
                )

    return redirect('ofertaAdmin')

def conocimientos(request):
    idOferta = request.GET.get('idOferta')
    ofertaEmpleo = OfertasEmpleos.objects.filter(id_oferta = idOferta).first()

    conocimientos = Conocimientos.objects.filter(id_oferta = idOferta)

    Datos = {
        'oferta': ofertaEmpleo,
        'conocimientos': conocimientos,
    }

    return render(request, 'administrator/modifiConocimientos.html', Datos)

@csrf_exempt
def crearConocimiento(request):
    if request.method == 'POST':
        nombConocimiento = request.POST.get('nombConocimiento').strip()
        idOferta = request.POST.get('idOferta')

        # Validaciones
        if nombConocimiento == "":
            return JsonResponse({'status': 'error', 'message': 'El conocimiento necesita un nombre.'})
        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO CONOCIMIENTOS (nom_con, id_oferta) " +
                        "VALUES (%s, %s)",
                        [nombConocimiento, idOferta]
                    )
            return JsonResponse({'status': 'success', 'message': 'El conocimiento se añadio correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        
@csrf_exempt
def editarConocimiento(request):
    if request.method == 'POST':
        nombConocimiento = request.POST.get('nombConocimiento').strip()
        idConocimiento = request.POST.get('idConocimiento')

        # Validaciones
        if nombConocimiento == "":
            return JsonResponse({'status': 'error', 'message': 'El conocimiento necesita un nombre.'})
        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE CONOCIMIENTOS SET nom_con = %s WHERE id_conocimiento = %s",
                        [nombConocimiento, idConocimiento]
                    )
            return JsonResponse({'status': 'success', 'message': 'El conocimiento se modificó correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        
@csrf_exempt
def eliminarConocimiento(request):
    idConocimiento = request.GET.get('idConocimiento')
    idOferta = request.GET.get('idOferta')

    with transaction.atomic():
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM CONOCIMIENTOS WHERE id_conocimiento = %s",
                [idConocimiento]
            )
    
    return redirect(f'{reverse("conocimientos")}?idOferta={idOferta}')
