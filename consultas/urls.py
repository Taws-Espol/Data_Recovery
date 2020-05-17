from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="consultas-home"),
    path('facebook_scrapper/', views.facebook, name="consultas-facebook"),
    path('instagram_scrapper/', views.instagram, name="consultas-instagram"),
    path('facebook_scrapper/publicaciones', views.publicaciones, name="consultas-facebook-publicaciones"),
    path('facebook_scrapper/comentarios', views.comentarios, name="consultas-facebook-comentarios"),
    path("descargar_archivo", views.descargar, name="consultas-descargar")
]