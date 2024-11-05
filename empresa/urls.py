from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioE, name='inicioE'),
    path('estudiantes/', views.estudiantesE, name='estudiantesE'), 
    path('configE/', views.configE, name='configE'), 
    path('ofertasE/', views.ofertasE, name='ofertasE'), 
    path('empresa/oferta/<int:id_oferta>/', views.detalle_oferta, name='detalle_oferta'),    
    path('eliminar-oferta/<int:id_oferta>/', views.eliminar_oferta, name='eliminar_oferta'),
    path('editar-oferta/<int:id_oferta>/', views.editar_oferta, name='editar_oferta'),
    path('crearOferta/', views.crearOferta, name='crearOferta'), 
    path('listEAp/', views.listEAp, name='listEAp'), 
    path('logout/', views.logout_view, name='logout'),  
    path('estudiantes_lista/', views.estudiantesE, name='lista_estudiantes'),
    path('empresa/estudiante/<int:id_estudiante>/', views.detalle_estudiante, name='detalle_estudiante'),    

]
