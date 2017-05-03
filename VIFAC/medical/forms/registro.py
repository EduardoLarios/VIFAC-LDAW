from ..models.registro import Registro
from ..models.laboratorios import Laboratorio, Ultrasonido
from ..models.problemas import Problemas
from django.forms import *

class RegistroForm(ModelForm):

    class Meta:
        model = Registro
        fields = [
            'date',
            'sdg',
            'ta',
            'weight',
            'fu',
            'posic',
            'fcf',
            'tv',
            'edema',
            'mf',
            'ctx',
            'stv',
            'disuria',
            'flujo',
            'comentario',
        ]

class LaboratorioForm(ModelForm):

    class Meta:
        model = Laboratorio
        fields = [
            'date',
            'result',
        ]


class UltrasonidoForm(ModelForm):
    class Meta:
        model = Ultrasonido
        fields = [
            'date',
            'result',
        ]


class ProblemasForm(ModelForm):
    class Meta:
        model = Problemas
        fields = [
            'descripcion',
            'medicamento',
        ]