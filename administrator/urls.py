from django.urls import path
from . import views

urlpatterns = [
    path('', views.administrator, name='administrator'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('estudiantes/cursos/', views.curso, name='curso'),
    path('empresa/', views.empresa, name='empresa'),
    path('empresa/about-me/', views.aboutMe, name='aboutMeStudent'), 
]