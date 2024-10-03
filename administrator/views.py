from django.shortcuts import render

def administratorAdmin(request):
    return render(request, 'administrator/administrator.html')

def estudiantesAdmin(request):
    return render(request, 'administrator/estudiantes.html')

def cursoAdmin(request):
    return render(request, 'administrator/curso.html')

def empresaAdmin(request):
    return render(request, 'administrator/empresa.html')

def aboutMeAdmin(request):
    return render(request, 'administrator/aboutMeStudent.html')

def editOfertas(request):
    return render(request, 'administrator/editOfertas.html')

def editUsuarios(request):
    return render(request, 'administrator/editUsuarios.html')

def editCV(request):
    return render(request, 'administrator/editCV.html')