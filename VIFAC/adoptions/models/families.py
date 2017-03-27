# -*- coding: utf-8 -*-
from django.db import models

Status = (
	(0, 'Vivos'),
	(1, 'Muertos'),
	(2, 'Stand By'),
)

class Family(models.Model):
	
	nombreFam = models.CharField(
		max_length=200,
		null=False,
		blank=False,
		default=' ',
	)
	
	fRegistro = models.DateField(
		auto_now = True,
	)
	
	estudioSC = models.BooleanField(
		default= False,
		help_text= 'Estudio socioeconomico'
	)
	
	estudioPsi = models.BooleanField(
		default=False,
		help_text='Estudio psicologa'
	)
	
	cartaDIF = models.BooleanField(
		default=False,
	)
	
	comprobanteDom = models.BooleanField(
		default=False,
		help_text='Comprobante de Domicilio'
	)
	
	status = models.PositiveIntegerField(
		choices=Status,
		default=0
	)
	
	motivoBaja = models.CharField(
		max_length=1000,
		default='',
	)
	
	fBaja = models.DateField(
		auto_now=True,
		help_text='Fecha que paso de Vivos a Muertos'
	)
	
	def __str__(self):
		return self.nombreFam