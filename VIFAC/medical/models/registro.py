from django.db import models
from datetime import date
from .expediente import Exp_Medico
from django.utils.timezone import now

class Registro(models.Model):

    date = models.DateField(
        null=False,
        blank=False,
        default=now,
        verbose_name="Register's date"
    )
    sdg = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        default='',
        verbose_name="SDG"
    )
    ta = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        default='',
        verbose_name="ta"
    )
    weight = models.PositiveIntegerField(
        null=False,
        blank=False
    )
    fu = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        default='',
        verbose_name="fu"
    )
    posic = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        default='',
        verbose_name="fu"
    )
    fcf = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        default='',
        verbose_name="fu"
    )
    tv = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        default='',
        verbose_name="fu"
    )
    edema = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        default='',
        verbose_name="fu"
    )
    mf = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        default='',
        verbose_name="fu"
    )
    ctx = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        default='',
        verbose_name="fu"
    )
    stv = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        default='',
        verbose_name="fu"
    )
    disuria = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        default='',
        verbose_name="fu"
    )
    flujo = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        default='',
        verbose_name="fu"
    )
    comentario = models.CharField(
        max_length=512,
        null=False,
        blank=True,
        default='',
        verbose_name="fu"
    )
    paciente = models.ForeignKey(Exp_Medico,
        null = True,
        on_delete = models.CASCADE
    )
