# -*- coding: utf-8 -*-
from ..models.categories import Category
from ..models.donors import Donor
from django import forms
from .fields import *



class DonationForm(forms.Form):
    
    description = forms.CharField(
        max_length = 512,
        label = "Descripción de la donación",
        help_text = 'Arroz, $500 pesos, etc...'
    )
    category = ModelChoiceField(
        queryset = Category.objects.all(),
        required = True,
        empty_label = 'Categoría',
        label_fn = lambda c: c.name
    )
    donor = ModelChoiceField(
        queryset = Donor.objects.all(),
        required = True,
        empty_label = 'Donador',
        label_fn = lambda c: c.full_name
    )
    
    
