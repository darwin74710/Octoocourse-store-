from django.shortcuts import render

def empresa(request):
    return render(request, 'empresa/empresa.html')

def aboutMe(request):
    return render(request, 'empresa/aboutMeStudent.html')