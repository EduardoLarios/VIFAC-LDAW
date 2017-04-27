from django.db import models
from .expediente import Exp_Medico

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
    paciente = models.ForeignKey(Exp_Medico,
        null = True
    )
