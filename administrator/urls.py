from django.urls import path
from . import views, views_estudiantes, views_empresas, views_cursos, views_ofertas, views_data, views_filtros

urlpatterns = [
    path('', views.administratorAdmin, name='administratorAdmin'),
    path('Estudiantes/', views_estudiantes.estudiantesAdmin, name='estudiantesAdmin'),
    path('Estudiantes/Modificar/', views_estudiantes.estudianteEditar, name='estudianteEditar'),
    path('Estudiantes/HojaVida/', views_estudiantes.hojaVidaVisualizar, name='hojaVidaVisualizar'),
    path('Estudiantes/Eliminar/', views_estudiantes.estudianteEliminar, name='estudianteEliminar'),

    path('Empresas/', views_empresas.empresaAdmin, name='empresaAdmin'),
    path('Empresas/Modificar/', views_empresas.empresaEditar, name='empresaEditar'),
    path('Empresas/Eliminar/', views_empresas.empresaEliminar, name='empresaEliminar'),

    path('Cursos/', views_cursos.cursoAdmin, name='cursoAdmin'),
    path('Cursos/Añadir/', views_cursos.cursoAñadir, name='cursoAñadir'),
    path('Cursos/Modificar/', views_cursos.cursoEditar, name='cursoEditar'),
    path('Cursos/Eliminar/', views_cursos.cursoEliminar, name='cursoEliminar'),
    
    path('Cursos/Contenidos/', views_cursos.cursoContenidos, name='cursoContenidos'),
    path('Cursos/Contenidos/Crear/', views_cursos.crearContenido, name='crearContenido'),
    path('Cursos/Contenidos/Modificar/', views_cursos.editarContenido, name='editarContenido'),
    path('Cursos/Contenidos/Eliminar/', views_cursos.eliminarContenido, name='eliminarContenido'),

    path('Cursos/SubContenidos/Crear/', views_cursos.crearSubContenido, name='crearSubContenido'),
    path('Cursos/SubContenidos/Modificar/', views_cursos.editarSubContenido, name='editarSubContenido'),
    path('Cursos/SubContenidos/Eliminar/', views_cursos.eliminarSubContenido, name='eliminarSubContenido'),

    path('Cursos/Preguntas/', views_cursos.cursoPreguntas, name='cursoPreguntas'),
    path('Cursos/Preguntas/Crear/', views_cursos.crearPregunta, name='crearPregunta'),
    path('Cursos/Preguntas/Modificar/', views_cursos.editarPregunta, name='editarPregunta'),
    path('Cursos/Preguntas/Eliminar/', views_cursos.eliminarPregunta, name='eliminarPregunta'),

    path('Cursos/Respuestas/Crear/', views_cursos.crearRespuesta, name='crearRespuesta'),
    path('Cursos/Respuestas/Modificar/', views_cursos.editarRespuesta, name='editarRespuesta'),
    path('Cursos/Respuestas/Eliminar/', views_cursos.eliminarRespuesta, name='eliminarRespuesta'),

    path('Ofertas/', views_ofertas.ofertaAdmin, name='ofertaAdmin'),
    path('Ofertas/Modificar/', views_ofertas.ofertaEditar, name='ofertaEditar'),
    path('Ofertas/Eliminar/', views_ofertas.ofertaEliminar, name='ofertaEliminar'),

    path('Ofertas/Conocimientos/', views_ofertas.conocimientos, name='conocimientos'),
    path('Cursos/Conocimientos/Crear/', views_ofertas.crearConocimiento, name='crearConocimiento'),
    path('Cursos/Conocimientos/Modificar/', views_ofertas.editarConocimiento, name='editarConocimiento'),
    path('Cursos/Conocimientos/Eliminar/', views_ofertas.eliminarConocimiento, name='eliminarConocimiento'),

    path('guardarHV/', views_data.guardarHVAdmin, name='guardarHVAdmin'),
    path('guardarEstudiante/<int:idStudent>', views_data.guardarEstudianteAdmin, name='guardarEstudianteAdmin'),
    path('guardarEmpresa/<int:idEmpres>', views_data.guardarEmpresaAdmin, name='guardarEmpresaAdmin'),
    path('guardarCurso/<int:idCurse>', views_data.guardarCursoAdmin, name='guardarCursoAdmin'),
    path('guardarOferta/<int:idOfert>', views_data.guardarOfertaAdmin, name='guardarOfertaAdmin'),

    path('filtros/contenido/', views_filtros.contenidoAdmin, name='contenidoAdmin'),
    path('filtros/dificultad/', views_filtros.dificultadAdmin, name='dificultadAdmin'),
    path('filtros/duracion/', views_filtros.duracionAdmin, name='duracionAdmin'),
    path('filtros/certificado/', views_filtros.certificadoAdmin, name='certificadoAdmin'),
    path('filtros/contrato/', views_filtros.contratoAdmin, name='contratoAdmin'),

    path('filtros/Crear/', views_filtros.crearFiltro, name='crearFiltro'),
    path('filtros/Modificar/', views_filtros.editarOferta, name='editarOferta'),
    path('filtros/Eliminar/', views_filtros.eliminarFiltro, name='eliminarFiltro'),
]