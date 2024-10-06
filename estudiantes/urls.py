from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('Cursos/', views.Cursos, name='Cursos'),
    path('Ofertas/', views.Ofertas, name='Ofertas'),
    path('Configuración/', views.Configuracion, name='Configuracion'),
]