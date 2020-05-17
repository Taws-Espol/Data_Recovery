from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OpcionesScrapperPublicaciones, OpcionesScrapperInstagram
from django.contrib import messages
from funciones import FacebookBot as fb_bot
from funciones import InstagramBot as ig_bot
import threading

# Create your views here.

def home(request):
    return render(request,"consultas/home.html")

def facebook(request):
    if request.method == 'POST':
        form = OpcionesScrapperPublicaciones(request.POST)
        if form.is_valid():
            form.save()
            pagina=form.cleaned_data.get("pagina")
            cantidad_publicaciones=int(form.cleaned_data.get("cantidad_comentarios"))
            messages.success(request, f'El Scrapper ha finalizado, a continuacion puede descargar el archivo')
            h1=threading.Thread(name="hilo_publicaciones", target=fb_bot.imprimir_publicaciones, args=(pagina,cantidad_publicaciones))
            h1.start()
            h1.join()
            return redirect('consultas-descargar')
    else:
        form = OpcionesScrapperPublicaciones()
    return render(request,"consultas/facebook.html", {"form":form})

def instagram(request):
    if request.method == 'POST':
        form = OpcionesScrapperInstagram(request.POST)
        if form.is_valid():
            form.save()
            url_ubicacion=form.cleaned_data.get("url_ubicacion")
            cantidad_publicaciones=int(form.cleaned_data.get("cantidad_publicaciones"))
            messages.success(request, f'El Scrapper ha finalizado, a continuacion puede descargar el archivo')
            h2=threading.Thread(name="hilo_publicaciones", target=ig_bot.imprimir_informacion, args=(url_ubicacion,cantidad_publicaciones))
            h2.start()
            h2.join()
            return redirect('consultas-descargar')
    else:
        form = OpcionesScrapperInstagram()
    return render(request,"consultas/instagram.html", {'form': form})

def comentarios(request):
    return HttpResponse("<h1>Scrapper de los comenarios de una publicacion de Facebook</h1>")

def descargar(request):
    return render(request,"consultas/descargar.html")




