from django import forms
from .models import ScrapperPublicaciones, ScrapperInstagram

class OpcionesScrapperPublicaciones(forms.ModelForm):
    class Meta:
        model = ScrapperPublicaciones
        fields = ['pagina','cantidad_comentarios']

class OpcionesScrapperInstagram(forms.ModelForm):
    class Meta:
        model= ScrapperInstagram
        fields=["url_ubicacion","cantidad_publicaciones"]