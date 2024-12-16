from django.urls import path
from . import views
from administrator.views import administratorAdmin

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.inicioS, name='inicioS'),
    path('administrator/', administratorAdmin, name='administrator'),
]