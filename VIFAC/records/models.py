from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import *

# Modelo Archivos

class Archivo(Model):
    nombre = CharField(
        max_length = 128,
        null = False,
        blank = False,
        verbose_name = 'Nombre del archivo'
    )
    
    file = FileField(
        upload_to = '/archivos/registros',
        blank = False,
        max_length = 512
    )
    
    fecha_subida = DateTimeField(
        auto_now_add = True
    )
    
    class Meta(object):
        verbose_name = 'archivo'
        verbose_name_plural = 'archivos'

State = (
    ('Ninguno', 'Ninguno'),
    ('Aguascalientes', 'Aguascalientes'),
    ('Baja California', 'Baja California'),
    ('Baja California Sur', 'Baja California Sur'),
    ('Campeche', 'Campeche'),
    ('Chiapas', 'Chiapas'),
    ('Chihuahua', 'Chihuahua'),
    ('CDMX', 'Ciudad de México'),
    ('Coahuila', 'Coahuila'),
    ('Colima', 'Colima'),
    ('Durango', 'Durango'),
    ('Guanajuato','Guanajuato'),
    ('Guerrero', 'Guerrero'),
    ('Hidalgo', 'Hidalgo'),
    ('Jalisco', 'Jalisco'),
    ('Estado de México', 'Estado de México'),
    ('Michoacán', 'Michoacán'),
    ('Morelos', 'Morelos'),
    ('Nayarit', 'Nayarit'),
    ('Nuevo León', 'Nuevo León'),
    ('Oaxaca', 'Oaxaca'),
    ('Puebla', 'Puebla'),
    ('Querétaro', 'Querétaro'),
    ('Quintana Roo', 'Quintana Roo'),
    ('San Luis Potosí', 'San Luis Potosí'),
    ('Sinaloa', 'Sinaloa'),
    ('Sonora', 'Sonora'),
    ('Tabasco', 'Tabasco'),
    ('Tamaulipas', 'Tamaulipas'),
    ('Tlaxcala', 'Tlaxcala'),
    ('Veracruz', 'Veracruz'),
    ('Yucatán', 'Yucatán'),
    ('Zacatecas', 'Zacatecas')
)

Relacion_Vives = (
    ('Padre', 'Padre'),
    ('Madre', 'Madre'),
    ('Hermano', 'Hermano'),
    ('Primo', 'Primo'),
    ('Tío', 'Tío'),
    ('Abuelo', 'Abuelo'),
    ('Amigo', 'Amigo'),
    ('Otro', 'Otro')
)

Estado_Civil = (
    ('Soltera', 'Soltera'),
    ('Casada', 'Casada'),
    ('Divorciada', 'Divorciada'),
    ('Viuda', 'Viuda'),
    ('Unión Libre', 'Unión Libre'),
)

Referencia = (
    ('Amistad', 'Amistad'),
    ('Periodico', 'Periodico'),
    ('Familiar', 'Familiar'),
    ('Trabajo', 'Trabajo'),
    ('Volante', 'Volante'),
    ('Sopt TV', 'Sopt TV'),
    ('Página web', 'Página web'),
    ('Migración', 'Migración')
)

