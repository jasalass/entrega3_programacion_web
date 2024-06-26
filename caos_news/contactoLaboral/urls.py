from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactoLaboral, name='contacto-laboral')
]