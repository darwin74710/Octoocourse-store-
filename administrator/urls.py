from django.urls import path
from . import views, views_estudiantes, views_empresas, views_cursos

urlpatterns = [
    path('', views.administratorAdmin, name='administratorAdmin'),
    path('modificarEstudiantes/', views_estudiantes.estudiantesAdmin, name='estudiantesAdmin'),
    path('modificarEmpresas/', views_empresas.empresaAdmin, name='empresaAdmin'),
    path('modificarCursos/', views_cursos.cursoAdmin, name='cursoAdmin'),
]