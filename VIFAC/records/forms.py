# -*- coding: utf-8 -*-
from .models import State, Relacion_Vives, Estado_Civil, Referencia, Embarazo, Voluntario, Relacion, Estudios, Duracion, Ayuda, Religiones, Poblacion, Migrante, Vive, Trabajado
from phonenumber_field.formfields import PhoneNumberField
from django import forms


class RecordForm(forms.Form):
    nombre = forms.CharField(
        help_text = 'Nombre',
        label = 'Nombre de la beneficiaria'
    )

    apellido_paterno = forms.CharField(
        help_text = 'Apellido Paterno',
        label = 'Apellido Paterno'
    )
    
    apellido_materno = forms.CharField(
        help_text = 'Apellido Materno',
        label = 'Apellido Materno'
    )

    edad = forms.IntegerField(
        help_text = 'Edad',
        label = 'Edad'
    )
    
    telefono_casa = forms.CharField(
        initial = '+52',
        help_text = 'Teléfono de casa',
        label = 'Teléfono de casa'
    )
    
    telefono_particular = forms.CharField(
        initial = '+52',
        help_text = 'Teléfono de particular',
        label = 'Teléfono de particular'
    )
    
    fecha_nacimiento = forms.DateField(
        label = 'Fecha de nacimiento'
    )
    
    estado_nacimiento = forms.ChoiceField(
        label='Estado de Nacimiento',
        choices=State,
        help_text='Estado de nacimiento'
    )
    
    estado_civil =  forms.ChoiceField(
        choices = Estado_Civil,
        help_text = 'Estado Civil',
        label = 'Estado Civil',
    )
    
    religion =  forms.ChoiceField(
        choices=Religiones,
        help_text='Religión',
        label='Religión',
    )

    tipo_poblacion = forms.ChoiceField(
        choices=Poblacion,
        help_text='Tipo de población',
        label='Tipo de población',
    )
    
    migrante = forms.ChoiceField(
        choices=Migrante,
        help_text='¿Eres migrante?',
        label='¿Eres migrate?',
    )

    estado = forms.ChoiceField(
        choices = State,
        help_text = 'Estado',
        label = 'Estado'
    )
    
    ciudad = forms.CharField(
        help_text = 'Ciudad',
        label = 'Ciudad'
    )
    
    calle = forms.CharField(
        help_text = 'Calle',
        label = 'Calle'
    )
    
    colonia = forms.CharField(
        help_text='Colonia',
        label='Colonia'
    )
    
    codigo_postal =  forms.CharField(
        help_text = 'Código Postal',
        label = 'Código Postal'
    )
    
    vives_nombre = forms.CharField(
        help_text = 'Nombre',
        label = 'Nombre'
    )

    vives_apellido_paterno = forms.CharField(
        help_text = 'Apellido Paterno',
        label = 'Apellido Paterno'
    )
    
    vives_apellido_materno = forms.CharField(
        help_text = 'Apellido Materno',
        label = 'Apellido Materno'
    )
    
    tipo_relacion_vives = forms.ChoiceField(
        choices = Relacion_Vives,
        help_text = 'Con quien vives',
        label = 'Tipo de relación con quien vives'
    )
    
    telefono_vives = forms.CharField(
        help_text = 'Teléfono de la persona con quien vives',
        initial='+52',
        label = 'Teléfono de la persona con quien vives'
    )
    
    estado_vives = forms.ChoiceField(
        choices = State,
        help_text = 'Estado',
        label = 'Estado'
    )
    
    ciudad_vives = forms.CharField(
        help_text = 'Ciudad',
        label = 'Ciudad'
    )
    
    calle_vives = forms.CharField(
        help_text = 'Calle',
        label = 'Calle'
    )
    
    colonia_vives = forms.CharField(
        help_text = 'Colonia',
        label = 'Colonia'
    )
    
    codigo_postal_vives = forms.CharField(
        help_text = 'Código Postal',
        label = 'Código Postal'
    )
    
    vive_padre = forms.ChoiceField(
        choices=Vive,
        help_text='¿Tu padre vive?',
        label='¿Vive tu padre?'
    )
    
    padre_nombre = forms.CharField(
        help_text = 'Nombre'
    )

    padre_apellido_paterno = forms.CharField(
        help_text = 'Apellido Paterno'
    )

    padre_apellido_materno = forms.CharField(
        help_text = 'Apellido Materno'
    )

    padre_telefono_casa = forms.CharField(
        help_text = 'Teléfono de casa'
    )

    padre_telefono_particular = forms.CharField(
        help_text = 'Teléfono de particular'
    )

    padre_fecha_nacimiento = forms.DateField()

    padre_estado_civil = forms.ChoiceField(
        choices=Estado_Civil,
        help_text = 'Estado Civil'
    )

    padre_estado = forms.ChoiceField(
        choices = State,
        help_text = 'Estado'
    )

    padre_ciudad = forms.CharField(
        help_text = 'Ciudad'
    )

    padre_calle = forms.CharField(
        help_text = 'Calle'
    )
    
    padre_colonia = forms.CharField(
        help_text = 'Colonia',
        label = 'Colonia'
    )

    padre_codigo_postal = forms.CharField(
        help_text = 'Código Postal'
    )

    padre_ocupacion = forms.CharField(
        help_text = 'Ocupación',
        label = 'Ocupación'
    )
    # Info madre

    vive_madre = forms.ChoiceField(
        choices=Vive,
        help_text='¿Tu madre vive?',
        label='¿Vive tu madre?'
    )

    madre_nombre = forms.CharField(
        help_text = 'Nombre'
    )

    madre_apellido_paterno = forms.CharField(
        help_text = 'Apellido Paterno'
    )

    madre_apellido_materno = forms.CharField(
        help_text = 'Apellido Materno'
    )

    madre_telefono_casa = forms.CharField(
        help_text = 'Teléfono de casa'
    )

    madre_telefono_particular = forms.CharField(
        help_text = 'Teléfono de particular'
    )

    madre_fecha_nacimiento = forms.DateField()

    madre_estado_civil = forms.ChoiceField(
        choices = Estado_Civil,
        help_text = 'Estado Civil'
    )

    madre_migrante = forms.BooleanField(
    )

    madre_estado = forms.ChoiceField(
        choices = State,
        help_text = 'Estado'
    )

    madre_ciudad = forms.CharField(
        help_text = 'Ciudad'
    )

    madre_calle = forms.CharField(
        help_text = 'Calle'
    )

    madre_codigo_postal = forms.CharField(
        help_text = 'Código Postal'
    )
    
    madre_colonia = forms.CharField(
        help_text = 'Colonia',
        label = 'Colonia'
    )
    
    madre_ocupacion = forms.CharField(
        help_text = 'Ocupación',
        label = 'Ocupación'
    )

    # formacion familia

    integrantes_familia = forms.IntegerField(
        help_text = 'Número de integrantes en la familia'
    )

    numero_hermanos = forms.IntegerField(
        help_text = 'Numero de hermanos',
    )

    lugar_dentro_familia = forms.CharField(
        help_text = 'Lugar dentro de la familia'
    )

    # relacion con:

    relacion_padre = forms.CharField(
        help_text = 'Relación con tu padre'
    )

    relacion_madre = forms.CharField(
        help_text = 'Relación con tu madre'
    )

    relacion_hermanos = forms.CharField(
        help_text = 'Relación con tus hermanos'
    )

    encargado_crianza = forms.CharField(
        help_text = 'Encargado de tu crianza'
    )

    # ocupacion

    trabajado_antes = forms.ChoiceField(
        choices = Trabajado,
        help_text='¿Has trabajado antes?'
    )

    puesto = forms.CharField(
        help_text = 'Puesto'
    )

    lugar_trabajo = forms.CharField(
        help_text = 'Lugar de trabajo'
    )

    jefe_inmediato = forms.CharField(
        help_text = 'Jefe inmediato'
    )

    telefono_jefe = PhoneNumberField(
        initial='+52',
        help_text='Teléfono'
    )

    trabajo_estado = forms.ChoiceField(
        choices = State,
        help_text = 'Estado'
    )

    trabajo_ciudad = forms.CharField(
        help_text = 'Ciudad'
    )

    trabajo_calle = forms.CharField(
        help_text = 'Calle',
        label = 'Calle'
    )

    trabajo_codigo_postal = forms.CharField(
        help_text = 'Código Postal',
        label='Código Postal'
    )
    
    trabajo_colonia = forms.CharField(
        help_text = 'Colonia',
        label='Colonia'
    )
    # Como conociste vida y familia

    referencia = forms.ChoiceField(
        choices = Referencia,
        help_text = 'Cómo conoció VIFAC'
    )

    visto_en = forms.CharField()

    canal = forms.CharField()

    otros = forms.CharField()

    # Datos Generales de la Persona

    nombre_recomendacion = forms.CharField()

    apellido_paterno_recomendacion = forms.CharField()

    apellido_materno_recomendacion = forms.CharField()

    relacion_recomendacion = forms.ChoiceField(
        choices = Relacion_Vives,
    )

    telefono_recomendacion = PhoneNumberField(
        initial = '+52'
    )

    # Dirección

    calle_recomendacion = forms.CharField(
        help_text = 'Calle'
    )

    numero_exterior = forms.CharField(
        help_text = 'Número'
    )

    codigo_postal_recomendacion = forms.CharField(
        help_text = 'Código Postal'
    )

    colonia = forms.CharField(
        help_text = 'Colonia'
    )

    ciudad_referencia = forms.CharField(
        help_text = 'Ciudad'
    )

    estado_referencia = forms.ChoiceField(
        choices = State,
        help_text = 'Estado'
    )

    tipo_de_ayuda = forms.ChoiceField(
        choices = Ayuda,
    )

    fecha_ultima_menstruacion = forms.DateField(
        help_text = 'Fecha de ultima menstruación'
    )

    fecha_de_parto_esperada = forms.DateField(
        help_text = 'Fecha esperada de parto'
    )

    # Referencias
    # Contacto de Emergencia

    nombre_emergencia = forms.CharField(
        help_text = 'Nombre contacto de emergencia'
    )

    apellido_paterno_emergencia = forms.CharField(
        help_text = 'Apellido paterno'
    )

    apellido_materno_emergencia = forms.CharField(
        help_text = 'Apellido materno'
    )

    relacion_emergencia = forms.ChoiceField(
        choices = Relacion_Vives,
        help_text = 'Relación con el contacto de emergencia'
    )

    telefono_emergencia = PhoneNumberField(
        initial = '+52'
    )

    codigo_postal_emergencia = forms.CharField(
        help_text = 'Código Postal'
    )

    colonia_emergencia = forms.CharField(
        help_text = 'Colonia'
    )

    ciudad_emergencia = forms.CharField(
        help_text = 'Ciudad'
    )

    estado_emergencia = forms.ChoiceField(
        choices = State,
        help_text = 'Estado'
    )
    
    calle_emergencia = forms.CharField(
        help_text = 'Calle'
    )
    
    # Referencia Médica

    control_medico = forms.BooleanField(
        help_text = 'Ha tenido control médico'
    )

    enfermedades_padecidas = forms.CharField(
        help_text = 'Enfermedades Padecidas'
    )

    nombre_medico = forms.CharField(
        help_text = 'Nombre del médico a cargo'
    )

    nombre_clinica = forms.CharField(
        help_text = 'Nombre de la clínica'
    )

    telefono_medico = PhoneNumberField(
        initial = '+52'
    )

    calle_medico = forms.CharField(
        help_text = 'Calle'
    )

    numero_exterior_medico = forms.CharField(
        help_text = 'Número de calle'
    )

    codigo_postal_medico = forms.CharField(
        help_text = 'Código Postal'
    )

    colonia_medico = forms.CharField()

    ciudad_medico = forms.CharField(
        help_text = 'Ciudad'
    )

    estado_medico = forms.ChoiceField(
        choices = State,
        help_text = 'Estado'
    )

    # Personal

    estado_de_animo = forms.CharField(
        help_text = 'Estado de ánimo'
    )

    infancia = forms.CharField(
        help_text = 'Descripción infancia'
    )

    # Embarazo

    tipo_embarazo = forms.ChoiceField(
        choices = Embarazo,
        help_text = 'Tipo de embarazo'
    )

    reaccion = forms.CharField(
        help_text = 'Reacción al embarazo'
    )

    apoyo_papa = forms.CharField(
        help_text = 'Apoyo del papá'
    )

    relacion_con_padre = forms.ChoiceField(
        choices = Relacion,
        help_text = 'Relación con el padre'
    )

    duracion_relacion = forms.CharField(
        help_text = 'Duración de la relación'
    )

    familiares = forms.CharField(
        help_text = 'Familiares que saben del embarazo'
    )

    actitud_familiares = forms.CharField(
        help_text = 'Actitud que espera de los familiares'
    )

    relacion_voluntaria = forms.ChoiceField(
        choices = Voluntario,
        help_text = 'Relaciones voluntarias'
    )

    comunicacion_padre = forms.BooleanField(
        help_text = 'Comunicación con el padre'
    )

    aborto_considerado = forms.BooleanField(
        help_text = 'Se consideró el abortó'
    )

    violencia_intrafamiliar = forms.BooleanField(
        help_text = 'Violencia intrafamiliar'
    )

    # Escolaridad

    maximo_grado_estudios = forms.ChoiceField(
        choices = Estudios,
        help_text = 'Máximo grado de estudios'
    )

    nombre_escuela = forms.CharField(
        help_text = 'Nombre de la institución escolar'
    )

    tiempo_cursado = forms.ChoiceField(
        choices = Duracion,
        help_text = 'Años cursados'
    )
