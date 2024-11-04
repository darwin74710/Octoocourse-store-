from django.shortcuts import render
from administrator.models_empresas import Empresas

def empresaAdmin(request):
    empresas = Empresas.objects.all()

    return render(request, 'administrator/modifiEmpresas.html', {'empresas': empresas})