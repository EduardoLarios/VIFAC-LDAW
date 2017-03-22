# -*- coding: utf-8 -*-
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from datetime import *

__all__ = [ 'Donors', 'State' ]

State = (
    (0, 'Ninguno'),
    (1, 'Aguascalientes'),
    (2, 'Baja California'),
    (3, 'Baja California Sur'),
    (4, 'Campeche'),
    (5, 'Chiapas'),
    (6, 'Chihuahua'),
    (7, 'Ciudad de México'),
    (8, 'Coahuila de Zaragoza'),
    (9, 'Colima'),
    (10, 'Durango'),
    (11,'Guanajuato'),
    (12, 'Guerrero'),
    (13, 'Hidalgo'),
    (14, 'Jalisco'),
    (15, 'Estado de México'),
    (16, 'Michoacán de Ocampo'),
    (17, 'Morelos'),
    (18, 'Nayarit'),
    (19, 'Nuevo León'),
    (20, 'Oaxaca'),
    (21, 'Puebla'),
    (22, 'Querétaro de Arteaga'),
    (23, 'Quintana Roo'),
    (24, 'San Luis Potosí'),
    (25, 'Sinaloa'),
    (26, 'Sonora'),
    (27, 'Tabasco'),
    (28, 'Tamaulipas'),
    (29, 'Tlaxcala'),
    (30, 'Veracruz'),
    (31, 'Yucatán'),
    (32, 'Zacatecas')
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

    state = models.PositiveIntegerField(
        choices = State,
        default = 0,
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
        return '%s-%s,%s' % (self.full_name, self.state, self.city)

    class Meta(object):
        verbose_name = 'donor'
        verbose_name_plural = 'donors'

