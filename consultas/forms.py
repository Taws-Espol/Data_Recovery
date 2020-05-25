from django import forms
from .models import ScrapperPublicaciones, ScrapperInstagram, ScrapperComentarios

class OpcionesScrapperPublicaciones(forms.ModelForm):
    class Meta:
        model = ScrapperPublicaciones
        fields = ['pagina','cantidad_publicaciones']

class OpcionesScrapperInstagram(forms.ModelForm):
    class Meta:
        model= ScrapperInstagram
        fields=["url_ubicacion","cantidad_publicaciones"]

class OpcionesScrapperComentarios(forms.ModelForm):
    class Meta:
        model=ScrapperComentarios
        fields=["url_publicacion","tipo_comentario"]