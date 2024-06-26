#Archivo con las rutas de las vistas de la app
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.vista_login, name='login'),
     path('registro/', views.registro_usuario, name='registro'),
     path('logout/', LogoutView.as_view(next_page='index'), name='logout')
]