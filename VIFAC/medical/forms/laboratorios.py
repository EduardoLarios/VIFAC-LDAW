from django.forms import ModelForm
from ..models. laboratorios import Laboratorio, Ultrasonido

class LaboratorioForm(ModelForm):

    class Meta:
        model = Laboratorio
        fields = [ 'date', 'result' ]

class UltraSonidoForm(ModelForm):

    class Meta:
        model = Ultrasonido
        fields = ['date', 'result']