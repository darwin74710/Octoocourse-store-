from django.shortcuts import render
from administrator.models_empresas import OfertasEmpleos

def ofertaAdmin(request):
    ofertas = OfertasEmpleos.objects.all()

    return render(request, 'administrator/modifiOfertas.html', {'ofertas': ofertas})

def ofertaEditar(request):
    idOferta = request.GET.get('idOferta')
    oferta = OfertasEmpleos.objects.filter(id_oferta = idOferta).first()

    return render(request, 'administrator/ofertaEditar.html', {'oferta': oferta})