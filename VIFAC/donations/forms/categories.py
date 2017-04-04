# -*- coding: utf-8 -*-
from django import forms


class CategoriesForm(forms.Form):
	
	name = forms.CharField(
		max_length = 256,
		label = 'Nombre de Categoría',
		help_text= 'Cómo se llamará esta categoría de donación'
	)
	
	description = forms.CharField(
		max_length = 256,
		label = 'Descripción de categoría',
		help_text= 'Ej: Monetaría, alimentaria, descripción general, etc...'
	)