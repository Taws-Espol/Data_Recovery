from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="consultas-home"),
    path('facebook_scrapper/', views.facebook, name="consultas-facebook"),
    path('instagram_scrapper/', views.instagram, name="consultas-instagram"),
]