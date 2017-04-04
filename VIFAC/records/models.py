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

class Expediente(models.Model):
    #Datos Generales
    nombre = models.CharField(
        max_length=256,
        verbose_name='Nombre',
        help_text='Nombre'
    )
    
    apellido_paterno = models.CharField(
        max_length=256,
        verbose_name='Apellido Paterno',
        help_text='Apellido Paterno'
    )
    
    apellido_materno = models.CharField(
        max_length=256,
        verbose_name='Apellido Materno',
        help_text='Apellido Materno'
    )
    
    edad = models.IntegerField(
        blank=True,
        verbose_name='Edad',
        help_text='Edad'
    )
    
    telefono_casa = models.CharField(
        max_length=8,
        default='',
        blank=True,
        verbose_name= "Telefono de casa",
        help_text='Telefono de casa'
    )
    
    telefono_particular = models.CharField(
        max_length = 8,
        default = '',
        blank= True,
        verbose_name= "Telefono particular",
        help_text='Telefono de particular'
    )
    
    fecha_nacimiento = models.DateField(
        blank = True
    )
    
    estado_civil =  models.CharField(
        max_length=128,
        choices=Estado_Civil,
        verbose_name='Estado Civil',
        help_text='Estado Civil'
    )
    
    migrante = models.BooleanField(
        default=False
    )

    estado = models.CharField(
        blank=True,
        choices=State,
        default='',
        max_length=256,
        verbose_name="Estado",
        help_text = 'Estado'
    )

    ciudad = models.CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Ciudad",
        help_text='Ciudad'
    )

    calle = models.CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Calle",
        help_text='Calle'
    )
    
    codigo_postal =  models.CharField(
        blank=True,
        max_length=128,
        default='',
        verbose_name='Codigo Postal',
        help_text='Codigo Postal'
    )
    
    #Historia Familiar
    
    vives_nombre = models.CharField(
        max_length=256,
        verbose_name='Nombre',
        help_text='Nombre'
    )
    
    vives_apellido_paterno = models.CharField(
        max_length=256,
        verbose_name='Apellido Paterno',
        help_text='Apellido Paterno'
    )

    vives_apellido_materno = models.CharField(
        max_length=256,
        verbose_name='Apellido Materno',
        help_text='Apellido Materno'
    )
    
    tipo_relacion_vives = models.CharField(
        max_length=128,
        blank=True,
        choices=Relacion_Vives,
        default='',
        verbose_name='Con quien vives',
        help_text='Con quien vives'
    )
    
    telefono_vives = models.CharField(
        max_length = 8,
        default = '',
        blank= True,
        verbose_name= "Telefono",
        help_text='Telefono de la persona con quien vives'
    )

    estado_vives = models.CharField(
        blank=True,
        choices=State,
        default='',
        max_length=256,
        verbose_name="Estado",
        help_text='Estado'
    )

    ciudad_vives = models.CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Ciudad",
        help_text='Ciudad'
    )

    calle_vives = models.CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Calle",
        help_text='Calle'
    )

    codigo_postal_vives = models.CharField(
        blank=True,
        max_length=128,
        default='',
        verbose_name='Codigo Postal',
        help_text='Codigo Postal'
    )
    
    #info padre
    
    vive_padre = models.BooleanField(
        default=True,
    )

    padre_nombre = models.CharField(
        default='',
        max_length=256,
        verbose_name='Nombre',
        help_text='Nombre'
    )

    padre_apellido_paterno = models.CharField(
        blank=True,
        max_length=256,
        verbose_name='Apellido Paterno',
        help_text='Apellido Paterno'
    )

    padre_apellido_materno = models.CharField(
        blank=True,
        max_length=256,
        verbose_name='Apellido Materno',
        help_text='Apellido Materno'
    )

    padre_telefono_casa = models.CharField(
        max_length=8,
        default='',
        blank=True,
        verbose_name="Telefono de casa",
        help_text='Telefono de casa'
    )

    padre_telefono_particular = models.CharField(
        max_length=8,
        default='',
        blank=True,
        verbose_name="Telefono particular",
        help_text='Telefono de particular'
    )

    padre_fecha_nacimiento = models.DateField(
        blank=True,
        null=True,
    )

    padre_estado_civil = models.CharField(
        blank=True,
        max_length=128,
        choices=Estado_Civil,
        verbose_name='Estado Civil',
        help_text='Estado Civil'
    )

    padre_estado = models.CharField(
        blank=True,
        choices=State,
        default='',
        max_length=256,
        verbose_name="Estado",
        help_text='Estado'
    )

    padre_ciudad = models.CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Ciudad",
        help_text='Ciudad'
    )

    padre_calle = models.CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Calle",
        help_text='Calle'
    )

    padre_codigo_postal = models.CharField(
        blank=True,
        max_length=128,
        default='',
        verbose_name='Codigo Postal',
        help_text='Codigo Postal'
    )
    
    #Info madre

    vive_madre = models.BooleanField(
        default=True
    )

    madre_nombre = models.CharField(
        max_length=256,
        default='',
        verbose_name='Nombre',
        help_text='Nombre'
    )

    madre_apellido_paterno = models.CharField(
        blank=True,
        max_length=256,
        verbose_name='Apellido Paterno',
        help_text='Apellido Paterno'
    )

    madre_apellido_materno = models.CharField(
        blank=True,
        max_length=256,
        verbose_name='Apellido Materno',
        help_text='Apellido Materno'
    )

    madre_telefono_casa = models.CharField(
        max_length=8,
        default='',
        blank=True,
        verbose_name="Telefono de casa",
        help_text='Telefono de casa'
    )

    madre_telefono_particular = models.CharField(
        max_length=8,
        default='',
        blank=True,
        verbose_name="Telefono particular",
        help_text='Telefono de particular'
    )

    madre_fecha_nacimiento = models.DateField(
        blank=True,
        null=True,
    )

    madre_estado_civil = models.CharField(
        blank=True,
        max_length=128,
        choices=Estado_Civil,
        verbose_name='Estado Civil',
        help_text='Estado Civil'
    )

    madre_migrante = models.BooleanField(
        default=False
    )

    madre_estado = models.CharField(
        blank=True,
        choices=State,
        default='',
        max_length=256,
        verbose_name="Estado",
        help_text='Estado'
    )

    madre_ciudad = models.CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Ciudad",
        help_text='Ciudad'
    )

    madre_calle = models.CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Calle",
        help_text='Calle'
    )

    madre_codigo_postal = models.CharField(
        blank=True,
        max_length=128,
        default='',
        verbose_name='Codigo Postal',
        help_text='Codigo Postal'
    )
    
    #formacion familia
    
    integrantes_familia = models.IntegerField(
        blank=True,
        default=0,
        verbose_name='Numero de integrantes',
        help_text='Numero de integrantes en la familia'
    )
    
    numero_hermanos = models.IntegerField(
        blank=True,
        default=0,
        verbose_name='Numero de hermanos',
        help_text='Numero de hermanos'
    )
    
    lugar_dentro_familia = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='Lugar dentro de la familia',
        help_text='Lugar dentro de la familia'
    )
    
    #relacion con:
    
    relacion_padre = models.CharField(
        max_length=512,
        blank=True,
        verbose_name='Relación con tu padre',
        help_text='Relación con tu padre'
    )
    
    relacion_madre = models.CharField(
        max_length=512,
        blank=True,
        verbose_name='Relación con tu madre',
        help_text='Relación con tu madre'
    )
    
    relacion_hermanos = models.CharField(
        max_length=512,
        blank=True,
        verbose_name='Relación con tus hermanos',
        help_text='Relación con tus hermanos'
    )
    
    encargado_crianza = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='Encargado de tu crianza',
        help_text='Encargado de tu crianza'
    )
    
    #ocupacion
    
    trabajado_antes = models.BooleanField(
        blank=True,
        default=False
    )
    
    puesto  = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='Puesto de trabajo',
        help_text='Puesto'
    )
    
    lugar_trabajo = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='Lugar trabajo',
        help_text='Lugar de trabajo'
    )
    
    jefe_inmediato = models.CharField(
        max_length=256,
        blank=True,
        default='',
        verbose_name='Jefe inmediato',
        help_text='Jefe inmediato'
    )
    
    telefono_jefe = models.CharField(
        max_length=24,
        blank=True,
        default=''
    )

    trabajo_estado = models.CharField(
        blank=True,
        choices=State,
        default='',
        max_length=256,
        verbose_name="Estado",
        help_text='Estado'
    )

    trabajo_ciudad = models.CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Ciudad",
        help_text='Ciudad'
    )

    trabajo_calle = models.CharField(
        blank=True,
        max_length=256,
        default='',
        verbose_name="Calle",
        help_text='Calle'
    )

    trabajo_codigo_postal = models.CharField(
        blank=True,
        max_length=128,
        default='',
        verbose_name='Codigo Postal',
        help_text='Codigo Postal'
    )
    
    # Como conociste vida y familia
    
    referencia =  models.CharField(
        blank=True,
        choices=Referencia,
        default='',
        max_length=256,
        verbose_name="Referencia",
        help_text='Cómo conoció VIFAC'
    )
    
    