from django.db import models

# Create your models here.

class ScrapperPublicaciones(models.Model):
    pagina = models.CharField(max_length=100)
    cantidad_publicaciones = models.CharField(max_length=100)

class ScrapperInstagram(models.Model):
    url_ubicacion=models.CharField(max_length=100)
    cantidad_publicaciones=models.CharField(max_length=100)

class ScrapperComentarios(models.Model):
    RELEVANTES = 'Más relevantes'
    RECIENTES = 'Más recientes'
    TODOS = 'Todos los comentarios'
    TIPOS_DE_COMENTARIOS = [
        (RELEVANTES, 'Más relevantes'),
        (RECIENTES, 'Más recientes'),
        (TODOS, 'Todos los comentarios'),
    ]
    url_publicacion=models.CharField(max_length=100)
    tipo_comentario=models.CharField(max_length=21,choices=TIPOS_DE_COMENTARIOS,default=RELEVANTES)