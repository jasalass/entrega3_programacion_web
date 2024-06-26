#Archivo con las rutas de las vistas de la app
from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index')
]