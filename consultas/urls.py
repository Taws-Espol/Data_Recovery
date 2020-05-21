from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="consultas-home"),
    path('contactos/', views.contactos, name="consultas-contactos"),
    path('informacion/', views.contactos, name="consultas-informacion"),
    path('facebook_scrapper/', views.facebook, name="consultas-facebook"),
    path('instagram_scrapper/', views.instagram, name="consultas-instagram"),
]