from django.urls import path
from . import views

urlpatterns = [
    path('', views.administratorAdmin, name='administratorAdmin'),
    path('estudiantes/', views.estudiantesAdmin, name='estudiantesAdmin'),
    path('estudiantes/cursos/', views.cursoAdmin, name='cursoAdmin'),
    path('empresa/', views.empresaAdmin, name='empresaAdmin'),
    path('empresa/about-me/', views.aboutMeAdmin, name='aboutMeStudentAdmin'), 
]