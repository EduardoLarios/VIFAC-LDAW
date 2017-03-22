from django import forms
from .models import Panfleta, Participante
class AsignPanfletForm(forms.ModelForm):

    class Meta:
        model = Panfleta
        fields = ['folio',]

class PanfletForm(forms.ModelForm):

    class Meta:
        model = Panfleta
        fields = ['devuelta', 'monto_entregado']