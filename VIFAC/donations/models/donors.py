# -*- coding: utf-8 -*-
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from datetime import *

__all__ = [ 'Donors', 'State' ]

State = (
    ('Ninguno', 'Ninguno'),
    ('Aguascalientes', 'Aguascalientes'),
    ('Baja California', 'Baja California'),
    ('Baja California Sur', 'Baja California Sur'),
    ('Campeche', 'Campeche'),
    ('Chiapas', 'Chiapas'),
    ('Chihuahua', 'Chihuahua'),
    ('CDMX', 'Ciudad de México'),
    ('Coahuila', 'Coahuila'),
    ('Colima', 'Colima'),
    ('Durango', 'Durango'),
    ('Guanajuato','Guanajuato'),
    ('Guerrero', 'Guerrero'),
    ('Hidalgo', 'Hidalgo'),
    ('Jalisco', 'Jalisco'),
    ('Estado de México', 'Estado de México'),
    ('Michoacán', 'Michoacán'),
    ('Morelos', 'Morelos'),
    ('Nayarit', 'Nayarit'),
    ('Nuevo León', 'Nuevo León'),
    ('Oaxaca', 'Oaxaca'),
    ('Puebla', 'Puebla'),
    ('Querétaro', 'Querétaro'),
    ('Quintana Roo', 'Quintana Roo'),
    ('San Luis Potosí', 'San Luis Potosí'),
    ('Sinaloa', 'Sinaloa'),
    ('Sonora', 'Sonora'),
    ('Tabasco', 'Tabasco'),
    ('Tamaulipas', 'Tamaulipas'),
    ('Tlaxcala', 'Tlaxcala'),
    ('Veracruz', 'Veracruz'),
    ('Yucatán', 'Yucatán'),
    ('Zacatecas', 'Zacatecas')
)


class Donor(models.Model):

    full_name = models.CharField(
        max_length = 512,
        db_index = True,
        verbose_name = 'Donor Name',
        help_text = "Donor's name"
    )
    
    integration_date = models.DateField(
        default = date.today,
        verbose_name = 'Integration Date',
        help_text = "Date when the donor is integrated into Vifac"
    )

    state = models.CharField(
        choices = State,
        default = '',
        max_length = 256,
        verbose_name = "State"
    )

    city = models.CharField(
        max_length = 256,
        default = '',
        verbose_name = "City"
    )
    
    street = models.CharField(
        max_length = 256,
        default = '',
        verbose_name = "Street"
    )
    
    number = models.CharField(
        max_length = 8,
        default = '',
        verbose_name= "Number"
    )
    
    reference =  models.CharField(
        max_length = 256,
        default = '',
        verbose_name = "Reference",
        help_text = "Whoever introduced the donor to Vifac"
    )

    contact_name = models.CharField(
        max_length = 512,
        default = '',
        verbose_name = 'Contact Name',
        help_text = "Contact's name"
    )

    contact_email = models.EmailField(
        max_length = 256,
        blank = True,
        help_text = "Contact's Email"
    )
    
    contact_phone_number = PhoneNumberField()

    contact_birthday = models.DateField(
        blank = True
    )
    
    contact_anniversary = models.DateField(
        blank = True
    )


    def __str__(self) -> str:
        return '%s' % (self.full_name)

    class Meta(object):
        verbose_name = 'donor'
        verbose_name_plural = 'donors'

