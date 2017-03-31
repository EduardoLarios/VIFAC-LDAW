from django.test import TestCase
from .models import Escuela, Material
from django.db.models import QuerySet


class UserTestCase(TestCase):
    def setUp(self):
        Escuela.objects.create(name='test1', ciudad='test1', estado='test1')
        Escuela.objects.create(name='test2', ciudad='test2', estado='test2')
    
    def test_create_school(self):
        Escuela.objects.create(name='create', ciudad='test', estado='test')
        school_count = Escuela.objects.all().count()
        
        self.assertEqual(school_count, 3)
        
    def test_school_exists(self):
        school_counts = Escuela.objects.filter(name='test1').count()
        
        self.assertEqual(school_counts, 1)

    def test_delete_school(self):
        school = Escuela.objects.get(name='test2')
        school.delete()
        school_count = Escuela.objects.all().count()
        
        self.assertEqual(school_count, 1)
        
    def test_list_user(self):
        queryset =  Escuela.objects.all()
        
        self.assertIsInstance(queryset, QuerySet)
        
    def test_assign_material(self):
        school = Escuela.objects.get(name='test1')
        Material.objects.create(categoria='ejemplo', descripcion='ejemplo', entrego='ejemplo', escuela=school)
        material_count = Material.objects.all().count()
        
        self.assertEqual(material_count, 1)
        
    def test_list_material(self):
        school = Escuela.objects.get(name='test1')
        Material.objects.create(categoria='ejemplo', descripcion='ejemplo', entrego='ejemplo', escuela=school)
        queryset = Material.objects.all()
        
        self.assertIsInstance(queryset, QuerySet)
        
    def test_remove_material(self):
        school = Escuela.objects.get(name='test1')
        Material.objects.create(categoria='ejemplo', descripcion='ejemplo', entrego='ejemplo', escuela=school)
        material = Material.objects.get(escuela=school)
        material.delete()
        material_count = Material.objects.all().count()
        
        self.assertEqual(material_count, 0)
    
    def test_edit_school(self):
        school = Escuela.objects.get(name='test1')
        school.name = 'nuevo nombre'
        
        self.assertEqual(school.name, 'nuevo nombre')
        
    def test_edit_material(self):
        school = Escuela.objects.get(name='test1')
        Material.objects.create(categoria='ejemplo', descripcion='ejemplo', entrego='ejemplo', escuela=school)
        material = Material.objects.get(descripcion='ejemplo')
        material.descripcion = 'nueva descripcion'
        self.assertEqual(material.descripcion, 'nueva descripcion')