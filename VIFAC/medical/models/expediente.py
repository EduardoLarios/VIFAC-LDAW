from django.db import models

# Create your models here.


class Exp_Medico(models.Model):
    
    nombre = models.CharField(
        verbose_name='Nombre',
        max_length=1024,
        default=''
    )
    
    tipo_sanguineo = models.CharField(
        verbose_name='Tipo sanguineo',
        max_length=24,
        default=''
    )
    
    edad = models.IntegerField(
        verbose_name='Edad',
    )
    
    fecha_nacimiento = models.DateField(
        verbose_name='Fecha nacimiento',
    )
    
    estado_civil = models.CharField(
        verbose_name='Estado Civil',
        max_length=1024,
        default=''
    )
    
    telefono = models.CharField(
        verbose_name='Telefono',
        max_length=12,
        default=''
    )
    
    domicilio = models.CharField(
        verbose_name='Domicilio',
        max_length=1024,
        default=''
    )
    
    padre_bebe = models.CharField(
        verbose_name='Nombre del padre',
        max_length=1024,
        default=''
    )
    
    edad_padre = models.IntegerField(
        verbose_name='Edad',
    )
    
    apoyo = models.CharField(
        verbose_name='Apoyo',
        max_length=1024,
        default=''
    )
    
    FUM = models.DateField(
        verbose_name='FUM',
    )

    ciclos = models.CharField(
        verbose_name='Nombre',
        max_length=512,
        default=''
    )

    uso_anticonceptivos_FUM = models.CharField(
        max_length=512,
        verbose_name='Uso de anticonceptivos',
        default=''
    )

    fppxfum = models.CharField(
        verbose_name='FFP x FUM',
        max_length=512,
        default=''
    )
    
    fppxusg = models.CharField(
        verbose_name='FFP x USG',
        max_length=512,
        default=''
    )
    
    fpp_definitiva = models.CharField(
        verbose_name='FFP definitiva',
        max_length=512,
        default=''
    )
    
    G = models.CharField(
        verbose_name='G',
        max_length=512,
        default=''
    )
    
    P = models.CharField(
        verbose_name='P',
        max_length=512,
        default=''
    )
    
    termino = models.CharField(
        verbose_name='Término',
        max_length=512,
        default=''
    )
    
    Ab = models.CharField(
        verbose_name='Término',
        max_length=512,
        default=''
    )
    
    ectop = models.CharField(
        verbose_name='Ectop',
        max_length=512,
        default=''
    )
    
    multiples = models.CharField(
        verbose_name='Múltiples',
        max_length=512,
        default=''
    )
    
    cesarea = models.CharField(
        verbose_name='Cesárea',
        max_length=512,
        default=''
    )
    
    medicamento_desde_fum = models.CharField(
        verbose_name='Medicamentos/Droga desde FUM',
        max_length=512,
        default=''
    )
    
    contacto_con_enfermedad_infecciosa_fum = models.CharField(
        verbose_name='Contacto con enfermedad infecciosa desde fum',
        max_length=512,
        default=''
    )
    
    embarazos_anteriores = models.IntegerField(
        verbose_name='Embarazos anteriores',
        default=0
    )
    
    app = models.CharField(
        verbose_name='APP',
        max_length=512,
        default=''
    )
    
    medicamentos = models.CharField(
        verbose_name='Medicamentos',
        max_length=512,
        default=''
    )
    
    cirugias = models.CharField(
        verbose_name='Cirugias',
        max_length=512,
        default=''
    )
    
    alergias = models.CharField(
        verbose_name='alergias',
        max_length=512,
        default=''
    )
    
    apnp_fuma = models.CharField(
        verbose_name='apnp fuma',
        max_length=512,
        default=''
    )
    
    alcohol = models.CharField(
        verbose_name='alcohol',
        max_length=512,
        default=''
    )
    
    droga = models.CharField(
        verbose_name='droga',
        max_length=512,
        default=''
    )
    
    trabajo = models.CharField(
        verbose_name='trabajo',
        max_length=512,
        default=''
    )
    
    ahf = models.CharField(
        verbose_name='ahf',
        max_length=512,
        default=''
    )
    
    ahf_padre = models.CharField(
        verbose_name='app/ahf del padre del bebe',
        max_length=512,
        default=''
    )