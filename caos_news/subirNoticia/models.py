from django.db import models

from login.models import Usuario

class Noticia(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    bajada_de_titulo = models.CharField(max_length=150, null=True, blank=True)
    cuerpo = models.TextField(max_length=2000, null=False)
    imagen = models.ImageField(upload_to='noticias/', null=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) 

    def __str__(self):
        return self.titulo