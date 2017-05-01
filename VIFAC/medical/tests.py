from django.test import TestCase

# Create your tests here.

class LaboratorioTest(TestCase):
    def setUp(self):
        date = datetime.date.today()
        paciente = Donor.objects.create(
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

        # Tests if a a categories' queryset can be retrieved

    def test_laboratorio_can_be_viewed(self):
        categories = Laboratorio.objects.all()
        self.assertIsInstance(categories, QuerySet)

        # Tests if a Laboratorio can be edited

    def test_Laboratorio_can_be_edited(self):
        Laboratorio_1 = Laboratorio.objects.get(name = 'Categoria 1')
        Laboratorio_1.name = 'Categoria Editada'
        self.assertEqual(Laboratorio_1.name, 'Categoria Editada')

        # Tests if a Laboratorio can be deleted

    def test_Laboratorio_can_be_deleted(self):
        Laboratorio_1 = Laboratorio.objects.get(name = 'Categoria 1')
        Laboratorio_1.delete()
        Laboratorio_counts = Laboratorio.objects.filter(name = 'Categoria 1').count()
        self.assertEqual(Laboratorio_counts, 0)

        # Tests if a new Laboratorio can be created

    def test_Laboratorio_be_created(self):
        Laboratorio.objects.create(name = 'Prueba 1', description = 'Prueba 1')
        Laboratorio_counts = Laboratorio.objects.filter(name = 'Prueba 1').count()
        self.assertEqual(Laboratorio_counts, 1)


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
