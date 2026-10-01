from django.shortcuts import render, get_object_or_404
from .models import Artista

def inicio_artistas(request):
    artistas = Artista.objects.all()
    context = {'artistas': artistas}
    return render(request, 'artistas/inicio.html', context)

def detalle_artista(request, artista_id):
    artista = get_object_or_404(Artista, id=artista_id)
    context = {'artista': artista}
    return render(request, 'artistas/detalle.html', context)