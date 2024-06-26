from django.urls import path
from . import views

urlpatterns = [
    path('', views.suscripcion, name='suscripcion')
]