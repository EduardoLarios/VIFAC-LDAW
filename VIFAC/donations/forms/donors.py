# -*- coding: utf-8 -*-
from phonenumber_field.formfields import PhoneNumberField
from ..models.donors import State
from django import forms


class DonorForm(forms.Form):
    
    full_name = forms.CharField(
        max_length = 512,
        label = "Nombre del donador",
        help_text = 'Nombre con apellidos'
    )
    
    integration_date = forms.DateField(
        widget = forms.DateInput(attrs = { 'type': 'date' }),
        help_text = 'Fecha en que se integró a la organización, por default hoy '
    )
    
    state = forms.ChoiceField(
        choices = State,
        label = 'Estado'
    )
    
    city = forms.CharField(
        max_length = 256,
        label = 'Ciudad'
    )
    
    street = forms.CharField(
        max_length = 256,
        label = 'Calle y Colonia'
    )
    
    number = forms.CharField(
        max_length = 8,
        label = 'Número Exterior'
    )
    
    reference = forms.CharField(
        max_length = 256,
        label = 'Referencia',
        help_text = "Persona quien introdujo al donador a config"
    )
    
    contact_name = forms.CharField(
        max_length = 512,
        label = 'Nombre del contacto',
        help_text = "Nombre del contacto con donador"
    )
    
    contact_email = forms.EmailField(
        max_length = 256,
        label = 'Correo del contacto',
        help_text = "Introduzca un correo electrónico válido"
    )
    
    contact_phone_number = PhoneNumberField(
        initial = '+52'
    )
    
    contact_birthday = forms.DateField(
        widget = forms.DateInput(attrs = { 'type': 'date' })
    )
    
    contact_anniversary= forms.DateField(
        widget = forms.DateInput(attrs = { 'type': 'date' })
    )
    
    
    
    
    
