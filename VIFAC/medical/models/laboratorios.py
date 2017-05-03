from django.db import models
from datetime import date
from .expediente import Exp_Medico
from django.utils.timezone import now

class Laboratorio(models.Model):

    date = models.DateField(
        null=False,
        blank=False,
        default=now,
        verbose_name="Lab's date"
    )
    result = models.CharField(
        max_length=512,
        null=False,
        blank=False,
    )
    paciente = models.ForeignKey(Exp_Medico,
        null = True,
        on_delete = models.CASCADE
    )


class Ultrasonido(models.Model):

    date = models.DateField(
        null=False,
        blank=False,
        default = now,
        verbose_name="Ultrasonido's date"
    )
    result = models.CharField(
        max_length=512,
        null=False,
        blank=False,
    )
    paciente = models.ForeignKey(Exp_Medico,
        null = True,
        on_delete = models.CASCADE
    )

