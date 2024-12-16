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
    path('aplicarCurso/', views_data.aplicarCurso, name='aplicarCurso'),
    path('Cursos/Pruebas/<int:idEstudiante>/<int:idCurso>/', views_cursos.Pruebas, name='PruebasCursos'),
    path('Cursos/Pruebas/validar/', views_data.validarCurso, name='validarCurso'),
    path('aplicarOferta/', views_data.aplicarOferta, name='aplicarOferta'),
    path('Ofertas/Pruebas/<int:idEstudiante>/<int:idOferta>/', views_ofertas.Pruebas, name='PruebasOfertas'),
    path('Ofertas/Pruebas/Guardar/Respuesta/', views_ofertas.GuardarRespuesta, name='GuardarRespuesta'),
    path('guardarHV/', views_data.guardarHV, name='guardarHV'),
    path('logout/', views_cursos.logout_view, name='logout'),  
    path('acceso_denegado/', views_ofertas.acceso_denegado, name='acceso_denegado'),
    path('acceso_denegado/', views_config.acceso_denegado, name='acceso_denegado'),




]