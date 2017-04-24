from django.db import models

class Problemas(models.Model):

    descripcion = models.CharField(
        max_length=512,
        null=False,
        blank=False,
    )
    medicamento = models.CharField(
        max_length=512,
        null=False,
        blank=False,
    )
