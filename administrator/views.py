from django.shortcuts import render

def administrator(request):
    return render(request, 'administrator/administrator.html')

def estudiantes(request):
    return render(request, 'administrator/estudiantes.html')

def curso(request):
    return render(request, 'administrator/curso.html')

def empresa(request):
    return render(request, 'administrator/empresa.html')

def aboutMe(request):
    return render(request, 'administrator/aboutMeStudent.html')