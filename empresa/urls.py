from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioE, name='inicioE'),
    path('about-me/', views.aboutMe, name='aboutMeStudent'), 
    path('estudiantes/', views.estudiantesE, name='estudiantesE'), 
    path('configE/', views.configE, name='configE'), 
    path('ofertasE/', views.ofertasE, name='ofertasE'), 
    path('des_ofertas/', views.des_ofertas, name='des_ofertas'), 
    path('listEAp/', views.listEAp, name='listEAp'), 






]
