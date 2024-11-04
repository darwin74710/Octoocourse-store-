from django.urls import path
from . import views_cursos, views_data, views_ofertas, views_config

urlpatterns = [
    path('', views_cursos.Inicio, name='Inicio'),
    path('Cursos/', views_cursos.CursosPrincipal, name='Cursos'),
    path('Cursos/Info/', views_cursos.CursosInfo, name='CursosInfo'),
    path('Cursos/Content/', views_cursos.CursosContent, name='CursosContent'),
    path('Ofertas/', views_ofertas.Ofertas, name='Ofertas'),
    path('Ofertas/Info/', views_ofertas.OfertasInfo, name='OfertasInfo'),
    path('Configuración/', views_config.Configuracion, name='Configuracion'), 
    path('guardarContra/', views_data.guardarContra, name='guardarContra'),
    path('guardarHV/', views_data.guardarHV, name='guardarHV'),
    path('logout/', views_cursos.logout_view, name='logout'),  

]