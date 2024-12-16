from django.shortcuts import render
from administrator.models_empresas import Empresas, OfertasEmpleos
from django.db import connection, transaction
from django.http import HttpResponse
from django.shortcuts import redirect
import os
import shutil
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test

def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

@superuser_required
def empresaAdmin(request):
    empresas = Empresas.objects.all()

    return render(request, 'administrator/modifiEmpresas.html', {'empresas': empresas})

@superuser_required
def empresaEditar(request):
    idEmpresa = request.GET.get('idEmpresa')
    empresa = Empresas.objects.filter(nit = idEmpresa).first()

    return render(request, 'administrator/empresaEditar.html', {'empresa': empresa})

@superuser_required
def empresaEliminar(request):
    idEmpres = request.GET.get('idEmpresa')
    empresa = Empresas.objects.filter(nit = idEmpres).first()
    ofertas = OfertasEmpleos.objects.filter(nit = idEmpres)

    if empresa is None:
        return HttpResponse("Empresa no encontrada", status=404)
    else:
        # Elimino todas las carpetas de los pdfs
        carpetaPDF1 = 'OfertasExamenes/Examenes/' + str(idEmpres)
        ExamenesPDF = os.path.join(settings.DATA_ROOT, carpetaPDF1)

        carpetaPDF2 = 'OfertasExamenes/Respuestas/' + str(idEmpres)
        RespuestasPDF = os.path.join(settings.DATA_ROOT, carpetaPDF2)

        if os.path.exists(ExamenesPDF):
            shutil.rmtree(ExamenesPDF)
        
        if os.path.exists(RespuestasPDF):
            shutil.rmtree(RespuestasPDF)

        with transaction.atomic():
            with connection.cursor() as cursor:
                for oferta in ofertas:
                    cursor.execute(
                        "DELETE FROM CONOCIMIENTOS WHERE ID_OFERTA = %s",
                        [oferta.id_oferta]
                    )
                    cursor.execute(
                        "DELETE FROM OFERTAS_DISPONIBLES WHERE ID_OFERTA = %s",
                        [oferta.id_oferta]
                    )
                    cursor.execute(
                        "DELETE FROM OFERTAS_EMPLEOS WHERE ID_OFERTA = %s",
                        [oferta.id_oferta]
                    )
                
                cursor.execute(
                        "DELETE FROM EMPRESAS WHERE NIT = %s",
                        [idEmpres]
                    )
    return redirect('empresaAdmin')