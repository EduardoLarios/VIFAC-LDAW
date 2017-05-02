from .models.laboratorios import Laboratorio, Ultrasonido
from .models.expediente import Exp_Medico
from .models.registro import Registro
from .models.problemas import Problemas
from django.db.models import QuerySet
from django.test import TestCase
import datetime

# Create your tests here.

class LaboratorioTest(TestCase):
    def setUp(self):
        date = datetime.date.today()
        paciente = Exp_Medico.objects.create(
            nombre = "Test 1",
            tipo_sanguineo = "o+",
            edad = "20",
            fecha_nacimiento = "1996-04-08"
        )
        Laboratorio.objects.create(
            date = date,
            result = "Result test",
            paciente = paciente
        )


    def test_laboratorio_can_be_viewed(self):
        labs = Laboratorio.objects.all()
        self.assertIsInstance(labs, QuerySet)


    def test_Laboratorio_can_be_edited(self):
        Laboratorio_1 = Laboratorio.objects.get(result = 'Result test')
        Laboratorio_1.result = 'Test Result'
        self.assertEqual(Laboratorio_1.result, 'Test Result')


    def test_Laboratorio_be_created(self):
        Laboratorio.objects.create(date = '2017-05-02', result = 'Prueba 1')
        Laboratorio_counts = Laboratorio.objects.filter(result = 'Prueba 1').count()
        self.assertEqual(Laboratorio_counts, 1)

    def test_Laboratorio_can_be_deleted(self):
        Laboratorio_1 = Laboratorio.objects.get(result = 'Result test')
        Laboratorio_1.delete()
        Laboratorio_counts = Laboratorio.objects.filter(result = 'Result test').count()
        self.assertEqual(Laboratorio_counts, 0)

class UltrasonidoTest(TestCase):
    def setUp(self):
        date = datetime.date.today()
        paciente = Exp_Medico.objects.create(
            nombre = "Test 1",
            tipo_sanguineo = "o+",
            edad = "20",
            fecha_nacimiento = "1996-04-08"
        )
        Ultrasonido.objects.create(
            date = date,
            result = "Result test",
            paciente = paciente
        )

    def test_Ultrasonido_can_be_viewed(self):
        us = Ultrasonido.objects.all()
        self.assertIsInstance(us, QuerySet)

    def test_Ultrasonido_can_be_edited(self):
        Ultrasonido_1 = Ultrasonido.objects.get(result = 'Result test')
        Ultrasonido_1.result = 'Test Result'
        self.assertEqual(Ultrasonido_1.result, 'Test Result')

    def test_Ultrasonido_be_created(self):
        Ultrasonido.objects.create(date = '2017-05-02', result = 'Prueba 1')
        Ultrasonido_counts = Ultrasonido.objects.filter(result = 'Prueba 1').count()
        self.assertEqual(Ultrasonido_counts, 1)

    def test_Ultrasonido_can_be_deleted(self):
        Ultrasonido_1 = Ultrasonido.objects.get(result = 'Result test')
        Ultrasonido_1.delete()
        Ultrasonido_counts = Ultrasonido.objects.filter(result = 'Result test').count()
        self.assertEqual(Ultrasonido_counts, 0)

class ProblemasTest(TestCase):
    def setUp(self):
        date = datetime.date.today()
        paciente = Exp_Medico.objects.create(
            nombre = "Test 1",
            tipo_sanguineo = "o+",
            edad = "20",
            fecha_nacimiento = "1996-04-08"
        )
        Problemas.objects.create(
            descripcion = "Result test",
            medicamento = 'Test medicamento',
            paciente = paciente
        )

    def test_Problemas_can_be_viewed(self):
        problemas = Problemas.objects.all()
        self.assertIsInstance(problemas, QuerySet)

    def test_Problemas_can_be_edited(self):
        Problemas_1 = Problemas.objects.get(descripcion = 'Result test')
        Problemas_1.descripcion = 'Test Result'
        self.assertEqual(Problemas_1.descripcion, 'Test Result')

    def test_Problemas_be_created(self):
        Problemas.objects.create(descripcion = 'Prueba 1', medicamento = "medicamento")
        Problemas_counts = Problemas.objects.filter(descripcion = 'Prueba 1').count()
        self.assertEqual(Problemas_counts, 1)

    def test_Problemas_can_be_deleted(self):
        Problemas_1 = Problemas.objects.get(descripcion = 'Result test')
        Problemas_1.delete()
        Problemas_counts = Problemas.objects.filter(descripcion = 'Result test').count()
        self.assertEqual(Problemas_counts, 0)


class RegistroTest(TestCase):
    def setUp(self):
        date = datetime.date.today()
        paciente = Exp_Medico.objects.create(
            nombre = "Test 1",
            tipo_sanguineo = "o+",
            edad = "20",
            fecha_nacimiento = "1996-04-08"
        )
        Registro.objects.create(
            date = date,
            sdg = 'Test sdg',
            ta = 'Test ta',
            weight = 60,
            paciente = paciente
        )

    def test_Registro_can_be_viewed(self):
        registros = Registro.objects.all()
        self.assertIsInstance(registros, QuerySet)

    def test_Registro_can_be_edited(self):
        Registro_1 = Registro.objects.get(sdg = 'Test sdg')
        Registro_1.sdg = 'Test Result'
        self.assertEqual(Registro_1.sdg, 'Test Result')

    def test_Registro_be_created(self):
        Registro.objects.create(date = '2017-05-02', sdg = 'Prueba 1', weight = 50)
        Registro_counts = Registro.objects.filter(sdg = 'Prueba 1').count()
        self.assertEqual(Registro_counts, 1)

    def test_Registro_can_be_deleted(self):
        Registro_1 = Registro.objects.get(sdg = 'Test sdg')
        Registro_1.delete()
        Registro_counts = Registro.objects.filter(sdg = 'Test sdg').count()
        self.assertEqual(Registro_counts, 0)

class ExpedienteTest(TestCase):
    def setUp(self):
        date = datetime.date.today()
        Exp_Medico.objects.create(
            nombre = "Test 1",
            tipo_sanguineo = "o+",
            edad = "20",
            fecha_nacimiento = "1996-04-08"
        )

    def test_Exp_Medico_can_be_viewed(self):
        exp = Exp_Medico.objects.all()
        self.assertIsInstance(exp, QuerySet)

    def test_Exp_Medico_can_be_edited(self):
        Exp_Medico_1 = Exp_Medico.objects.get(nombre = 'Test 1')
        Exp_Medico_1.nombre = 'Test Result'
        self.assertEqual(Exp_Medico_1.nombre, 'Test Result')

    def test_Exp_Medico_be_created(self):
        Exp_Medico.objects.create(nombre = "Test 2", tipo_sanguineo = "a+", edad = "50", fecha_nacimiento = "1996-04-08")
        Exp_Medico_counts = Exp_Medico.objects.filter(nombre = 'Test 2').count()
        self.assertEqual(Exp_Medico_counts, 1)

    def test_Exp_Medico_can_be_deleted(self):
        Exp_Medico_1 = Exp_Medico.objects.get(nombre = "Test 1")
        Exp_Medico_1.delete()
        Exp_Medico_counts = Exp_Medico.objects.filter(nombre = "Test 1").count()
        self.assertEqual(Exp_Medico_counts, 0)