from django.db import models


class Suscripcion(models.Model):
    tipo = models.CharField(max_length=10)
    valor = models.IntegerField()

    def __str__(self):
        return self.tipo