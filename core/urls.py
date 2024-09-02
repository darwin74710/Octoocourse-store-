from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ventas/', views.ventas, name='ventas'),
]