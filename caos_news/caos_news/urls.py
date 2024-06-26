from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Conectar el mapeador, aquí se definen las rutas a los archivos urls.py de cada app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login/', include('login.urls')),
    path('contacto/', include('contacto.urls')),
    path('busqueda/', include('busqueda.urls')),
    path('contactoLaboral/', include('contactoLaboral.urls')),
    path('suscripcion/', include('suscripcion.urls')),
    path('subir-noticia/', include('subirNoticia.urls')),
]

#Configurar que se puedan ver archivos multimedia subidos por los usuarios en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
