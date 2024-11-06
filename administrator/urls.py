from django.urls import path
from . import views, views_estudiantes, views_empresas, views_cursos, views_ofertas, views_data

urlpatterns = [
    path('', views.administratorAdmin, name='administratorAdmin'),
    path('Estudiantes/', views_estudiantes.estudiantesAdmin, name='estudiantesAdmin'),
    path('Estudiantes/Modificar/', views_estudiantes.estudianteEditar, name='estudianteEditar'),
    path('Estudiantes/HojaVida/', views_estudiantes.hojaVidaVisualizar, name='hojaVidaVisualizar'),
    path('Empresas/', views_empresas.empresaAdmin, name='empresaAdmin'),
    path('Empresas/Modificar/', views_empresas.empresaEditar, name='empresaEditar'),
    path('Cursos/', views_cursos.cursoAdmin, name='cursoAdmin'),
    path('Cursos/Modificar/', views_cursos.cursoEditar, name='cursoEditar'),
    path('Ofertas/', views_ofertas.ofertaAdmin, name='ofertaAdmin'),
    path('Ofertas/Modificar/', views_ofertas.ofertaEditar, name='ofertaEditar'),

    path('guardarHV/', views_data.guardarHVAdmin, name='guardarHVAdmin'),
    path('guardarEstudiante/<int:idStudent>', views_data.guardarEstudianteAdmin, name='guardarEstudianteAdmin'),
    path('guardarEmpresa/<int:idEmpres>', views_data.guardarEmpresaAdmin, name='guardarEmpresaAdmin'),
    path('guardarCurso/<int:idCurse>', views_data.guardarCursoAdmin, name='guardarCursoAdmin'),
    path('guardarOferta/<int:idOfert>', views_data.guardarOfertaAdmin, name='guardarOfertaAdmin'),
]