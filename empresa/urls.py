from django.urls import path
from . import views

urlpatterns = [
    path('', views.empresa, name='empresa'),
    path('about-me/', views.aboutMe, name='aboutMeStudent'), 
]
