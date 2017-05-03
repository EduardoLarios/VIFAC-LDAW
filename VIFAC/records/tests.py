from .models import Expediente, Documento
from django.db.models import QuerySet
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse


class ExpedienteTests(TestCase):
    def setUp(self):
        Expediente.objects.create(
            nombre='Test 1',
            apellido_paterno='Test 1',
            apellido_materno='Test 1',
            edad=1,
            estado_nacimiento='Oaxaca',
            fecha_nacimiento='2000-01-01'
        )
        Expediente.objects.create(
            nombre='Test 2',
            apellido_paterno='Test 2',
            apellido_materno='Test 2',
            edad=1,
            estado_nacimiento='Oaxaca',
            fecha_nacimiento='2000-01-01'
        )
        
        # Tests if a a categories' queryset can be retrieved
    
    def test_expediente_puede_listarse(self):
        expedientes = Expediente.objects.all()
        self.assertIsInstance(expedientes, QuerySet)
            
    def test_expediente_can_be_edited(self):
        category_1 = Expediente.objects.get(nombre='Test 1')
        category_1.name = 'Expediente Editado'
        self.assertEqual(category_1.name, 'Expediente Editado')
        
        # Tests if a category can be deleted
    
    def test_expediente_can_be_deleted(self):
        expediente_1 = Expediente.objects.get(nombre='Test 1')
        expediente_1.delete()
        expediente_count = Expediente.objects.filter(nombre='Test 1').count()
        self.assertEqual(expediente_count, 0)
        
        # Tests if a new category can be created
    
    def test_expediente_be_created(self):
        Expediente.objects.create(
            nombre='Prueba 1',
            apellido_paterno='Prueba 1',
            apellido_materno='Prueba 1',
            edad=1,
            estado_nacimiento='Oaxaca',
            fecha_nacimiento='2000-01-01'
        )
        expediente_counts = Expediente.objects.filter(nombre='Prueba 1').count()
        self.assertEqual(expediente_counts, 1)
        
    def test_expediente_sin_nombre(self):
        try:
            Expediente.objects.create(
                apellido_paterno='Prueba 2',
                apellido_materno='Prueba 1',
                estado_nacimiento='Oaxaca',
                edad=21,
                fecha_nacimiento='2000-01-01'
            )
        except Exception as e:
            return True
        
        else:
            return False

    def test_expediente_sin_edad(self):
        try:
            Expediente.objects.create(
                nombre='Prueba 3',
                apellido_paterno='Prueba 3',
                apellido_materno='Prueba 3',
                estado_nacimiento='Oaxaca',
                fecha_nacimiento='2000-01-01'
            )
        except Exception as e:
            return True

        else:
            return False

    def test_expediente_sin_apellidos(self):
        try:
            Expediente.objects.create(
                nombre='Prueba 3',
                estado_nacimiento='Oaxaca',
                edad=21,
                fecha_nacimiento='2000-01-01'
            )
        except Exception as e:
            return True

        else:
            return False

    def test_expediente_lista_expediente(self):
        expedientes = Expediente.objects.all()
        self.assertIsInstance(expedientes, QuerySet)

    def test_expediente_editar_expediente(self):
        category_1 = Expediente.objects.get(nombre = 'Test 1')
        category_1.name = 'Expediente Editado'
        self.assertEqual(category_1.name, 'Expediente Editado')
    
        # Tests if a category can be deleted

    def test_expediente_borrar_expediente(self):
        expediente_1 = Expediente.objects.get(nombre = 'Test 1')
        expediente_1.delete()
        expediente_count = Expediente.objects.filter(nombre = 'Test 1').count()
        self.assertEqual(expediente_count, 0)
    
        # Tests if a new category can be created

    def test_expediente_crear_expediente(self):
        Expediente.objects.create(
            nombre = 'Prueba 5',
            apellido_paterno = 'Prueba 5',
            apellido_materno = 'Prueba 5',
            edad = 1,
            estado_nacimiento = 'Oaxaca',
            fecha_nacimiento = '2000-01-01'
        )
        expediente_counts = Expediente.objects.filter(nombre = 'Prueba 5').count()
        self.assertEqual(expediente_counts, 1)

    def test_expediente_incompleto(self):
        try:
            Expediente.objects.create(
                apellido_paterno = 'Prueba 2',
                apellido_materno = 'Prueba 1',
                estado_nacimiento = 'Oaxaca',
                edad = 21,
                fecha_nacimiento = '2000-01-01'
            )
        except Exception as e:
            return True
    
        else:
            return False

    def test_expediente_incompleto_edad(self):
        try:
            Expediente.objects.create(
                nombre = 'Prueba 3',
                apellido_paterno = 'Prueba 3',
                apellido_materno = 'Prueba 3',
                estado_nacimiento = 'Oaxaca',
                fecha_nacimiento = '2000-01-01'
            )
        except Exception as e:
            return True
    
        else:
            return False

    def test_expediente_incompleto_apellidos(self):
        try:
            Expediente.objects.create(
                nombre = 'Prueba 3',
                estado_nacimiento = 'Oaxaca',
                edad = 21,
                fecha_nacimiento = '2000-01-01'
            )
        except Exception as e:
            return True
    
        else:
            return False

    def test_expediente_lista_general(self):
        expedientes = Expediente.objects.all()
        self.assertIsInstance(expedientes, QuerySet)

    def test_expediente_editar_general(self):
        category_1 = Expediente.objects.get(nombre = 'Test 1')
        category_1.name = 'Expediente Editado'
        self.assertEqual(category_1.name, 'Expediente Editado')
    
        # Tests if a category can be deleted

    def test_expediente_borrar_general(self):
        expediente_1 = Expediente.objects.get(nombre = 'Test 1')
        expediente_1.delete()
        expediente_count = Expediente.objects.filter(nombre = 'Test 1').count()
        self.assertEqual(expediente_count, 0)
    
        # Tests if a new category can be created

    def test_expediente_crear_general(self):
        Expediente.objects.create(
            nombre = 'Prueba 1',
            apellido_paterno = 'Prueba 1',
            apellido_materno = 'Prueba 1',
            edad = 1,
            estado_nacimiento = 'Oaxaca',
            fecha_nacimiento = '2000-01-01'
        )
        expediente_counts = Expediente.objects.filter(nombre = 'Prueba 1').count()
        self.assertEqual(expediente_counts, 1)

    def test_expediente_general(self):
        try:
            Expediente.objects.create(
                apellido_paterno = 'Prueba 2',
                apellido_materno = 'Prueba 1',
                estado_nacimiento = 'Oaxaca',
                edad = 21,
                fecha_nacimiento = '2000-01-01'
            )
        except Exception as e:
            return True
    
        else:
            return False

    def test_expediente_incompleto_general(self):
        try:
            Expediente.objects.create(
                nombre = 'Prueba 3',
                apellido_paterno = 'Prueba 3',
                apellido_materno = 'Prueba 3',
                estado_nacimiento = 'Oaxaca',
                fecha_nacimiento = '2000-01-01'
            )
        except Exception as e:
            return True
    
        else:
            return False

    def test_expediente_incompleto_general_2(self):
        try:
            Expediente.objects.create(
                nombre = 'Prueba 3',
                estado_nacimiento = 'Oaxaca',
                edad = 21,
                fecha_nacimiento = '2000-01-01'
            )
        except Exception as e:
            return True
    
        else:
            return False
        
