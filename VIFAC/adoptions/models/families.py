# -*- coding: utf-8 -*-
from django.db import models
from datetime import *

Status = (
	('Vivos', 'Vivos'),
	('Muertos', 'Muertos'),
	('Adopcion', 'Adopcion'),
)

class Family(models.Model):
	
	nombreFam = models.CharField(
		max_length=200,
		null=False,
		blank=False,
		default=' ',
	)
	
	Aniversario = models.DateField(
		default=date.today
	)
	
	fRegistro = models.DateField(
		default=date.today
	)
	
	actaMatrimonioCivil=models.BooleanField(
		default=False
	)
	
	actaMatrimonioReligioso = models.BooleanField(
		default=False
	)
	
	estudioSC = models.BooleanField(
		default= False,
		help_text= 'Estudio socioeconomico'
	)
	
	comprobanteDom = models.BooleanField(
		default=False,
		help_text='Comprobante de Domicilio'
	)
	
	comprobanteResidencia = models.BooleanField(
		default=False,
	)
	
	cartasRecomendacion = models.PositiveIntegerField(
		default=0
	)
	
	cartasRecomendacionSacerdotal = models.PositiveIntegerField(
		default=0
	)
	
	cartaAbuelosPaternos = models.BooleanField(
		default=False,
	)
	
	cartaAbuelosMaternos = models.BooleanField(
		default=False,
	)
	
	estudioPsi = models.BooleanField(
		default=False,
		help_text='Estudio psicologa'
	)
	
	certificadoIdoneidad = models.BooleanField(
		default=False,
	)
	
	fotosFamiliares = models.PositiveIntegerField(
		default=0,
	)
	
	cartaDIF = models.BooleanField(
		default=False,
	)
	
	cursoPadres = models.BooleanField(
		default=False,
	)

	status = models.CharField(
		max_length=100,
		choices=Status,
		default='Vivos'
	)
	
	motivoBaja = models.CharField(
		max_length=1000,
		default=' ',
	)
	
	fBaja = models.DateField(
		default=date.today,
		help_text='Fecha que paso de Vivos a Muertos'
	)
	
	nombreMamaBio = models.CharField(
		max_length=1000,
		default='Nombre de la mama que dio en adopcion',
	)
	
	fAdopcion = models.DateField(
		default=date.today,
		help_text='Fecha que paso de Vivos a Adopcion'
	)
	
	def __str__(self):
		return self.nombreFam