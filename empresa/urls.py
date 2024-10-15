from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioE, name='inicioE'),
    path('about-me/', views.aboutMe, name='aboutMeStudent'), 
    path('estudiantes/', views.estudiantesE, name='estudiantesE'), 
    path('configE/', views.configE, name='configE'), 
    path('ofertasE/', views.ofertasE, name='ofertasE'), 
    path('publicarO/', views.publicaro, name='publicaro'), 
    path('DetallesOferta/', views.DetallesOferta, name='DetallesOferta'), 
    path('listEAp/', views.listEAp, name='listEAp'), 






]
