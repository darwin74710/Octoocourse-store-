from django.shortcuts import render


def inicioE(request):
    return render(request, 'empresa/inicioE.html')

def aboutMe(request):
    return render(request, 'empresa/aboutMeStudent.html')


def estudiantesE(request):
    return render(request, 'empresa/estudiantesE.html')


def configE(request):
    return render(request, 'empresa/configE.html')

def ofertasE(request):
    return render(request, 'empresa/ofertasE.html')


def des_ofertas(request):
    return render(request, 'empresa/des_ofertas.html')

def listEAp(request):
    return render(request, 'empresa/listEAp.html')

def publicaro(request):
    return render(request, 'empresa/publicaro.html')

def DetallesOferta(request):
    return render(request, 'empresa/DetallesOferta.html')




