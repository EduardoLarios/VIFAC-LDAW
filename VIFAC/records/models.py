#--*-- UTF -8 --*--
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


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
    ('Soltero', 'Soltero'),
    ('Casado', 'Casado'),
    ('Divorciado', 'Divorciado'),
    ('Viudo', 'Viudo'),
    ('Unión Libre', 'Unión Libre'),
)

Religiones = (
    ('Catolica', 'Catolica'),
    ('Cristiana', 'Cristiana'),
    ('Protestante', 'Protestante'),
    ('Ninguna', 'Ninguna'),
    ('Otra', 'Otra')
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

Ayuda = (
    ('Otro', 'Otro'),
    ('Interna', 'Interna'),
    ('Externa', 'Externa'),
)

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

Poblacion = (
    ('Rural', 'Rural'),
    ('Urbana', 'Urbana'),
    ('Indigena', 'Indigena')
)

Migrante = (
    ('No', 'No'),
    ('Si', 'Si')
)

Vive = (
    ('No sabe', 'No sabe'),
    ('No', 'No'),
    ('Si', 'Si')
)

Trabajado = (
    ('No', 'No'),
    ('Si', 'Si')
)

class Expediente(models.Model):
    #Datos Generales
    nombre = models.CharField(
        max_length = 256,
        verbose_name = 'Nombre',
        help_text = 'Nombre'
    )
    
    apellido_paterno = models.CharField(
        max_length = 256,
        verbose_name = 'Apellido Paterno',
        help_text = 'Apellido Paterno'
    )
    
    apellido_materno = models.CharField(
        max_length = 256,
        verbose_name = 'Apellido Materno',
        help_text = 'Apellido Materno'
    )
    
    edad = models.IntegerField(
        blank = True,
        verbose_name = 'Edad',
        help_text = 'Edad'
    )
    
    telefono_casa = models.CharField(
        max_length = 10,
        default = '',
        blank = True,
        verbose_name =  "Teléfono  de casa",
        help_text = 'Teléfono  de casa'
    )
    
    telefono_particular = models.CharField(
        max_length = 10,
        default = '',
        blank = True,
        verbose_name =  "Teléfono  particular",
        help_text = 'Teléfono  de particular'
    )
    
    estado_nacimiento = models.CharField(
        blank=True,
        choices=State,
        default='',
        max_length=256,
        verbose_name="Estado de nacimiento",
        help_text='Estado de nacimiento'
    )
    
    fecha_nacimiento = models.DateField(
        blank = True
    )
    
    estado_civil =  models.CharField(
        max_length = 128,
        choices = Estado_Civil,
        verbose_name = 'Estado Civil',
        help_text = 'Estado Civil'
    )
    
    religion = models.CharField(
        blank=True,
        default='',
        max_length=128,
        choices=Religiones,
        verbose_name='Religión',
        help_text='Religión'
    )
    
    tipo_poblacion = models.CharField(
        blank=True,
        default='',
        max_length=128,
        choices=Poblacion,
        verbose_name='Tipo de Población',
        help_text='Tipo de Población'
    )
    
    migrante = models.CharField(
        max_length=12,
        choices=Migrante,
        verbose_name='Migrante',
        help_text='Migrante'
    )

    estado = models.CharField(
        blank = True,
        choices = State,
        default = '',
        max_length = 256,
        verbose_name = "Estado",
        help_text = 'Estado'
    )

    ciudad = models.CharField(
        blank =  True,
        max_length = 256,
        default = '',
        verbose_name = "Ciudad",
        help_text = 'Ciudad'
    )

    calle = models.CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Calle",
        help_text = 'Calle'
    )
    
    colonia = models.CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Colonia",
        help_text='Colonia'
    )
    
    codigo_postal =  models.CharField(
        blank = True,
        max_length = 128,
        default = '',
        verbose_name = 'Código  Postal',
        help_text = 'Código  Postal'
    )
    
    #Historia Familiar
    
    vives_nombre = models.CharField(
        max_length = 256,
        verbose_name = 'Nombre',
        help_text = 'Nombre'
    )
    
    vives_apellido_paterno = models.CharField(
        max_length = 256,
        verbose_name = 'Apellido Paterno',
        help_text = 'Apellido Paterno'
    )

    vives_apellido_materno = models.CharField(
        max_length = 256,
        verbose_name = 'Apellido Materno',
        help_text = 'Apellido Materno'
    )
    
    tipo_relacion_vives = models.CharField(
        max_length = 128,
        blank = True,
        choices =  Relacion_Vives,
        default = '',
        verbose_name = 'Con quien vives',
        help_text = 'Con quien vives'
    )
    
    telefono_vives = models.CharField(
        max_length = 8,
        default = '',
        blank = True,
        verbose_name =  "Teléfono ",
        help_text = 'Teléfono  de la persona con quien vives'
    )

    estado_vives = models.CharField(
        blank = True,
        choices = State,
        default = '',
        max_length = 256,
        verbose_name = "Estado",
        help_text = 'Estado'
    )

    ciudad_vives = models.CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Ciudad",
        help_text = 'Ciudad'
    )

    calle_vives = models.CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Calle",
        help_text = 'Calle'
    )

    colonia_vives = models.CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Colonia Vives",
        help_text = 'Colonia'
    )
    
    codigo_postal_vives = models.CharField(
        blank = True,
        max_length = 128,
        default = '',
        verbose_name = 'Código Postal',
        help_text = 'Código Postal'
    )
    
    #info padre
    
    vive_padre = models.CharField(
        blank=True,
        choices=Vive,
        default='',
        max_length=256,
        verbose_name="Vive padre",
        help_text='¿Tu padre vive?'
    )

    padre_nombre = models.CharField(
        default = '',
        max_length = 256,
        verbose_name = 'Nombre',
        help_text = 'Nombre'
    )

    padre_apellido_paterno = models.CharField(
        blank =  True,
        max_length = 256,
        verbose_name = 'Apellido Paterno',
        help_text = 'Apellido Paterno'
    )

    padre_apellido_materno = models.CharField(
        blank =  True,
        max_length = 256,
        verbose_name =   'Apellido Materno',
        help_text = 'Apellido Materno'
    )

    padre_telefono_casa = models.CharField(
        max_length = 8,
        default = '',
        blank =  True,
        verbose_name = "Teléfono  de casa",
        help_text = 'Teléfono  de casa'
    )

    padre_telefono_particular = models.CharField(
        max_length = 8,
        default = '',
        blank = True,
        verbose_name = "Teléfono  particular",
        help_text = 'Teléfono  de particular'
    )

    padre_fecha_nacimiento = models.DateField(
        blank = True,
        null = False,
        default = None
    )

    padre_estado_civil = models.CharField(
        blank =  True,
        max_length = 128,
        choices =  Estado_Civil,
        verbose_name =   'Estado Civil',
        help_text =  'Estado Civil'
    )

    padre_estado = models.CharField(
        blank = True,
        choices = State,
        default = '',
        max_length = 256,
        verbose_name = "Estado",
        help_text = 'Estado'
    )

    padre_ciudad = models.CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Ciudad",
        help_text = 'Ciudad'
    )

    padre_calle = models.CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Calle",
        help_text = 'Calle'
    )

    padre_colonia = models.CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Colonia",
        help_text = 'Colonia'
    )

    padre_codigo_postal = models.CharField(
        blank = True,
        max_length = 128,
        default = '',
        verbose_name = 'Código  Postal',
        help_text = 'Código  Postal'
    )
    
    padre_ocupacion = models.CharField(
        blank = True,
        max_length = 128,
        default = '',
        verbose_name = 'Ocupación',
        help_text = 'Ocupación'
    )
    
    #Info madre

    vive_madre = models.CharField(
        blank=True,
        choices=Vive,
        default='',
        max_length=256,
        verbose_name="Vive madre",
        help_text='¿Tu madre vive?'
    )

    madre_nombre = models.CharField(
        max_length = 256,
        default = '',
        verbose_name = 'Nombre',
        help_text = 'Nombre'
    )

    madre_apellido_paterno = models.CharField(
        blank = True,
        max_length = 256,
        verbose_name = 'Apellido Paterno',
        help_text = 'Apellido Paterno'
    )

    madre_apellido_materno = models.CharField(
        blank = True,
        max_length = 256,
        verbose_name = 'Apellido Materno',
        help_text = 'Apellido Materno'
    )

    madre_telefono_casa = models.CharField(
        max_length = 8,
        default = '',
        blank = True,
        verbose_name = "Teléfono  de casa",
        help_text = 'Teléfono  de casa'
    )

    madre_telefono_particular = models.CharField(
        max_length = 8,
        default = '',
        blank = True,
        verbose_name = "Teléfono  particular",
        help_text = 'Teléfono  de particular'
    )

    madre_fecha_nacimiento = models.DateField(
        blank = True,
        null = True,
    )

    madre_estado_civil = models.CharField(
        blank = True,
        max_length = 128,
        choices = Estado_Civil,
        verbose_name = 'Estado Civil',
        help_text = 'Estado Civil'
    )

    madre_migrante = models.BooleanField(
        default = False
    )

    madre_estado = models.CharField(
        blank = True,
        choices = State,
        default = '',
        max_length = 256,
        verbose_name = "Estado",
        help_text = 'Estado'
    )

    madre_ciudad = models.CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Ciudad",
        help_text = 'Ciudad'
    )

    madre_calle = models.CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Calle",
        help_text = 'Calle'
    )

    madre_codigo_postal = models.CharField(
        blank =  True,
        max_length = 128,
        default = '',
        verbose_name = 'Código  Postal',
        help_text = 'Código  Postal'
    )
    
    madre_colonia = models.CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Colonia",
        help_text = 'Colonia'
    )
    
    madre_ocupacion = models.CharField(
        blank = True,
        max_length = 128,
        default = '',
        verbose_name = 'Ocupación',
        help_text = 'Ocupación'
    )
    
    #formacion familia
    
    integrantes_familia = models.IntegerField(
        blank = True,
        default = 0,
        verbose_name = 'Numero de integrantes',
        help_text = 'Numero de integrantes en la familia'
    )
    
    numero_hermanos = models.IntegerField(
        blank =  True,
        default = 0,
        verbose_name = 'Numero de hermanos',
        help_text = 'Numero de hermanos'
    )
    
    lugar_dentro_familia = models.CharField(
        max_length = 128,
        blank = True,
        verbose_name = 'Lugar dentro de la familia',
        help_text = 'Lugar dentro de la familia'
    )
    
    #relacion con:
    
    relacion_padre = models.CharField(
        max_length = 512,
        blank = True,
        verbose_name = 'Relación con tu padre',
        help_text = 'Relación con tu padre'
    )
    
    relacion_madre = models.CharField(
        max_length = 512,
        blank = True,
        verbose_name = 'Relación con tu madre',
        help_text = 'Relación con tu madre'
    )
    
    relacion_hermanos = models.CharField(
        max_length = 512,
        blank = True,
        verbose_name = 'Relación con tus hermanos',
        help_text = 'Relación con tus hermanos'
    )
    
    encargado_crianza = models.CharField(
        max_length = 256,
        blank = True,
        verbose_name = 'Encargado de tu crianza',
        help_text = 'Encargado de tu crianza'
    )
    
    #ocupacion
    
    trabajado_antes = models.CharField(
        max_length=12,
        blank=True,
        default='',
        choices=Trabajado,
    )
    
    puesto  = models.CharField(
        max_length = 256,
        blank = True,
        verbose_name = 'Puesto de trabajo',
        help_text = 'Puesto'
    )
    
    lugar_trabajo = models.CharField(
        max_length = 256,
        blank = True,
        verbose_name = 'Lugar trabajo',
        help_text = 'Lugar de trabajo'
    )
    
    jefe_inmediato = models.CharField(
        max_length = 256,
        blank = True,
        default = '',
        verbose_name = 'Jefe inmediato',
        help_text = 'Jefe inmediato'
    )
    
    telefono_jefe = models.CharField(
        max_length = 24,
        blank = True,
        default = ''
    )

    trabajo_estado = models.CharField(
        blank = True,
        choices = State,
        default = '',
        max_length = 256,
        verbose_name = "Estado",
        help_text = 'Estado'
    )

    trabajo_ciudad = models.CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Ciudad",
        help_text = 'Ciudad'
    )

    trabajo_calle = models.CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Calle",
        help_text = 'Calle'
    )

    trabajo_codigo_postal = models.CharField(
        blank = True,
        max_length = 128,
        default = '',
        verbose_name = 'Código  Postal',
        help_text = 'Código  Postal'
    )

    trabajo_colonia = models.CharField(
        blank = True,
        max_length = 128,
        default = '',
        verbose_name = 'Colonia',
        help_text = 'Colonia'
    )
    
    # Como conociste vida y familia

    referencia = models.CharField(
        blank = True,
        choices =  Referencia,
        default = '',
        max_length = 256,
        verbose_name = "Referencia",
        help_text = 'Cómo conoció VIFAC'
    )
    
    visto_en = models.CharField(
        max_length = 256,
        blank = True,
        default = '',
        verbose_name = 'Dónde se ha visto la referencia'
    )

    canal = models.CharField(
        max_length = 256,
        blank = True,
        default = '',
        verbose_name = 'Canal donde se ha visto la referencia'
    )

    otros = models.CharField(
        max_length = 256,
        blank = True,
        default = '',
        verbose_name = 'Otro medio donde se ha visto la referencia'
    )

    # Datos Generales de la Persona

    nombre_recomendacion = models.CharField(
        max_length = 64,
        blank = True,
        default = '',
        verbose_name = 'Nombre persona'
    )

    apellido_paterno_recomendacion = models.CharField(
        max_length = 64,
        blank = True,
        default = '',
        verbose_name = 'Apellido paterno'
    )

    apellido_materno_recomendacion = models.CharField(
        max_length = 64,
        blank = True,
        default = '',
        verbose_name = 'Apellido materno'
    )

    relacion_recomendacion = models.CharField(
        max_length = 1024,
        choices = Relacion_Vives,
        blank = True,
        default = '',
        verbose_name = 'Relación con la persona que recomienda'
    )

    telefono_recomendacion = PhoneNumberField(
        default = ''
    )

    # Dirección

    calle_recomendacion = models.CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = 'Calle',
        help_text = 'Calle'
    )

    numero_exterior = models.CharField(
        blank = True,
        max_length = 8,
        default = '',
        verbose_name = 'Número',
        help_text = 'Número'
    )

    codigo_postal_recomendacion = models.CharField(
        blank = True,
        max_length = 8,
        default = '',
        verbose_name = 'Código  Postal',
        help_text = 'Código  Postal'
    )

    colonia = models.CharField(
        max_length = 128,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Colonia'
    )

    ciudad_referencia = models.CharField(
        blank = True,
        max_length = 64,
        default = '',
        verbose_name = "Ciudad",
        help_text = 'Ciudad'
    )

    estado_referencia = models.CharField(
        max_length = 1024,
        blank = True,
        choices = State,
        default = '',
        verbose_name = "Estado",
        help_text = 'Estado'
    )

    # Situación Actual
    # Información General

    tipo_de_ayuda = models.CharField(
        max_length = 1024,
        choices = Ayuda,
        blank = True,
        default = '',
        verbose_name = 'Tipo de ayuda'
    )

    fecha_ultima_menstruacion = models.DateField(
        auto_now = False,
        null = False,
        blank = True,
        default = None,
        verbose_name = 'Fecha de última menstruación'
    )

    fecha_de_parto_esperada = models.DateField(
        auto_now = False,
        null = False,
        blank = True,
        default = None,
        verbose_name = 'Fecha esperada de parto'
    )

    # Referencias
    # Contacto de Emergencia

    nombre_emergencia = models.CharField(
        blank = True,
        max_length = 64,
        default = '',
        verbose_name = 'Nombre',
        help_text = 'Nombre contacto de emergencia'
    )

    apellido_paterno_emergencia = models.CharField(
        max_length = 64,
        blank = True,
        default = '',
        verbose_name = 'Apellido paterno'
    )

    apellido_materno_emergencia = models.CharField(
        max_length = 64,
        blank = True,
        default = '',
        verbose_name = 'Apellido materno'
    )

    relacion_emergencia = models.CharField(
        max_length = 1024,
        choices = Relacion_Vives,
        blank = True,
        default = '',
        verbose_name = 'Relación con el contacto de emergencia'
    )

    telefono_emergencia = PhoneNumberField(
        default = ''
    )

    codigo_postal_emergencia = models.CharField(
        blank = True,
        max_length = 8,
        default = '',
        verbose_name = 'Código  Postal',
        help_text = 'Código  Postal'
    )

    colonia_emergencia = models.CharField(
        max_length = 128,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Colonia'
    )

    ciudad_emergencia = models.CharField(
        blank = True,
        max_length = 64,
        default = '',
        verbose_name = "Ciudad",
        help_text = 'Ciudad'
    )

    estado_emergencia = models.CharField(
        max_length = 1024,
        blank = True,
        choices = State,
        default = '',
        verbose_name = "Estado",
        help_text = 'Estado'
    )
    
    calle_emergencia = models.CharField(
        max_length = 1024,
        blank = True,
        default = '',
        verbose_name = "Calle",
        help_text = 'Calle'
    )

    # Referencia Médica

    control_medico = models.BooleanField(
        null = False,
        blank = True,
        default = False,
        verbose_name = 'Ha tenido control médico'
    )

    enfermedades_padecidas = models.CharField(
        max_length = 128,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Enfermedades Padecidas'
    )

    nombre_medico = models.CharField(
        max_length = 256,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Nombre del médico a cargo'
    )

    nombre_clinica = models.CharField(
        max_length = 256,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Nombre de la clínica'
    )

    telefono_medico = PhoneNumberField(
        default = ''
    )

    calle_medico = models.CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Calle",
        help_text = 'Calle'
    )

    numero_exterior_medico = models.CharField(
        blank = True,
        max_length = 8,
        default = '',
        verbose_name = "Número de calle",
        help_text = 'Número de calle'
    )

    codigo_postal_medico = models.CharField(
        blank = True,
        max_length = 8,
        default = '',
        verbose_name = 'Código  Postal',
        help_text = 'Código  Postal'
    )

    colonia_medico = models.CharField(
        max_length = 128,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Colonia'
    )

    ciudad_medico = models.CharField(
        blank = True,
        max_length = 256,
        default = '',
        verbose_name = "Ciudad",
        help_text = 'Ciudad'
    )

    estado_medico = models.CharField(
        max_length = 1024,
        blank = True,
        choices = State,
        default = '',
        verbose_name = "Estado",
        help_text = 'Estado'
    )

    # Personal

    estado_de_animo = models.CharField(
        max_length = 1024,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Estado de ánimo'
    )

    infancia = models.CharField(
        max_length = 1024,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Descripción infancia'
    )

    # Embarazo

    tipo_embarazo = models.CharField(
        max_length = 1024,
        choices = Embarazo,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Tipo de embarazo'
    )

    reaccion = models.CharField(
        max_length = 1024,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Reacción al embarazo'
    )

    apoyo_papa = models.CharField(
        max_length = 1024,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Apoyo del papá'
    )

    relacion_con_padre = models.CharField(
        max_length = 1024,
        choices = Relacion,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Relación con el padre'
    )

    duracion_relacion = models.CharField(
        max_length = 64,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Duración de la relación'
    )

    familiares = models.CharField(
        max_length = 512,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Familiares que saben del embarazo'
    )

    actitud_familiares = models.CharField(
        max_length = 512,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Actitud que espera de los familiares'
    )

    relacion_voluntaria = models.CharField(
        max_length = 1024,
        choices = Voluntario,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Relaciones voluntarias'
    )

    comunicacion_padre = models.BooleanField(
        null = False,
        blank = True,
        default = True,
        verbose_name = 'Comunicación con el padre'
    )

    aborto_considerado = models.BooleanField(
        null = False,
        blank = True,
        default = False,
        verbose_name = 'Se consideró el abortó'
    )

    violencia_intrafamiliar = models.BooleanField(
        null = False,
        blank = True,
        default = False,
        verbose_name = 'Violencia intrafamiliar'
    )

    # Escolaridad

    maximo_grado_estudios = models.CharField(
        max_length = 1024,
        null = False,
        choices = Estudios,
        blank = True,
        default = 'Otro',
        verbose_name = 'Máximo grado de estudios'
    )

    nombre_escuela = models.CharField(
        max_length = 128,
        null = False,
        blank = True,
        default = '',
        verbose_name = 'Nombre de la institución escolar'
    )

    tiempo_cursado = models.CharField(
        max_length = 1024,
        choices = Duracion,
        null = False,
        blank = True,
        default = 'Otro',
        verbose_name = 'Años cursados'
    )

    class Meta(object):
        verbose_name = 'Expediente'
        verbose_name_plural = 'Expedientes'
