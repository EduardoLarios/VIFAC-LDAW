from django.db import models

# Create your models here.

class Participante(models.Model):
    full_name = models.CharField(
        max_length=512,
        db_index=True,
        verbose_name='Participante Name',
        help_text="Participante's name"
    )

    def __str__(self):
        return self.full_name


class Panfleta(models.Model):
    folio = models.CharField(max_length=15)
    devuelta = models.BooleanField()
    monto_entregado = models.IntegerField()
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)

