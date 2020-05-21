from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OpcionesScrapperPublicaciones, OpcionesScrapperInstagram, OpcionesScrapperComentarios
from django.contrib import messages
from funciones import FacebookBot as fb_bot
from funciones import InstagramBot as ig_bot
import threading

# Create your views here.

def home(request):
    return render(request,"consultas/home.html")

def contactos(request):
    return render(request,"consultas/contactos.html")

def informacion(request):
    return render(request,"consultas/informacion.html")

def facebook(request):
    if request.method == 'POST':
        form_pu = OpcionesScrapperPublicaciones(request.POST)
        if form_pu.is_valid():
            form_pu.save()
            pagina=form_pu.cleaned_data.get("pagina")
            cantidad_publicaciones=int(form_pu.cleaned_data.get("cantidad_comentarios"))
            messages.success(request, f'El Scrapper ha finalizado, a continuacion puede descargar el archivo')
            h1=threading.Thread(name="hilo_publicaciones", target=fb_bot.imprimir_publicaciones, args=(pagina,cantidad_publicaciones))
            h1.start()
            h1.join()
            return render(request,'consultas/descargar.html',{"ruta":"archivos/Facebook_Publicaciones.tsv"})

        form_co = OpcionesScrapperComentarios(request.POST)
        if form_co.is_valid():
            form_co.save()
            url_publicacion = form_co.cleaned_data.get("url_publicacion")
            tipo_comentario = form_co.cleaned_data.get("tipo_comentario")
            messages.success(request, f'El Scrapper ha finalizado, a continuacion puede descargar el archivo')
            h3 = threading.Thread(name="hilo_comentarios", target=fb_bot.imprimir_comentarios,args=(url_publicacion, tipo_comentario))
            h3.start()
            h3.join()
            return render(request,'consultas/descargar.html',{"ruta":"archivos/Facebook_Comentarios.tsv"})
    else:
        form_pu = OpcionesScrapperPublicaciones()
        form_co = OpcionesScrapperComentarios()

    return render(request,"consultas/facebook.html", {"form_pu":form_pu,"form_co":form_co})

def instagram(request):
    if request.method == 'POST':
        form = OpcionesScrapperInstagram(request.POST)
        if form.is_valid():
            form.save()
            url_ubicacion=form.cleaned_data.get("url_ubicacion")
            cantidad_publicaciones=int(form.cleaned_data.get("cantidad_publicaciones"))
            messages.success(request, f'El Scrapper ha finalizado, a continuacion puede descargar el archivo')
            h2=threading.Thread(name="hilo_instagram", target=ig_bot.imprimir_informacion, args=(url_ubicacion,cantidad_publicaciones))
            h2.start()
            h2.join()
            return render(request,'consultas/descargar.html',{"ruta":"archivos/Instagram.tsv"})
    else:
        form = OpcionesScrapperInstagram()
    return render(request,"consultas/instagram.html", {'form': form})





