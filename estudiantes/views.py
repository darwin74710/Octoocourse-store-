from django.shortcuts import render

def home(request):
    return render(request, 'estudiantes/home.html')

def config(request):
    return render(request, 'estudiantes/config.html')
