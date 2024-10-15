from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'login/home.html')


def inicioS(request):
    return render(request, 'login/InicioS.html')
