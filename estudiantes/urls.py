from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('Cursos/', views.Cursos, name='Cursos'),
    path('Cursos/Info/', views.CursosInfo, name='CursosInfo'),
    path('Ofertas/', views.Ofertas, name='Ofertas'),
    path('Ofertas/Info/', views.OfertasInfo, name='OfertasInfo'),
    path('Configuración/', views.Configuracion, name='Configuracion'),
]