class DocumentosTest(TestCase):
    def test_upload_ejemplo(self):
        exp = Expediente.objects.create(
                pk='1',
                nombre='Prueba 4',
                apellido_paterno='Prueba 3',
                apellido_materno='Prueba 3',
                edad=21,
                estado_nacimiento='Oaxaca',
                fecha_nacimiento='2000-01-01'
        )
        with open('/home/esteban/Documentos/Github/VIFAC-LDAW/VIFAC/records/wishlist.doc') as fp:
            self.client.post('expedientes/subir_documento/1', {'document': fp, 'descripcion':'ejemplo', 'expediente': exp})
            
    def test_documento_existe(self):
        exp = Expediente.objects.create(
                pk='1',
                nombre='Prueba 4',
                apellido_paterno='Prueba 3',
                apellido_materno='Prueba 3',
                edad=21,
                estado_nacimiento='Oaxaca',
                fecha_nacimiento='2000-01-01'
        )
        Documento.objects.create(
            descripcion='Prueba 1',
            document='archivo.txt',
            expediente=exp,
        )
        documento_count = Documento.objects.filter(descripcion='Prueba 1').count()
        self.assertEqual(documento_count, 1)

    def test_delete_documento(self):
        exp = Expediente.objects.create(
                nombre='Prueba 4',
                apellido_paterno='Prueba 3',
                apellido_materno='Prueba 3',
                edad=21,
                estado_nacimiento='Oaxaca',
                fecha_nacimiento='2000-01-01'
        )
        Documento.objects.create(
            descripcion='Prueba 4',
            document='archivo.txt',
            expediente=exp,
        )
        documento = Documento.objects.get(descripcion='Prueba 4')
        documento.delete()
        documento_count = Documento.objects.filter(descripcion='Prueba 4').count()
        self.assertEqual(documento_count, 0)
        
    def test_lista_documentos(self):
        exp = Expediente.objects.create(
                nombre='Prueba 5',
                apellido_paterno='Prueba 3',
                apellido_materno='Prueba 3',
                edad=21,
                estado_nacimiento='Oaxaca',
                fecha_nacimiento='2000-01-01'
        )
        Documento.objects.create(
            descripcion='Prueba 5',
            document='archivo.txt',
            expediente=exp,
        )
        documentos = Documento.objects.all()
        self.assertIsInstance(documentos, QuerySet)
