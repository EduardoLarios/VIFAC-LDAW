from .models import Panfleta, Participante
from django.db.models import QuerySet
from django.test import TestCase


# This file contains all tests for 'donations' app
# Automatized tests for categories model

class PanfletaTest(TestCase):

    def setUp(self):
        part = Participante.objects.create(
            full_name='Tester',
            phone_number='4611234567'
        )

        Panfleta.objects.create(
            folio='T1',
            participante=part
        )


    def test_panfleta_can_be_viewed(self):
        panfletas = Panfleta.objects.all()
        self.assertIsInstance(panfletas, QuerySet)

        # Tests if a category can be edited

    def test_panfleta_can_be_edited(self):
        panf1 = Panfleta.objects.get(folio='T1')
        panf1.folio = 'T2'
        self.assertEqual(panf1.folio, 'T2')


    def test_panfleta_can_be_deleted(self):
        panf1 = Panfleta.objects.get(folio='T1')
        panf1.delete()
        panf_counts = Panfleta.objects.filter(folio='T1').count()
        self.assertEqual(panf_counts, 0)


    def test_panfleta_be_created(self):
        part = Participante.objects.create(
            full_name='Tester',
            phone_number='4611234567'
        )
        Panfleta.objects.create(folio='T2', participante=part)
        panf_counts = Panfleta.objects.filter(folio='T2').count()
        self.assertEqual(panf_counts, 1)


# Automatized tests for donors model

class ParticipanteTest(TestCase):

    def setUp(self):
        Participante.objects.create(
            full_name='Participante 1',
            phone_number='+524426884356'
        )

        # Tests if a donors' queryset can be retrieved

    def test_participante_can_be_viewed(self):
        part = Participante.objects.all()
        self.assertIsInstance(part, QuerySet)

        # Tests if a donor can be edited

    def test_participante_can_be_edited(self):
        part = Participante.objects.get(full_name='Participante 1')
        part.full_name = 'Participante 2'
        self.assertEqual(part.full_name, 'Participante 2')

        # Tests if a donor can be deleted

    def test_participante_can_be_deleted(self):
        part = Participante.objects.get(full_name='Participante 1')
        part.delete()
        part_counts = Participante.objects.filter(full_name='Participante 1').count()
        self.assertEqual(part_counts, 0)

        # Tests if a new donor can be created

    def test_participante_can_be_created(self):
        Participante.objects.create(
            full_name='Nombre Completo',
            phone_number='+524426884356',
        )
        part_counts = Participante.objects.filter(full_name='Nombre Completo').count()
        self.assertEqual(part_counts, 1)
