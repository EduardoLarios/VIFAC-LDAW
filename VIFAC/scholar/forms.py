from django import forms
from .models import Escuela, Material


class AsignarMaterial(forms.ModelForm):
    
    class Meta:
        model = Material
        fields = ['descripcion', 'categoria', 'entrego']
    
        
class EscuelaForm(forms.ModelForm):
    
    class Meta:
        model = Escuela
        fields = ['name', 'ciudad', 'estado']