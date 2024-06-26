#Archivo con las rutas de las vistas de la app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.subirNoticia, name='subir-noticia'),
    path('listar-noticias/', views.lista_noticias, name='listar-noticias'),
    path('noticia/<int:pk>/editar/', views.actualizar_noticia, name='actualizar_noticia'),
    path('noticia/<int:pk>/eliminar/', views.eliminar_noticia, name='eliminar_noticia'),
]

