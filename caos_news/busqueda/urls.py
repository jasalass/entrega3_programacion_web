from django.urls import path
from . import views

urlpatterns = [
    path('', views.busqueda, name='busqueda')
]