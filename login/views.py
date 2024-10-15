from django.shortcuts import render

# Create your views here.

def inicioS(request):
    return render(request, 'login/InicioS.html')
