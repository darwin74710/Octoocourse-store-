from django.urls import path
from . import views, views_data

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('Cursos/', views.Cursos, name='Cursos'),
    path('Cursos/Info/', views.CursosInfo, name='CursosInfo'),
    path('Cursos/Content/', views.CursosContent, name='CursosContent'),
    path('Ofertas/', views.Ofertas, name='Ofertas'),
    path('Ofertas/Info/', views.OfertasInfo, name='OfertasInfo'),
    path('Configuración/', views.Configuracion, name='Configuracion'),

    path('guardarContra/', views_data.guardarContra, name='guardarContra'),
    path('guardarHV/', views_data.guardarHV, name='guardarHV'),
]