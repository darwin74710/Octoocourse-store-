from django.shortcuts import render
from administrator.models_empresas import Empresas, OfertasEmpleos
from django.db import connection, transaction
from django.http import HttpResponse
from django.shortcuts import redirect

def empresaAdmin(request):
    empresas = Empresas.objects.all()

    return render(request, 'administrator/modifiEmpresas.html', {'empresas': empresas})

def empresaEditar(request):
    idEmpresa = request.GET.get('idEmpresa')
    empresa = Empresas.objects.filter(nit = idEmpresa).first()

    return render(request, 'administrator/empresaEditar.html', {'empresa': empresa})

def empresaEliminar(request):
    idEmpres = request.GET.get('idEmpresa')
    empresa = Empresas.objects.filter(nit = idEmpres).first()
    ofertas = OfertasEmpleos.objects.filter(nit = idEmpres)

    if empresa is None:
        return HttpResponse("Empresa no encontrada", status=404)
    else:
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
                        "DELETE FROM RESPUESTAS_OFERTAS WHERE ID_OFERTA = %s",
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