from django.db import models
#exampleee

class Escuela(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Nombre de la Escuela',
        help_text='Nombre de la Escuela'
    )
    ciudad = models.CharField(
        max_length=256,
        verbose_name='Ciudad',
        help_text='Ciudad de la escuela'
    )
    estado = models.CharField(
        max_length=256,
        verbose_name='Estado',
        help_text='Estado donde está la escuela'
    )
    
    def __str__(self):
        return self.name


class Material(models.Model):
    categoria = models.CharField(
        max_length=128,
        verbose_name='Categoria de material',
        help_text="Nombre de categoria"
    )
    descripcion = models.CharField(
        max_length=256,
        verbose_name='Descripcion',
        help_text='Descripcion del producto'
    )
    entrego = models.CharField(
        max_length=256,
        verbose_name='Quien entrego',
        help_text='Persona que entrego el material'
    )
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descripcion

