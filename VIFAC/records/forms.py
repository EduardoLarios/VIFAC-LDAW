# -*- coding: utf-8 -*-
from phonenumber_field.formfields import PhoneNumberField
from .models import Expediente
from django import forms
from .models import State, Relacion_Vives, Estado_Civil, Referencia, Embarazo, Voluntario, Relacion, Estudios, Duracion, Ayuda


class DonorForm(forms.Form):
    nombre = forms.CharField(
        max_length=256,
        help_text='Nombre',
        label='Nombre de la beneficiaria'
    )

    apellido_paterno = forms.CharField(
        max_length=256,
        help_text='Apellido Paterno',
        label = 'Apellido Paterno'
    )
    
    apellido_materno = forms.CharField(
        max_length=256,
        help_text='Apellido Materno',
        label='Apellido Materno'
    )

    edad = forms.IntegerField(
        blank=True,
        help_text='Edad',
        label = 'Edad'
    )
    
    telefono_casa = forms.CharField(
        max_length=10,
        initial='+52',
        help_text='Telefono de casa',
        label='Telefono de casa'
    )
    
    telefono_particular = forms.CharField(
        max_length = 10,
        initial='+52',
        help_text='Telefono de particular',
        label='Telefono de particular'
    )
    
    fecha_nacimiento = forms.DateField(
        blank = True,
        label='Fecha de nacimiento'
    )
    
    estado_civil =  forms.CharField(
        max_length=128,
        choices=Estado_Civil,
        help_text='Estado Civil',
        label='Estado Civil'
    )
    
    migrante = forms.BooleanField(
        label='¿Eres migrate?'
    )

    estado = forms.CharField(
        choices=State,
        max_length=256,
        help_text = 'Estado',
        label='Estado'
    )
    
    ciudad = forms.CharField(
        max_length=256,
        help_text='Ciudad',
        label='Ciudad'
    )
    
    calle = forms.CharField(
        max_length=256,
        help_text='Calle',
        label='Calle'
    )
    
    codigo_postal =  forms.CharField(
        max_length=128,
        help_text='Codigo Postal',
        label = 'Codigo Postal'
    )
    
    vives_nombre = forms.CharField(
        max_length=256,
        help_text='Nombre',
        label='Nombre'
    )

    vives_apellido_paterno = forms.CharField(
        max_length=256,
        help_text='Apellido Paterno',
        label='Apellido Paterno'
    )
    
    vives_apellido_materno = forms.CharField(
        max_length=256,
        help_text='Apellido Materno',
        label='Apellido Materno'
    )
    
    tipo_relacion_vives = forms.CharField(
        max_length=128,
        choices=Relacion_Vives,
        help_text='Con quien vives',
        label = 'Tipo de relación con quien vives'
    )
    
    telefono_vives = forms.CharField(
        max_length = 8,
        help_text='Telefono de la persona con quien vives',
        label='Telefono de la persona con quien vives'
    )
    
    estado_vives = forms.CharField(
        choices=State,
        max_length=256,
        help_text='Estado',
        label='Estado'
    )
    
    ciudad_vives = forms.CharField(
        max_length=256,
        help_text='Ciudad',
        label='Ciudad'
    )
    
    calle_vives = forms.CharField(
        blank=True,
        max_length=256,
        help_text='Calle',
        label = 'Calle'
    )
    
    codigo_postal_vives = forms.CharField(
        max_length=128,
        verbose_name='Codigo Postal',
        help_text='Codigo Postal',
        label='Codigo Postal'
    )
    
    vive_padre = forms.BooleanField(
        label='¿Vive tu padre?'
    )
    
    padre_nombre = forms.CharField(
        max_length=256,
        verbose_name='Nombre',
        help_text='Nombre'
    )

    padre_apellido_paterno = forms.CharField(
        blank=True,
        max_length=256,
        verbose_name='Apellido Paterno',
        help_text='Apellido Paterno'
    )

    padre_apellido_materno = forms.CharField(
        blank=True,
        max_length=256,
        verbose_name='Apellido Materno',
        help_text='Apellido Materno'
    )

    padre_telefono_casa = forms.CharField(
        max_length=8,
        blank=True,
        verbose_name="Telefono de casa",
        help_text='Telefono de casa'
    )

    padre_telefono_particular = forms.CharField(
        max_length=8,
        blank=True,
        verbose_name="Telefono particular",
        help_text='Telefono de particular'
    )

    padre_fecha_nacimiento = forms.DateField(
        blank=True,
        null=True,
    )

    padre_estado_civil = forms.CharField(
        blank=True,
        max_length=128,
        choices=Estado_Civil,
        verbose_name='Estado Civil',
        help_text='Estado Civil'
    )

    padre_estado = forms.CharField(
        blank=True,
        choices=State,
        max_length=256,
        verbose_name="Estado",
        help_text='Estado'
    )

    padre_ciudad = forms.CharField(
        blank=True,
        max_length=256,
        verbose_name="Ciudad",
        help_text='Ciudad'
    )

    padre_calle = forms.CharField(
        blank=True,
        max_length=256,
        verbose_name="Calle",
        help_text='Calle'
    )

    padre_codigo_postal = forms.CharField(
        blank=True,
        max_length=128,
        verbose_name='Codigo Postal',
        help_text='Codigo Postal'
    )

    # Info madre

    vive_madre = forms.BooleanField(
        
    )

    madre_nombre = forms.CharField(
        max_length=256,
        verbose_name='Nombre',
        help_text='Nombre'
    )

    madre_apellido_paterno = forms.CharField(
        blank=True,
        max_length=256,
        verbose_name='Apellido Paterno',
        help_text='Apellido Paterno'
    )

    madre_apellido_materno = forms.CharField(
        blank=True,
        max_length=256,
        verbose_name='Apellido Materno',
        help_text='Apellido Materno'
    )

    madre_telefono_casa = forms.CharField(
        max_length=8,
        blank=True,
        verbose_name="Telefono de casa",
        help_text='Telefono de casa'
    )

    madre_telefono_particular = forms.CharField(
        max_length=8,
        blank=True,
        verbose_name="Telefono particular",
        help_text='Telefono de particular'
    )

    madre_fecha_nacimiento = forms.DateField(
        blank=True,
        null=True,
    )

    madre_estado_civil = forms.CharField(
        blank=True,
        max_length=128,
        choices=Estado_Civil,
        help_text='Estado Civil'
    )

    madre_migrante = forms.BooleanField(
    )

    madre_estado = forms.CharField(
        choices=State,
        max_length=256,
        help_text='Estado'
    )

    madre_ciudad = forms.CharField(
        max_length=256,
        help_text='Ciudad'
    )

    madre_calle = forms.CharField(
        max_length=256,
        help_text='Calle'
    )

    madre_codigo_postal = forms.CharField(
        max_length=128,
        help_text='Codigo Postal'
    )

    # formacion familia

    integrantes_familia = forms.IntegerField(
        verbose_name='Numero de integrantes',
        help_text='Numero de integrantes en la familia'
    )

    numero_hermanos = forms.IntegerField(
        help_text='Numero de hermanos'
    )

    lugar_dentro_familia = forms.CharField(
        max_length=128,
        help_text='Lugar dentro de la familia'
    )

    # relacion con:

    relacion_padre = forms.CharField(
        max_length=512,
        help_text='Relación con tu padre'
    )

    relacion_madre = forms.CharField(
        max_length=512,
        help_text='Relación con tu madre'
    )

    relacion_hermanos = forms.CharField(
        max_length=512,
        help_text='Relación con tus hermanos'
    )

    encargado_crianza = forms.CharField(
        max_length=256,
        help_text='Encargado de tu crianza'
    )

    # ocupacion

    trabajado_antes = forms.BooleanField(
        blank=True,
    )

    puesto = forms.CharField(
        max_length=256,
        help_text='Puesto'
    )

    lugar_trabajo = forms.CharField(
        max_length=256,
        help_text='Lugar de trabajo'
    )

    jefe_inmediato = forms.CharField(
        max_length=256,
        help_text='Jefe inmediato'
    )

    telefono_jefe = forms.CharField(
        max_length=24,
        blank=True,
    )

    trabajo_estado = forms.CharField(
        choices=State,
        max_length=256,
        help_text='Estado'
    )

    trabajo_ciudad = forms.CharField(
        max_length=256,
        verbose_name="Ciudad",
        help_text='Ciudad'
    )

    trabajo_calle = forms.CharField(
        max_length=256,
        help_text='Calle'
    )

    trabajo_codigo_postal = forms.CharField(
        max_length=128,
        verbose_name='Codigo Postal',
        help_text='Codigo Postal'
    )

    # Como conociste vida y familia

    referencia = forms.CharField(
        choices=Referencia,
        max_length=256,
        help_text='Cómo conoció VIFAC'
    )

    visto_en = forms.CharField(
        max_length=256,
        blank=True,
        verbose_name='Dónde se ha visto la referencia'
    )

    canal = forms.CharField(
        max_length=256,
        verbose_name='Canal donde se ha visto la referencia'
    )

    otros = forms.CharField(
        max_length=256,
        verbose_name='Otro medio donde se ha visto la referencia'
    )

    # Datos Generales de la Persona

    nombre_recomendacion = forms.CharField(
        max_length=64,
        verbose_name='Nombre persona'
    )

    apellido_paterno_recomendacion = forms.CharField(
        max_length=64,
        verbose_name='Apellido paterno'
    )

    apellido_materno_recomendacion = forms.CharField(
        max_length=64,
    )

    relacion_recomendacion = forms.CharField(
        max_length=1024,
        choices=Relacion_Vives,
    )

    telefono_recomendacion = PhoneNumberField(
        initial='+52'
    )

    # Dirección

    calle_recomendacion = forms.CharField(
        max_length=256,
        help_text='Calle'
    )

    numero_exterior = forms.CharField(
        max_length=8,
        help_text='Número'
    )

    codigo_postal_recomendacion = forms.CharField(
        max_length=8,
        help_text='Codigo Postal'
    )

    colonia = forms.CharField(
        max_length=128,
        verbose_name='Colonia',
        help_text='Colonia'
    )

    ciudad_referencia = forms.CharField(
        max_length=64,
        help_text='Ciudad'
    )

    estado_referencia = forms.CharField(
        max_length=1024,
        choices=State,
        help_text='Estado'
    )

    tipo_de_ayuda = forms.CharField(
        max_length=1024,
        choices=Ayuda,
    )

    fecha_ultima_menstruacion = forms.DateField(
        auto_now=False,
        help_text='Fecha de ultima menstruación'
    )

    fecha_de_parto_esperada = forms.DateField(
        auto_now=False,
        help_text='Fecha esperada de parto'
    )

    # Referencias
    # Contacto de Emergencia

    nombre_emergencia = forms.CharField(
        max_length=64,
        help_text='Nombre contacto de emergencia'
    )

    apellido_paterno_emergencia = forms.CharField(
        max_length=64,
        help_text='Apellido paterno'
    )

    apellido_materno_emergencia = forms.CharField(
        max_length=64,
        help_text='Apellido materno'
    )

    relacion_emergencia = forms.CharField(
        max_length=1024,
        choices=Relacion_Vives,
        help_text='Relación con el contacto de emergencia'
    )

    telefono_emergencia = PhoneNumberField(
        initial='+52'
    )

    codigo_postal_emergencia = forms.CharField(
        max_length=8,
        help_text='Codigo Postal'
    )

    colonia_emergencia = forms.CharField(
        max_length=128,
        help_text='Colonia'
    )

    ciudad_emergencia = forms.CharField(
        max_length=64,
        help_text='Ciudad'
    )

    estado_emergencia = forms.CharField(
        max_length=1024,
        choices=State,
        help_text='Estado'
    )

    # Referencia Médica

    control_medico = forms.BooleanField(
        help_text='Ha tenido control médico'
    )

    enfermedades_padecidas = forms.CharField(
        max_length=128,
        help_text='Enfermedades Padecidas'
    )

    nombre_medico = forms.CharField(
        max_length=256,
        help_text='Nombre del médico a cargo'
    )

    nombre_clinica = forms.CharField(
        max_length=256,
        help_text='Nombre de la clínica'
    )

    telefono_medico = PhoneNumberField(
        initial='+52'
    )

    calle_medico = forms.CharField(
        max_length=256,
        help_text='Calle'
    )

    numero_exterior_medico = forms.CharField(
        max_length=8,
        help_text='Número de calle'
    )

    codigo_postal_medico = forms.CharField(
        max_length=8,
        help_text='Codigo Postal'
    )

    colonia_medico = forms.CharField(
        max_length=128,
        verbose_name='Colonia'
    )

    ciudad_medico = forms.CharField(
        max_length=256,
        help_text='Ciudad'
    )

    estado_medico = forms.CharField(
        max_length=1024,
        choices=State,
        help_text='Estado'
    )

    # Personal

    estado_de_animo = forms.CharField(
        max_length=1024,
        help_text='Estado de ánimo'
    )

    infancia = forms.CharField(
        max_length=1024,
        help_text='Descripción infancia'
    )

    # Embarazo

    tipo_embarazo = forms.CharField(
        max_length=1024,
        choices=Embarazo,
        help_text='Tipo de embarazo'
    )

    reaccion = forms.CharField(
        max_length=1024,
        help_text='Reacción al embarazo'
    )

    apoyo_papa = forms.CharField(
        max_length=1024,
        help_text='Apoyo del papá'
    )

    relacion_con_padre = forms.CharField(
        max_length=1024,
        choices=Relacion,
        help_text='Relación con el padre'
    )

    duracion_relacion = forms.CharField(
        max_length=64,
        help_text='Duración de la relación'
    )

    familiares = forms.CharField(
        max_length=512,
        help_text='Familiares que saben del embarazo'
    )

    actitud_familiares = forms.CharField(
        max_length=512,
        help_text='Actitud que espera de los familiares'
    )

    relacion_voluntaria = forms.CharField(
        max_length=1024,
        choices=Voluntario,
        help_text='Relaciones voluntarias'
    )

    comunicacion_padre = forms.BooleanField(
        help_text='Comunicación con el padre'
    )

    aborto_considerado = forms.BooleanField(
        help_text='Se consideró el abortó'
    )

    violencia_intrafamiliar = forms.BooleanField(
        help_text='Violencia intrafamiliar'
    )

    # Escolaridad

    maximo_grado_estudios = forms.CharField(
        max_length=1024,
        choices=Estudios,
        help_text='Máximo grado de estudios'
    )

    nombre_escuela = forms.CharField(
        max_length=128,
        help_text='Nombre de la institución escolar'
    )

    tiempo_cursado = forms.CharField(
        max_length=1024,
        choices=Duracion,
        help_text='Años cursados'
    )