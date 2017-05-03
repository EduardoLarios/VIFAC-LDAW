from django.db import models
# Create your models here.


class Exp_Medico(models.Model):
    
    nombre = models.CharField(
        null = False,
        verbose_name='Nombre',
        max_length=1024,
        default=''
    )
    
    tipo_sanguineo = models.CharField(
        null = False,
        verbose_name='Tipo sanguineo',
        max_length=24,
        default=''
    )
    
    edad = models.IntegerField(
        null = False,
        verbose_name='Edad',
    )
    
    fecha_nacimiento = models.DateField(
        null = False,
        verbose_name='Fecha nacimiento',
    )
    
    estado_civil = models.CharField(
        null = True,
        verbose_name='Estado Civil',
        max_length=1024,
        default=''
    )
    
    telefono = models.CharField(
        null = True,
        verbose_name='Telefono',
        max_length=12,
        default=''
    )
    
    domicilio = models.CharField(
        null = True,
        verbose_name='Domicilio',
        max_length=1024,
        default=''
    )
    
    padre_bebe = models.CharField(
        null = True,
        verbose_name='Nombre del padre',
        max_length=1024,
        default=''
    )
    
    edad_padre = models.IntegerField(
        null = True,
        verbose_name='Edad',
    )
    
    apoyo = models.CharField(
        null = True,
        verbose_name='Apoyo',
        max_length=1024,
        default=''
    )
    
    FUM = models.DateField(
        null = True,
        verbose_name='FUM',
    )

    ciclos = models.CharField(
        null = True,
        verbose_name='Nombre',
        max_length=512,
        default=''
    )

    uso_anticonceptivos_FUM = models.CharField(
        null = True,
        max_length=512,
        verbose_name='Uso de anticonceptivos',
        default=''
    )

    fppxfum = models.CharField(
        null = True,
        verbose_name='FFP x FUM',
        max_length=512,
        default=''
    )
    
    fppxusg = models.CharField(
        null = True,
        verbose_name='FFP x USG',
        max_length=512,
        default=''
    )
    
    fpp_definitiva = models.CharField(
        null = True,
        verbose_name='FFP definitiva',
        max_length=512,
        default=''
    )
    
    G = models.CharField(
        null = True,
        verbose_name='G',
        max_length=512,
        default=''
    )
    
    P = models.CharField(
        null = True,
        verbose_name='P',
        max_length=512,
        default=''
    )
    
    termino = models.CharField(
        null = True,
        verbose_name='Término',
        max_length=512,
        default=''
    )
    
    Ab = models.CharField(
        null = True,
        verbose_name='Término',
        max_length=512,
        default=''
    )
    
    ectop = models.CharField(
        null = True,
        verbose_name='Ectop',
        max_length=512,
        default=''
    )
    
    multiples = models.CharField(
        null = True,
        verbose_name='Múltiples',
        max_length=512,
        default=''
    )
    
    cesarea = models.CharField(
        null = True,
        verbose_name='Cesárea',
        max_length=512,
        default=''
    )
    
    medicamento_desde_fum = models.CharField(
        null = True,
        verbose_name='Medicamentos/Droga desde FUM',
        max_length=512,
        default=''
    )
    
    contacto_con_enfermedad_infecciosa_fum = models.CharField(
        null = True,
        verbose_name='Contacto con enfermedad infecciosa desde fum',
        max_length=512,
        default=''
    )
    
    embarazos_anteriores = models.IntegerField(
        null = True,
        verbose_name='Embarazos anteriores',
        default=0
    )
    
    app = models.CharField(
        null = True,
        verbose_name='APP',
        max_length=512,
        default=''
    )
    
    medicamentos = models.CharField(
        null = True,
        verbose_name='Medicamentos',
        max_length=512,
        default=''
    )
    
    cirugias = models.CharField(
        null = True,
        verbose_name='Cirugias',
        max_length=512,
        default=''
    )
    
    alergias = models.CharField(
        null = True,
        verbose_name='alergias',
        max_length=512,
        default=''
    )
    
    apnp_fuma = models.CharField(
        null = True,
        verbose_name='apnp fuma',
        max_length=512,
        default=''
    )
    
    alcohol = models.CharField(
        null = True,
        verbose_name='alcohol',
        max_length=512,
        default=''
    )
    
    droga = models.CharField(
        null = True,
        verbose_name='droga',
        max_length=512,
        default=''
    )
    
    trabajo = models.CharField(
        null = True,
        verbose_name='trabajo',
        max_length=512,
        default=''
    )
    
    ahf = models.CharField(
        null = True,
        verbose_name='ahf',
        max_length=512,
        default=''
    )
    
    ahf_padre = models.CharField(
        null = True,
        verbose_name='app/ahf del padre del bebe',
        max_length=512,
        default=''
    )

    def __str__(self):
        return self.nombre
