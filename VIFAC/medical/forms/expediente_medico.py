from django import forms


class MedicoForm(forms.Form):
    nombre = forms.CharField(
        required=False,
        help_text='Nombre',
        label='Nombre de la beneficiaria'
    )

    tipo_sanguineo = forms.CharField(
        required=False,
        help_text='Tipo sanguineo',
        label='Tipo sanguineo'
    )

    edad = forms.IntegerField(
        label='Edad'
    )

    fecha_nacimiento = forms.DateField(
    )

    estado_civil = forms.CharField(
        required=False,
        help_text='Estado civil',
        label='Estado civil'
    )

    telefono = forms.CharField(
        required=False,
        max_length=12,
        help_text='Teléfono',
        label='Teléfono'
    )

    domicilio = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Domicilio',
        label='Domicilio'
    )

    padre_bebe = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Nombre del padre',
        label='Nombre del padre'
    )

    edad_padre = forms.IntegerField(
        label='Edad del padre'
    )

    apoyo = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Apoyo',
        label='Apoyo'
    )

    FUM = forms.DateField(
        label='FUM'
    )

    ciclos = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Ciclos',
        label='Ciclos'
    )

    uso_anticonceptivos_FUM = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Ciclos',
        label='Ciclos'
    )

    fppxfum = forms.CharField(
        required=False,
        max_length=1024,
        help_text='FPP X FUM',
        label='FPP X FUM'
    )

    fppxusg = forms.CharField(
        required=False,
        max_length=1024,
        help_text='FPP X USG',
        label='FPP X USG'
    )

    fpp_definitiva = forms.CharField(
        required=False,
        max_length=1024,
        help_text='FPP definitiva',
        label='FPP definitiva'
    )

    G = forms.CharField(
        required=False,
        max_length=1024,
        help_text='G',
        label='G'
    )

    P = forms.CharField(
        required=False,
        max_length=1024,
        help_text='P',
        label='P'
    )

    termino = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Termino',
        label='Termino'
    )

    Ab = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Ab',
        label='Ab'
    )

    ectop = forms.CharField(
        required=False,
        max_length=1024,
        help_text='ectop',
        label='ectop'
    )

    multiples = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Multiples',
        label='Multiples'
    )

    cesarea = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Cesarea',
        label='Cesarea'
    )

    medicamento_desde_fum = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Medicamento o droga desde FUM',
        label='Medicamento o droga desde FUM'
    )

    contacto_con_enfermedad_infecciosa_fum = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Contacto con enfermedad infecciosa desde FUM',
        label='Contacto con enfermedad infecciosa desde FUM'
    )

    embarazos_anteriores = forms.IntegerField(
        label='Embarazos anteriores'
    )

    app = forms.CharField(
        required=False,
        max_length=1024,
        help_text='APP',
        label='APP'
    )

    medicamentos = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Medicamentos',
        label='Medicamentos'
    )

    cirugias = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Cirugias',
        label='Cirugias'
    )

    alergias = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Alergias',
        label='Alergias'
    )


    apnp_fuma = forms.CharField(
        required=False,
        max_length=1024,
        help_text='APNP Fuma',
        label='APNP Fuma'
    )


    alcohol = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Alcohol',
        label='Alcohol'
    )

    droga = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Droga',
        label='Droga'
    )

    trabajo = forms.CharField(
        required=False,
        max_length=1024,
        help_text='Trabajo',
        label='Trabajo'
    )

    ahf = forms.CharField(
        required=False,
        max_length=1024,
        help_text='AHF',
        label='AHF'
    )

    ahf_padre = forms.CharField(
        required=False,
        max_length=1024,
        help_text='APP AHF Padre',
        label='APP AHF Padre'
    )
