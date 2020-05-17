from django.db import models

# Create your models here.

class ScrapperPublicaciones(models.Model):
    pagina = models.CharField(max_length=100)
    cantidad_comentarios = models.CharField(max_length=100)

class ScrapperInstagram(models.Model):
    url_ubicacion=models.CharField(max_length=100)
    cantidad_publicaciones=models.CharField(max_length=100)