from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')


def ventas(request):
    return render(request, 'core/ventas.html')