class Expediente(Model):
    #Datos Generales
    nombre = CharField(
        max_length=256,
        verbose_name='Nombre',
        help_text='Nombre'
    )
    
    apellido_paterno = CharField(
        max_length=256,
        verbose_name='Apellido Paterno',
        help_text='Apellido Paterno'
    )
    
    apellido_materno = CharField(
        max_length=256,
        verbose_name='Apellido Materno',
        help_text='Apellido Materno'
    )
    
    edad = IntegerField(
        blank=True,
        verbose_name='Edad',
        help_text='Edad'
    )
    
    telefono_casa = CharField(
        max_length=8,
        default='',
        blank=True,
        verbose_name= "Telefono de casa",
        help_text='Telefono de casa'
    )
    
    telefono_particular = CharField(
        max_length = 8,
        default = '',
        blank= True,
        verbose_name= "Telefono particular",
        help_text='Telefono de particular'
    )
    
    fecha_nacimiento = DateField(
        blank = True
    )
    
    estado_civil =  CharField(
        max_length=128,
        choices=Estado_Civil,
        verbose_name='Estado Civil',
        help_text='Estado Civil'
    )
    
    migrante = BooleanField(
        default=False
    )

    estado = CharField(
        blank=True,
        choices=State,
        default='',
        max_length=256,
        verbose_name="Estado",
        help_text = 'Estado'
    )

    ciudad = CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Ciudad",
        help_text='Ciudad'
    )

    calle = CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Calle",
        help_text='Calle'
    )
    
    codigo_postal = CharField(
        blank=True,
        max_length = 8,
        default='',
        verbose_name='Codigo Postal',
        help_text='Codigo Postal'
    )
    
    #Historia Familiar
    
    vives_nombre = CharField(
        max_length=256,
        verbose_name='Nombre',
        help_text='Nombre'
    )
    
    vives_apellido_paterno = CharField(
        max_length=256,
        verbose_name='Apellido Paterno',
        help_text='Apellido Paterno'
    )

    vives_apellido_materno = CharField(
        max_length=256,
        verbose_name='Apellido Materno',
        help_text='Apellido Materno'
    )
    
    tipo_relacion_vives = CharField(
        max_length=128,
        blank=True,
        choices=Relacion_Vives,
        default='',
        verbose_name='Con quien vives',
        help_text='Con quien vives'
    )
    
    telefono_vives = CharField(
        max_length = 8,
        default = '',
        blank= True,
        verbose_name= "Telefono",
        help_text='Telefono de la persona con quien vives'
    )

    estado_vives = CharField(
        blank=True,
        choices=State,
        default='',
        max_length=256,
        verbose_name="Estado",
        help_text='Estado'
    )

    ciudad_vives = CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Ciudad",
        help_text='Ciudad'
    )

    calle_vives = CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Calle",
        help_text='Calle'
    )

    codigo_postal_vives = CharField(
        blank=True,
        max_length=128,
        default='',
        verbose_name='Codigo Postal',
        help_text='Codigo Postal'
    )
    
    #info padre
    
    vive_padre = BooleanField(
        default=True,
    )

    padre_nombre = CharField(
        default='',
        max_length=256,
        verbose_name='Nombre',
        help_text='Nombre'
    )

    padre_apellido_paterno = CharField(
        blank=True,
        max_length=256,
        verbose_name='Apellido Paterno',
        help_text='Apellido Paterno'
    )

    padre_apellido_materno = CharField(
        blank=True,
        max_length=256,
        verbose_name='Apellido Materno',
        help_text='Apellido Materno'
    )

    padre_telefono_casa = CharField(
        max_length=8,
        default='',
        blank=True,
        verbose_name="Telefono de casa",
        help_text='Telefono de casa'
    )

    padre_telefono_particular = CharField(
        max_length=8,
        default='',
        blank=True,
        verbose_name="Telefono particular",
        help_text='Telefono de particular'
    )

    padre_fecha_nacimiento = DateField(
        blank=True,
        null=True,
    )

    padre_estado_civil = CharField(
        blank=True,
        max_length=128,
        choices=Estado_Civil,
        verbose_name='Estado Civil',
        help_text='Estado Civil'
    )

    padre_estado = CharField(
        blank=True,
        choices=State,
        default='',
        max_length=256,
        verbose_name="Estado",
        help_text='Estado'
    )

    padre_ciudad = CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Ciudad",
        help_text='Ciudad'
    )

    padre_calle = CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Calle",
        help_text='Calle'
    )

    padre_codigo_postal = CharField(
        blank=True,
        max_length=128,
        default='',
        verbose_name='Codigo Postal',
        help_text='Codigo Postal'
    )
    
    #Info madre

    vive_madre = BooleanField(
        default=True
    )

    madre_nombre = CharField(
        max_length=256,
        default='',
        verbose_name='Nombre',
        help_text='Nombre'
    )

    madre_apellido_paterno = CharField(
        blank=True,
        max_length=256,
        verbose_name='Apellido Paterno',
        help_text='Apellido Paterno'
    )

    madre_apellido_materno = CharField(
        blank=True,
        max_length=256,
        verbose_name='Apellido Materno',
        help_text='Apellido Materno'
    )

    madre_telefono_casa = CharField(
        max_length=8,
        default='',
        blank=True,
        verbose_name="Telefono de casa",
        help_text='Telefono de casa'
    )

    madre_telefono_particular = CharField(
        max_length=8,
        default='',
        blank=True,
        verbose_name="Telefono particular",
        help_text='Telefono de particular'
    )

    madre_fecha_nacimiento = DateField(
        blank=True,
        null=True,
    )

    madre_estado_civil = CharField(
        blank=True,
        max_length=128,
        choices=Estado_Civil,
        verbose_name='Estado Civil',
        help_text='Estado Civil'
    )

    madre_migrante = BooleanField(
        default=False
    )

    madre_estado = CharField(
        blank=True,
        choices=State,
        default='',
        max_length=256,
        verbose_name="Estado",
        help_text='Estado'
    )

    madre_ciudad = CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Ciudad",
        help_text='Ciudad'
    )

    madre_calle = CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Calle",
        help_text='Calle'
    )

    madre_codigo_postal = CharField(
        blank=True,
        max_length=128,
        default='',
        verbose_name='Codigo Postal',
        help_text='Codigo Postal'
    )
    
    #formacion familia
    
    integrantes_familia = IntegerField(
        blank=True,
        default=0,
        verbose_name='Numero de integrantes',
        help_text='Numero de integrantes en la familia'
    )
    
    numero_hermanos = IntegerField(
        blank=True,
        default=0,
        verbose_name='Numero de hermanos',
        help_text='Numero de hermanos'
    )
    
    lugar_dentro_familia = CharField(
        max_length=128,
        blank=True,
        verbose_name='Lugar dentro de la familia',
        help_text='Lugar dentro de la familia'
    )
    
    #relacion con:
    
    relacion_padre = CharField(
        max_length=512,
        blank=True,
        verbose_name='Relación con tu padre',
        help_text='Relación con tu padre'
    )
    
    relacion_madre = CharField(
        max_length=512,
        blank=True,
        verbose_name='Relación con tu madre',
        help_text='Relación con tu madre'
    )
    
    relacion_hermanos = CharField(
        max_length=512,
        blank=True,
        verbose_name='Relación con tus hermanos',
        help_text='Relación con tus hermanos'
    )
    
    encargado_crianza = CharField(
        max_length=256,
        blank=True,
        verbose_name='Encargado de tu crianza',
        help_text='Encargado de tu crianza'
    )
    
    #ocupacion
    
    trabajado_antes = BooleanField(
        blank=True,
        default=False
    )
    
    puesto  = CharField(
        max_length=256,
        blank=True,
        verbose_name='Puesto de trabajo',
        help_text='Puesto'
    )
    
    lugar_trabajo = CharField(
        max_length=256,
        blank=True,
        verbose_name='Lugar trabajo',
        help_text='Lugar de trabajo'
    )
    
    jefe_inmediato = CharField(
        max_length=256,
        blank=True,
        default='',
        verbose_name='Jefe inmediato',
        help_text='Jefe inmediato'
    )
    
    telefono_jefe = CharField(
        max_length=24,
        blank=True,
        default=''
    )

    trabajo_estado = CharField(
        blank=True,
        choices=State,
        default='',
        max_length=256,
        verbose_name="Estado",
        help_text='Estado'
    )

    trabajo_ciudad = CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Ciudad",
        help_text='Ciudad'
    )

    trabajo_calle = CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Calle",
        help_text='Calle'
    )

    trabajo_codigo_postal = CharField(
        blank=True,
        max_length=128,
        default='',
        verbose_name='Codigo Postal',
        help_text='Codigo Postal'
    )
    
    # Como conociste vida y familia
    
    referencia =  CharField(
        blank=True,
        choices=Referencia,
        default='',
        max_length=256,
        verbose_name="Referencia",
        help_text='Cómo conoció VIFAC'
    )
    
    visto_en = CharField(
        max_length = 256,
        blank = True,
        default = '',
        verbose_name = 'Dónde se ha visto la referencia'
    )
    
    canal = CharField(
        max_length = 256,
        blank = True,
        default = '',
        verbose_name = 'Canal donde se ha visto la referencia'
    )
    
    otros = CharField(
        max_length = 256,
        blank = True,
        default = '',
        verbose_name = 'Otro medio donde se ha visto la referencia'
    )
    
    # Datos Generales de la Persona
    
    nombre_recomendacion = CharField(
        max_length = 64,
        blank = True,
        default = '',
        verbose_name = 'Nombre persona'
    )
    
    apellido_paterno_recomendacion = CharField(
        max_length = 64,
        blank = True,
        default = '',
        verbose_name = 'Apellido paterno'
    )
    
    apellido_materno_recomendacion = CharField(
        max_length = 64,
        blank = True,
        default = '',
        verbose_name = 'Apellido materno'
    )
    
    relacion_recomendacion = CharField(
        choices = Relacion_Vives,
        blank = True,
        default = '',
        verbose_name = 'Relación con la persona que recomienda'
    )
    
    telefono_recomendacion = PhoneNumberField()
    
    # Dirección
    
    calle_recomendacion = CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name='Calle',
        help_text='Calle'
    )
    
    numero_exterior = CharField(
        blank=True,
        max_length=8,
        default='',
        verbose_name ='Número',
        help_text ='Número'
    )
    
    codigo_postal_recomendacion = CharField(
        blank = True,
        max_length = 8,
        default = '',
        verbose_name = 'Codigo Postal',
        help_text='Codigo Postal'
    )
    
    colonia = CharField(
        max_length = 128,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Colonia'
    )
    
    ciudad_referencia = CharField(
        blank = True,
        max_length = 64,
        default = '',
        verbose_name = "Ciudad",
        help_text = 'Ciudad'
    )
    
    estado_referencia = CharField(
        blank = True,
        choices = State,
        default = '',
        verbose_name = "Estado",
        help_text = 'Estado'
    )
    
    # Situación Actual
    # Información General
    
    Ayuda = (
        ('Otro', 'Otro'),
        ('Interna', 'Interna'),
        ('Externa', 'Externa'),
    )
    
    tipo_de_ayuda = CharField(
        choices = Ayuda,
        blank = True,
        default = '',
        verbose_name = 'Tipo de ayuda'
    )
    
    fecha_ultima_menstruacion = DateField(
        auto_now = False,
        null = False,
        blank = True,
        default = None,
        verbose_name = 'Fecha de última menstruación'
    )
    
    fecha_de_parto_esperada = DateField(
        auto_now = False,
        null = False,
        blank = True,
        default = None,
        verbose_name = 'Fecha esperada de parto'
    )
    
    # Referencias
    # Contacto de Emergencia
    
    nombre_emergencia = CharField(
        blank = True,
        max_length = 64,
        default = '',
        verbose_name = 'Nombre',
        help_text = 'Nombre contacto de emergencia'
    )

    apellido_paterno_emergencia = CharField(
        max_length = 64,
        blank = True,
        default = '',
        verbose_name = 'Apellido paterno'
    )

    apellido_materno_emergencia = CharField(
        max_length = 64,
        blank = True,
        default = '',
        verbose_name = 'Apellido materno'
    )
    
    relacion_emergencia = CharField(
        choices = Relacion_Vives,
        blank = True,
        default = '',
        verbose_name = 'Relación con el contacto de emergencia'
    )
    
    telefono_emergencia = PhoneNumberField()
    
    codigo_postal_emergencia = CharField(
        blank = True,
        max_length = 8,
        default = '',
        verbose_name = 'Codigo Postal',
        help_text = 'Codigo Postal'
    )
    
    colonia_emergencia = CharField(
        max_length = 128,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Colonia'
    )
    
    ciudad_emergencia = CharField(
        blank = True,
        max_length = 64,
        default = '',
        verbose_name = "Ciudad",
        help_text = 'Ciudad'
    )
    
    estado_emergencia = CharField(
        blank = True,
        choices = State,
        default = '',
        verbose_name = "Estado",
        help_text = 'Estado'
    )
    
    # Referencia Médica
    
    control_medico = BooleanField(
        null = False,
        blank = True,
        default = False,
        verbose_name = 'Ha tenido control médico'
    )
    
    enfermedades_padecidas = CharField(
        max_length = 128,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Enfermedades Padecidas'
    )
    
    nombre_medico = CharField(
        max_length = 256,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Nombre del médico a cargo'
    )
    
    nombre_clinica = CharField(
        max_length = 256,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Nombre de la clínica'
    )
    
    telefono_medico = PhoneNumberField()
    
    calle_medico = CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Calle",
        help_text = 'Calle'
    )
    
    numero_exterior_medico = CharField(
        blank = True,
        max_length = 8,
        default = '',
        verbose_name = "Número de calle",
        help_text = 'Número de calle'
    )
    
    codigo_postal_medico = CharField(
        blank = True,
        max_length = 8,
        default = '',
        verbose_name = 'Codigo Postal',
        help_text = 'Codigo Postal'
    )
    
    colonia_medico = CharField(
        max_length = 128,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Colonia'
    )
    
    ciudad_medico = CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Ciudad",
        help_text = 'Ciudad'
    )
    
    estado_medico = CharField(
        blank = True,
        choices = State,
        default = '',
        verbose_name = "Estado",
        help_text = 'Estado'
    )
    
    # Personal
    
    estado_de_animo = CharField(
        max_length = 1024,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Estado de ánimo'
    )
    
    infancia = CharField(
        max_length = 1024,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Descripción infancia'
    )
    
    # Embarazo
    
    Embarazo = (
        ('Deseado', 'Deseado'),
        ('Planeado', 'Planeado'),
        ('Inesperado', 'Inesperado'),
        ('Rechazado', 'Rechazado'),
        ('Otro', 'Otro')
    )

    Voluntario = (
        ('Sí', 'Sí'),
        ('No', 'No'),
        ('No respondió', 'No respondió')
    )

    Relacion = (
        ('Casados por la Iglesia', 'Casados por la Iglesia'),
        ('Casador por el civil', 'Casador por el civil'),
        ('Aventura', 'Aventura'),
        ('Violación', 'Violación'),
        ('Noviazgo', 'Noviazgo'),
        ('Otro', 'Otro')
    )

    tipo_embarazo = CharField(
        choices = Embarazo,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Tipo de embarazo'
    )
    
    reaccion = CharField(
        max_length = 1024,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Reacción al embarazo'
    )
    
    apoyo_papa = CharField(
        max_length = 1024,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Apoyo del papá'
    )
    
    relacion_con_padre = CharField(
        choices = Relacion,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Relación con el padre'
    )
    
    duracion_relacion = CharField(
        max_length = 64,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Duración de la relación'
    )
    
    familiares = CharField(
        max_length = 512,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Familiares que saben del embarazo'
    )
    
    actitud_familiares = CharField(
        max_length = 512,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Actitud que espera de los familiares'
    )
    
    relacion_voluntaria = CharField(
        choices = Voluntario,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Relaciones voluntarias'
    )
    
    comunicacion_padre = BooleanField(
        null = False,
        blank = True,
        default = True,
        verbose_name = 'Comunicación con el padre'
    )
    
    aborto_considerado = BooleanField(
        null = False,
        blank = True,
        default = False,
        verbose_name = 'Se consideró el abortó'
    )
    
    violencia_intrafamiliar = BooleanField(
        null = False,
        blank = True,
        default = False,
        verbose_name = 'Violencia intrafamiliar'
    )
    
    # Escolaridad

    Estudios = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('6+', '6+'),
        ('Otro', 'Otro')
    )

    Duracion = (
        ('Sin Estudios', 'Sin Estudios'),
        ('Primaria', 'Primaria'),
        ('Secundaria', 'Secundaria'),
        ('Preparatoria', 'Preparatoria'),
        ('Técnico', 'Técnico'),
        ('Licenciatura', 'Licenciatura'),
        ('Postgrado', 'Postgrado'),
        ('Otro', 'Otro')
    )
    
    maximo_grado_estudios = CharField(
        choices = Estudios,
        null = False,
        blank = True,
        default = 'Otro',
        verbose_name = 'Máximo grado de estudios'
    )
    
    nombre_escuela = CharField(
        max_length = 128,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Nombre de la institución escolar'
    )

    tiempo_cursado = CharField(
        choices = Duracion,
        null = False,
        blank = True,
        default = 'Otro',
        verbose_name = 'Años cursados'
    )
    
    archivos = ManyToManyField(
        Archivo,
        related_name = 'expediente',
        related_query_name = 'expedientes',
        on_delete = PROTECT,
        verbose_name = 'Archivos adjuntos'
    )
    
    class Meta(object):
        verbose_name = 'expediente'
        verbose_name_plural = 'expedientes'
    
    
    
    
    
    
    
        
        
    
    
    
    
    
    
    
    
    
