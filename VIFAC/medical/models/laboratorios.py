from django.db import models
from datetime import date
from .expediente import Exp_Medico


class Laboratorio(models.Model):

    date = models.DateField(
        null=False,
        blank=False,
        default=date.today,
        verbose_name="Lab's date"
    )
    result = models.CharField(
        max_length=512,
        null=False,
        blank=False,
    )
    paciente = models.ForeignKey(Exp_Medico,
        null = True
    )


class Ultrasonido(models.Model):

    date = models.DateField(
        null=False,
        blank=False,
        default=date.today,
        verbose_name="Ultrasonido's date"
    )
    result = models.CharField(
        max_length=512,
        null=False,
        blank=False,
    )
    paciente = models.ForeignKey(Exp_Medico,
        null = True
)

