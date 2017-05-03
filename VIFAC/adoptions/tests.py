# -*- coding: UTF-8 -*-
from django.test import TestCase
from .models import Family
from .models.members import Member
from django.db.models import QuerySet
import datetime

class FamilyTest(TestCase):
	#Crear Objeto
	def setUp(self):
		date = datetime.date.today()
		Family.objects.create(
			nombreFam = 'FamiliaPrueba',
			Aniversario = date,
			fRegistro = date,
			actaMatrimonioCivil = False,
			actaMatrimonioReligioso = False,
			estudioSC = False,
			comprobanteDom = False,
			comprobanteResidencia = False,
			cartasRecomendacion = 0,
			cartasRecomendacionSacerdotal = 0,
			cartaAbuelosPaternos = 0,
			cartaAbuelosMaternos = 0,
			estudioPsi = False,
			certificadoIdoneidad = False,
			fotosFamiliares = 0,
			cartaDIF = False,
			cursoPadres = False,
			status = 'Vivos',
			motivoBaja = ' ',
			fBaja = date,
			nombreMamaBio = 'MadreTest',
			fAdopcion = date
		)
		
		
		#CRUD FAMILY - CREATE
	def test_FamilyCreate(self):
		date = datetime.date.today()
		Family.objects.create(
			nombreFam = 'FamilyCreate',
			Aniversario = date)
		family_acum = Family.objects.filter(nombreFam = 'FamilyCreate').count()
		self.assertEqual(family_acum, 1)
		
		
		#CRUD FAMILY - READ
	def test_FamilyRead(self):
		families = Family.objects.all()
		self.assertIsInstance(families, QuerySet)
		
		
		#CRUD FAMILY - UPDATE
	def test_FamilyUpdate(self):
		family = Family.objects.get(nombreFam = 'FamiliaPrueba')
		family.nombreFam = 'FamiliaPruebaUpdate'
		self.assertEqual(family.nombreFam, 'FamiliaPruebaUpdate')
		
		
		#CRUD FAMILY - DELETE
	def test_FamilyDelete(self):
		family = Family.objects.get(nombreFam = 'FamiliaPrueba')
		family.delete()
		family_acum = Family.objects.filter(nombreFam='FamiliaPrueba').count()
		self.assertEqual(family_acum, 0)
		


class MemberTest(TestCase):
	#Crear Mama y Papa Familia
	date = datetime.date.today()
	
	Family.objects.create(
		nombreFam='FamiliaMember',
		Aniversario=date,
		fRegistro=date,
		actaMatrimonioCivil=False,
		actaMatrimonioReligioso=False,
		estudioSC=False,
		comprobanteDom=False,
		comprobanteResidencia=False,
		cartasRecomendacion=0,
		cartasRecomendacionSacerdotal=0,
		cartaAbuelosPaternos=0,
		cartaAbuelosMaternos=0,
		estudioPsi=False,
		certificadoIdoneidad=False,
		fotosFamiliares=0,
		cartaDIF=False,
		cursoPadres=False,
		status='Vivos',
		motivoBaja=' ',
		fBaja=date,
		nombreMamaBio='MadreTest',
		fAdopcion=date
	)
	
	family = Family.objects.get(nombreFam='FamiliaMember')
	
	Mom = Member.objects.create(
		familia = family,
		nombre = 'Maria',
		aPaterno = 'M',
		aMaterno = 'M',
		FNacimiento = date,
		Genero = 'Femenino'
	)
	
	Dad = Member.objects.create(
		familia=family,
		nombre='Juan',
		aPaterno='R',
		aMaterno='R',
		FNacimiento=date,
		Genero='Masculino'
	)
	
	
	# CRUD Mom - CREATE
	def test_MomCreate(self):
		date = datetime.date.today()
		Family.objects.create(
			nombreFam='FamilyCreate',
			Aniversario=date)
		
		family = Family.objects.get(nombreFam='FamilyCreate')
		
		Member.objects.create(
			familia=family,
			nombre='Maria',
			aPaterno='M',
			aMaterno='M',
			FNacimiento=date,
			Genero='Femenino'
		)
		Mom_acum = Member.objects.filter(familia=family, Genero='Femenino').count()
		self.assertEqual(Mom_acum, 1)
		
		
	# CRUD Dad - CREATE
	def test_DadCreate(self):
		date = datetime.date.today()
		Family.objects.create(
			nombreFam='FamilyCreate',
			Aniversario=date)
		
		family = Family.objects.get(nombreFam='FamilyCreate')
		
		Member.objects.create(
			familia=family,
			nombre='Juan',
			aPaterno='M',
			aMaterno='M',
			FNacimiento=date,
			Genero='Masculino'
		)
		Dad_acum = Member.objects.filter(familia=family, Genero='Masculino').count()
		self.assertEqual(Dad_acum, 1)
	
	
	# CRUD MomDad - READ
	def test_MomDadRead(self):
		members = Member.objects.all()
		self.assertIsInstance(members, QuerySet)
	
	
	# CRUD Mom - UPDATE
	def testMomUpdate(self):
		date = datetime.date.today()
		Family.objects.create(
			nombreFam='FamilyCreate',
			Aniversario=date)
		
		family = Family.objects.get(nombreFam='FamilyCreate')
		mom = Member.objects.create(
			familia=family,
			nombre='Maria',
			aPaterno='M',
			aMaterno='M',
			FNacimiento=date,
			Genero='Femenino'
		)
		mom.aPaterno='Ruiz'
		self.assertEqual(mom.aPaterno, 'Ruiz')

	
	# CRUD Dad - UPDATE
	def testDadUpdate(self):
		date = datetime.date.today()
		Family.objects.create(
			nombreFam='FamilyCreate',
			Aniversario=date)
		
		family = Family.objects.get(nombreFam='FamilyCreate')
		dad = Member.objects.create(
			familia=family,
			nombre='Juan',
			aPaterno='M',
			aMaterno='M',
			FNacimiento=date,
			Genero='Masculino'
		)
		dad.aPaterno = 'Juarez'
		self.assertEqual(dad.aPaterno, 'Juarez')
		
	# CRUD MomDad - DELETE
	def test_MemberDelete(self):
		date = datetime.date.today()
		Family.objects.create(
			nombreFam='FamilyCreate',
			Aniversario=date)
		
		family = Family.objects.get(nombreFam='FamilyCreate')
		
		Member.objects.create(
			familia=family,
			nombre='Juan',
			aPaterno='M',
			aMaterno='M',
			FNacimiento=date,
			Genero='Masculino'
		)
		
		Member.objects.create(
			familia=family,
			nombre='Maria',
			aPaterno='M',
			aMaterno='M',
			FNacimiento=date,
			Genero='Femenino'
		)
		
		family.delete()
		family_acum = Family.objects.filter(nombreFam='FamilyCreate').count()
		self.assertEqual(family_acum, 0)