from django.shortcuts import render
from administrator.models_empresas import Empresas

def empresaAdmin(request):
    empresas = Empresas.objects.all()

    return render(request, 'administrator/modifiEmpresas.html', {'empresas': empresas})

def empresaEditar(request):
    idEmpresa = request.GET.get('idEmpresa')
    empresa = Empresas.objects.filter(nit = idEmpresa).first()

    return render(request, 'administrator/empresaEditar.html', {'empresa': empresa})