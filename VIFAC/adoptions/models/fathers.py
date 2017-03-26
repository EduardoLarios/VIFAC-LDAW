# -*- coding: utf-8 -*-
from django.db import models

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
	(11, 'Guanajuato'),
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


class Father(models.Model):
	nombre = models.CharField(
		max_length=256,
		null=False,
		blank=False,
		default=''
	)
	
	aPaterno = models.CharField(
		max_length=256,
		null=False,
		blank=False,
		default=''
	)
	
	aMaterno = models.CharField(
		max_length=256,
		null=False,
		blank=False,
		default=''
	)
	
	FNacimiento = models.DateField(
		null=False,
		blank=False
	)
	
	Estado = models.PositiveIntegerField(
		choices=State,
		default=0
	)
	
	Telefono = models.CharField(
		max_length=256,
		null=False,
		blank=False,
		default=''
	)

