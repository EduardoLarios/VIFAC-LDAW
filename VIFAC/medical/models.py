from django.db import models

# Create your models here.


class Exp_Medico(models.Model):

    FUM = models.DateField(
        verbose_name='FUM',
    )

    ciclos = models.CharField(
        max_length=512,
    )

    uso_anticonceptivos_FUM = models.CharField(
        max_length=512,
    )

    