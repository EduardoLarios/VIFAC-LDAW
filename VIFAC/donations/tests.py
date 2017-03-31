# -*- coding: UTF-8 -*-
from .models import Category, Donation, Donor
from django.db.models import QuerySet
from django.test import TestCase
import datetime

# This file contains all tests for 'donations' app
# Automatized tests for categories model

class CategoryTest(TestCase):
    def setUp(self):
        Category.objects.create(
            name = 'Categoria 1',
            description = 'Descripcion 1'
        )
        Category.objects.create(
            name = 'Categoria 2',
            description = 'Descripcion 2'
        )
        
        # Tests if a a categories' queryset can be retrieved
        
    def test_category_can_be_viewed(self):
        categories = Category.objects.all()
        self.assertIsInstance(categories, QuerySet)
        
        # Tests if a category can be edited
                              
    def test_category_can_be_edited(self):
        category_1 = Category.objects.get(name = 'Categoria 1')
        category_1.name = 'Categoria Editada'
        self.assertEqual(category_1.name, 'Categoria Editada')
        
        # Tests if a category can be deleted
        
    def test_category_can_be_deleted(self):
        category_1 = Category.objects.get(name = 'Categoria 1')
        category_1.delete()
        category_counts = Category.objects.filter(name = 'Categoria 1').count()
        self.assertEqual(category_counts, 0)
        
        # Tests if a new category can be created
        
    def test_category_be_created(self):
        Category.objects.create(name = 'Prueba 1', description = 'Prueba 1')
        category_counts = Category.objects.filter(name = 'Prueba 1').count()
        self.assertEqual(category_counts, 1)

# Automatized tests for donors model

class DonorTest(TestCase):
    def setUp(self):
        date = datetime.date.today()
        Donor.objects.create(
            full_name = 'Nombre Completo',
            integration_date = date,
            state = 'Guanajuato',
            city = 'Irapuato',
            street = 'Una calle',
            number = '105',
            reference = 'Una referencia',
            contact_name = 'Nombre de contacto',
            contact_email = 'correo@ejemplo.com',
            contact_phone_number = '+524426884356',
            contact_birthday = date,
            contact_anniversary = date
        )
        
        # Tests if a donors' queryset can be retrieved
        
    def test_donor_can_be_viewed(self):
        donors = Donor.objects.all()
        self.assertIsInstance(donors, QuerySet)
        
        # Tests if a donor can be edited
    
    def test_donor_can_be_edited(self):
        donor = Donor.objects.get(full_name = 'Nombre Completo')
        donor.full_name = 'Nombre Editado'
        self.assertEqual(donor.full_name, 'Nombre Editado')
        
        # Tests if a donor can be deleted
    
    def test_donor_can_be_deleted(self):
        donor = Donor.objects.get(full_name = 'Nombre Completo')
        donor.delete()
        donor_counts = Donor.objects.filter(full_name = 'Nombre Completo').count()
        self.assertEqual(donor_counts, 0)
    
        # Tests if a new donor can be created
        
    def test_donor_can_be_created(self):
        date = datetime.date.today()
        Donor.objects.create(
            full_name = 'Nombre Completo',
            integration_date = date,
            state = 'Guanajuato',
            city = 'Irapuato',
            street = 'Una calle',
            number = '105',
            reference = 'Una referencia',
            contact_name = 'Nombre de contacto',
            contact_email = 'correo@ejemplo.com',
            contact_phone_number = '+524426884356',
            contact_birthday = date,
            contact_anniversary = date
        )
        donor_counts = Donor.objects.filter(full_name = 'Nombre Completo').count()
        self.assertEqual(donor_counts, 2)

# Automatized tests for donations model

class DonationsTest(TestCase):
    def setUp(self):
        date = datetime.date.today()
        donor = Donor.objects.create(
            full_name = 'Nombre Completo',
            integration_date = date,
            state = 'Guanajuato',
            city = 'Irapuato',
            street = 'Una calle',
            number = '105',
            reference = 'Una referencia',
            contact_name = 'Nombre de contacto',
            contact_email = 'correo@ejemplo.com',
            contact_phone_number = '+524426884356',
            contact_birthday = date,
            contact_anniversary = date
        )

        category = Category.objects.create(
        name = 'Categoria 1',
        description = 'Descripcion 1'

        )
        
        Donation.objects.create(
            donor = donor,
            description = 'Descripcion',
            category = category
        )
        
        # Tests if a donations' queryset can be retrieved
    
    def test_donation_can_be_viewed(self):
        donations = Donation.objects.all()
        self.assertIsInstance(donations, QuerySet)
        
        # Tests if a donation can be edited
    
    def test_donation_can_be_edited(self):
        donation = Donation.objects.get(description = 'Descripcion')
        donation.description = 'Descripcion Editada'
        self.assertEqual(donation.description, 'Descripcion Editada')
        
        # Tests if a donation can be deleted
    
    def test_donation_can_be_deleted(self):
        donation = Donation.objects.get(description = 'Descripcion')
        donation.delete()
        donation_counts = Donation.objects.filter(description = 'Descripcion').count()
        self.assertEqual(donation_counts, 0)
                         
        # Tests if a new donation can be created
    
    def test_donation_be_created(self):
        date = datetime.date.today()
        donor = Donor.objects.create(
            full_name = 'Nombre Completo',
            integration_date = date,
            state = 'Guanajuato',
            city = 'Irapuato',
            street = 'Una calle',
            number = '105',
            reference = 'Una referencia',
            contact_name = 'Nombre de contacto',
            contact_email = 'correo@ejemplo.com',
            contact_phone_number = '+524426884356',
            contact_birthday = date,
            contact_anniversary = date
        )
    
        category = Category.objects.create(
            name = 'Categoria 1',
            description = 'Descripcion 1'
    
        )
        
        Donation.objects.create(donor = donor, description = 'Descripcion', category = category)
        donation_counts = Donation.objects.filter(description = 'Descripcion').count()
        self.assertEqual(donation_counts, 2)
