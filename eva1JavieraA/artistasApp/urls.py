from django.urls import path
from artistasApp import views

urlpatterns = [
    path('', views.inicio_artistas, name='inicio'),
    path('artista/<slug:artista_id>/', views.detalle_artista, name='detalle_artista'),
]