from django.db import models
from django.core.validators import MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Participante(models.Model):
    full_name = models.CharField(
        max_length=512,
        verbose_name='Participante Name',
        help_text="Participante's name"
    )
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.full_name


class Panfleta(models.Model):
    folio = models.CharField(max_length=15)
    devuelta = models.BooleanField(default=False)
    monto_entregado = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(1250)])
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)

    def __str__(self):
        return self.folio

