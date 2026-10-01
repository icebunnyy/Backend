from django.db import models

class Artista(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50, blank=True, null=True)
    tag_color = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.CharField(max_length=255, blank=True, null=True)
    oyentes_mensuales = models.CharField(max_length=20, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)

    # Propiedad para que el HTML reconozca artista.albumes y convierta las canciones de texto a lista
    @property
    def albumes(self):
        lista_albumes = []
        for alb in self.albumes_set.all():  # O album_set dependiendo de cómo se generó tu relación
            # Si las canciones están guardadas como texto separado por comas o saltos de línea, las convertimos en lista:
            canciones_list = alb.canciones.split(',') if alb.canciones else []
            lista_albumes.append({
                'titulo': alb.titulo,
                'lanzamiento': alb.lanzamiento,
                'portada': alb.portada,
                'canciones': [c.strip() for c in canciones_list]
            })
        return lista_albumes

    @property
    def eventos(self):
        return self.eventos_set.all() # O evento_set

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'artistas'

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, db_column='artista_id', related_name='albumes_set')
    titulo = models.CharField(max_length=100)
    lanzamiento = models.CharField(max_length=10, blank=True, null=True)
    portada = models.CharField(max_length=255, blank=True, null=True)
    canciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'albumes'

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, db_column='artista_id', related_name='eventos_set')
    lugar = models.CharField(max_length=150, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventos'