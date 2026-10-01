from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def home_general(request):
    return render(request, 'index_general.html') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_general, name='home'),             # La raíz general 
    path('artistas/', include('artistasApp.urls')),  #  app de artistas 
]