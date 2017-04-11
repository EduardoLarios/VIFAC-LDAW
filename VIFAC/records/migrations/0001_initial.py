# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 01:24
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre', max_length=256, verbose_name='Nombre')),
                ('apellido_paterno', models.CharField(help_text='Apellido Paterno', max_length=256, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(help_text='Apellido Materno', max_length=256, verbose_name='Apellido Materno')),
                ('edad', models.IntegerField(blank=True, help_text='Edad', verbose_name='Edad')),
                ('telefono_casa', models.CharField(blank=True, default='', help_text='Telefono de casa', max_length=10, verbose_name='Telefono de casa')),
                ('telefono_particular', models.CharField(blank=True, default='', help_text='Telefono de particular', max_length=10, verbose_name='Telefono particular')),
                ('fecha_nacimiento', models.DateField(blank=True)),
                ('estado_civil', models.CharField(choices=[('Soltera', 'Soltera'), ('Casada', 'Casada'), ('Divorciada', 'Divorciada'), ('Viuda', 'Viuda'), ('Unión Libre', 'Unión Libre')], help_text='Estado Civil', max_length=128, verbose_name='Estado Civil')),
                ('migrante', models.BooleanField(default=False)),
                ('estado', models.CharField(blank=True, choices=[('Ninguno', 'Ninguno'), ('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('Chiapas', 'Chiapas'), ('Chihuahua', 'Chihuahua'), ('CDMX', 'Ciudad de México'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Estado de México', 'Estado de México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Roo', 'Quintana Roo'), ('San Luis Potosí', 'San Luis Potosí'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], default='', help_text='Estado', max_length=256, verbose_name='Estado')),
                ('ciudad', models.CharField(blank=True, default='', help_text='Ciudad', max_length=256, verbose_name='Ciudad')),
                ('calle', models.CharField(blank=True, default='', help_text='Calle', max_length=256, verbose_name='Calle')),
                ('codigo_postal', models.CharField(blank=True, default='', help_text='Codigo Postal', max_length=128, verbose_name='Codigo Postal')),
                ('vives_nombre', models.CharField(help_text='Nombre', max_length=256, verbose_name='Nombre')),
                ('vives_apellido_paterno', models.CharField(help_text='Apellido Paterno', max_length=256, verbose_name='Apellido Paterno')),
                ('vives_apellido_materno', models.CharField(help_text='Apellido Materno', max_length=256, verbose_name='Apellido Materno')),
                ('tipo_relacion_vives', models.CharField(blank=True, choices=[('Padre', 'Padre'), ('Madre', 'Madre'), ('Hermano', 'Hermano'), ('Primo', 'Primo'), ('Tío', 'Tío'), ('Abuelo', 'Abuelo'), ('Amigo', 'Amigo'), ('Otro', 'Otro')], default='', help_text='Con quien vives', max_length=128, verbose_name='Con quien vives')),
                ('telefono_vives', models.CharField(blank=True, default='', help_text='Telefono de la persona con quien vives', max_length=8, verbose_name='Telefono')),
                ('estado_vives', models.CharField(blank=True, choices=[('Ninguno', 'Ninguno'), ('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('Chiapas', 'Chiapas'), ('Chihuahua', 'Chihuahua'), ('CDMX', 'Ciudad de México'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Estado de México', 'Estado de México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Roo', 'Quintana Roo'), ('San Luis Potosí', 'San Luis Potosí'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], default='', help_text='Estado', max_length=256, verbose_name='Estado')),
                ('ciudad_vives', models.CharField(blank=True, default='', help_text='Ciudad', max_length=256, verbose_name='Ciudad')),
                ('calle_vives', models.CharField(blank=True, default='', help_text='Calle', max_length=256, verbose_name='Calle')),
                ('codigo_postal_vives', models.CharField(blank=True, default='', help_text='Codigo Postal', max_length=128, verbose_name='Codigo Postal')),
                ('vive_padre', models.BooleanField(default=True)),
                ('padre_nombre', models.CharField(default='', help_text='Nombre', max_length=256, verbose_name='Nombre')),
                ('padre_apellido_paterno', models.CharField(blank=True, help_text='Apellido Paterno', max_length=256, verbose_name='Apellido Paterno')),
                ('padre_apellido_materno', models.CharField(blank=True, help_text='Apellido Materno', max_length=256, verbose_name='Apellido Materno')),
                ('padre_telefono_casa', models.CharField(blank=True, default='', help_text='Telefono de casa', max_length=8, verbose_name='Telefono de casa')),
                ('padre_telefono_particular', models.CharField(blank=True, default='', help_text='Telefono de particular', max_length=8, verbose_name='Telefono particular')),
                ('padre_fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('padre_estado_civil', models.CharField(blank=True, choices=[('Soltera', 'Soltera'), ('Casada', 'Casada'), ('Divorciada', 'Divorciada'), ('Viuda', 'Viuda'), ('Unión Libre', 'Unión Libre')], help_text='Estado Civil', max_length=128, verbose_name='Estado Civil')),
                ('padre_estado', models.CharField(blank=True, choices=[('Ninguno', 'Ninguno'), ('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('Chiapas', 'Chiapas'), ('Chihuahua', 'Chihuahua'), ('CDMX', 'Ciudad de México'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Estado de México', 'Estado de México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Roo', 'Quintana Roo'), ('San Luis Potosí', 'San Luis Potosí'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], default='', help_text='Estado', max_length=256, verbose_name='Estado')),
                ('padre_ciudad', models.CharField(blank=True, default='', help_text='Ciudad', max_length=256, verbose_name='Ciudad')),
                ('padre_calle', models.CharField(blank=True, default='', help_text='Calle', max_length=256, verbose_name='Calle')),
                ('padre_codigo_postal', models.CharField(blank=True, default='', help_text='Codigo Postal', max_length=128, verbose_name='Codigo Postal')),
                ('vive_madre', models.BooleanField(default=True)),
                ('madre_nombre', models.CharField(default='', help_text='Nombre', max_length=256, verbose_name='Nombre')),
                ('madre_apellido_paterno', models.CharField(blank=True, help_text='Apellido Paterno', max_length=256, verbose_name='Apellido Paterno')),
                ('madre_apellido_materno', models.CharField(blank=True, help_text='Apellido Materno', max_length=256, verbose_name='Apellido Materno')),
                ('madre_telefono_casa', models.CharField(blank=True, default='', help_text='Telefono de casa', max_length=8, verbose_name='Telefono de casa')),
                ('madre_telefono_particular', models.CharField(blank=True, default='', help_text='Telefono de particular', max_length=8, verbose_name='Telefono particular')),
                ('madre_fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('madre_estado_civil', models.CharField(blank=True, choices=[('Soltera', 'Soltera'), ('Casada', 'Casada'), ('Divorciada', 'Divorciada'), ('Viuda', 'Viuda'), ('Unión Libre', 'Unión Libre')], help_text='Estado Civil', max_length=128, verbose_name='Estado Civil')),
                ('madre_migrante', models.BooleanField(default=False)),
                ('madre_estado', models.CharField(blank=True, choices=[('Ninguno', 'Ninguno'), ('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('Chiapas', 'Chiapas'), ('Chihuahua', 'Chihuahua'), ('CDMX', 'Ciudad de México'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Estado de México', 'Estado de México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Roo', 'Quintana Roo'), ('San Luis Potosí', 'San Luis Potosí'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], default='', help_text='Estado', max_length=256, verbose_name='Estado')),
                ('madre_ciudad', models.CharField(blank=True, default='', help_text='Ciudad', max_length=256, verbose_name='Ciudad')),
                ('madre_calle', models.CharField(blank=True, default='', help_text='Calle', max_length=256, verbose_name='Calle')),
                ('madre_codigo_postal', models.CharField(blank=True, default='', help_text='Codigo Postal', max_length=128, verbose_name='Codigo Postal')),
                ('integrantes_familia', models.IntegerField(blank=True, default=0, help_text='Numero de integrantes en la familia', verbose_name='Numero de integrantes')),
                ('numero_hermanos', models.IntegerField(blank=True, default=0, help_text='Numero de hermanos', verbose_name='Numero de hermanos')),
                ('lugar_dentro_familia', models.CharField(blank=True, help_text='Lugar dentro de la familia', max_length=128, verbose_name='Lugar dentro de la familia')),
                ('relacion_padre', models.CharField(blank=True, help_text='Relación con tu padre', max_length=512, verbose_name='Relación con tu padre')),
                ('relacion_madre', models.CharField(blank=True, help_text='Relación con tu madre', max_length=512, verbose_name='Relación con tu madre')),
                ('relacion_hermanos', models.CharField(blank=True, help_text='Relación con tus hermanos', max_length=512, verbose_name='Relación con tus hermanos')),
                ('encargado_crianza', models.CharField(blank=True, help_text='Encargado de tu crianza', max_length=256, verbose_name='Encargado de tu crianza')),
                ('trabajado_antes', models.BooleanField(default=False)),
                ('puesto', models.CharField(blank=True, help_text='Puesto', max_length=256, verbose_name='Puesto de trabajo')),
                ('lugar_trabajo', models.CharField(blank=True, help_text='Lugar de trabajo', max_length=256, verbose_name='Lugar trabajo')),
                ('jefe_inmediato', models.CharField(blank=True, default='', help_text='Jefe inmediato', max_length=256, verbose_name='Jefe inmediato')),
                ('telefono_jefe', models.CharField(blank=True, default='', max_length=24)),
                ('trabajo_estado', models.CharField(blank=True, choices=[('Ninguno', 'Ninguno'), ('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('Chiapas', 'Chiapas'), ('Chihuahua', 'Chihuahua'), ('CDMX', 'Ciudad de México'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Estado de México', 'Estado de México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Roo', 'Quintana Roo'), ('San Luis Potosí', 'San Luis Potosí'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], default='', help_text='Estado', max_length=256, verbose_name='Estado')),
                ('trabajo_ciudad', models.CharField(blank=True, default='', help_text='Ciudad', max_length=256, verbose_name='Ciudad')),
                ('trabajo_calle', models.CharField(blank=True, default='', help_text='Calle', max_length=256, verbose_name='Calle')),
                ('trabajo_codigo_postal', models.CharField(blank=True, default='', help_text='Codigo Postal', max_length=128, verbose_name='Codigo Postal')),
                ('referencia', models.CharField(blank=True, choices=[('Amistad', 'Amistad'), ('Periodico', 'Periodico'), ('Familiar', 'Familiar'), ('Trabajo', 'Trabajo'), ('Volante', 'Volante'), ('Sopt TV', 'Sopt TV'), ('Página web', 'Página web'), ('Migración', 'Migración')], default='', help_text='Cómo conoció VIFAC', max_length=256, verbose_name='Referencia')),
                ('visto_en', models.CharField(blank=True, default='', max_length=256, verbose_name='Dónde se ha visto la referencia')),
                ('canal', models.CharField(blank=True, default='', max_length=256, verbose_name='Canal donde se ha visto la referencia')),
                ('otros', models.CharField(blank=True, default='', max_length=256, verbose_name='Otro medio donde se ha visto la referencia')),
                ('nombre_recomendacion', models.CharField(blank=True, default='', max_length=64, verbose_name='Nombre persona')),
                ('apellido_paterno_recomendacion', models.CharField(blank=True, default='', max_length=64, verbose_name='Apellido paterno')),
                ('apellido_materno_recomendacion', models.CharField(blank=True, default='', max_length=64, verbose_name='Apellido materno')),
                ('relacion_recomendacion', models.CharField(blank=True, choices=[('Padre', 'Padre'), ('Madre', 'Madre'), ('Hermano', 'Hermano'), ('Primo', 'Primo'), ('Tío', 'Tío'), ('Abuelo', 'Abuelo'), ('Amigo', 'Amigo'), ('Otro', 'Otro')], default='', max_length=1024, verbose_name='Relación con la persona que recomienda')),
                ('telefono_recomendacion', phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128)),
                ('calle_recomendacion', models.CharField(blank=True, default='', help_text='Calle', max_length=256, verbose_name='Calle')),
                ('numero_exterior', models.CharField(blank=True, default='', help_text='Número', max_length=8, verbose_name='Número')),
                ('codigo_postal_recomendacion', models.CharField(blank=True, default='', help_text='Codigo Postal', max_length=8, verbose_name='Codigo Postal')),
                ('colonia', models.CharField(blank=True, default='', max_length=128, verbose_name='Colonia')),
                ('ciudad_referencia', models.CharField(blank=True, default='', help_text='Ciudad', max_length=64, verbose_name='Ciudad')),
                ('estado_referencia', models.CharField(blank=True, choices=[('Ninguno', 'Ninguno'), ('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('Chiapas', 'Chiapas'), ('Chihuahua', 'Chihuahua'), ('CDMX', 'Ciudad de México'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Estado de México', 'Estado de México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Roo', 'Quintana Roo'), ('San Luis Potosí', 'San Luis Potosí'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], default='', help_text='Estado', max_length=1024, verbose_name='Estado')),
                ('tipo_de_ayuda', models.CharField(blank=True, choices=[('Otro', 'Otro'), ('Interna', 'Interna'), ('Externa', 'Externa')], default='', max_length=1024, verbose_name='Tipo de ayuda')),
                ('fecha_ultima_menstruacion', models.DateField(blank=True, default=None, verbose_name='Fecha de última menstruación')),
                ('fecha_de_parto_esperada', models.DateField(blank=True, default=None, verbose_name='Fecha esperada de parto')),
                ('nombre_emergencia', models.CharField(blank=True, default='', help_text='Nombre contacto de emergencia', max_length=64, verbose_name='Nombre')),
                ('apellido_paterno_emergencia', models.CharField(blank=True, default='', max_length=64, verbose_name='Apellido paterno')),
                ('apellido_materno_emergencia', models.CharField(blank=True, default='', max_length=64, verbose_name='Apellido materno')),
                ('relacion_emergencia', models.CharField(blank=True, choices=[('Padre', 'Padre'), ('Madre', 'Madre'), ('Hermano', 'Hermano'), ('Primo', 'Primo'), ('Tío', 'Tío'), ('Abuelo', 'Abuelo'), ('Amigo', 'Amigo'), ('Otro', 'Otro')], default='', max_length=1024, verbose_name='Relación con el contacto de emergencia')),
                ('telefono_emergencia', phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128)),
                ('codigo_postal_emergencia', models.CharField(blank=True, default='', help_text='Codigo Postal', max_length=8, verbose_name='Codigo Postal')),
                ('colonia_emergencia', models.CharField(blank=True, default='', max_length=128, verbose_name='Colonia')),
                ('ciudad_emergencia', models.CharField(blank=True, default='', help_text='Ciudad', max_length=64, verbose_name='Ciudad')),
                ('estado_emergencia', models.CharField(blank=True, choices=[('Ninguno', 'Ninguno'), ('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('Chiapas', 'Chiapas'), ('Chihuahua', 'Chihuahua'), ('CDMX', 'Ciudad de México'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Estado de México', 'Estado de México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Roo', 'Quintana Roo'), ('San Luis Potosí', 'San Luis Potosí'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], default='', help_text='Estado', max_length=1024, verbose_name='Estado')),
                ('control_medico', models.BooleanField(default=False, verbose_name='Ha tenido control médico')),
                ('enfermedades_padecidas', models.CharField(blank=True, default='', max_length=128, verbose_name='Enfermedades Padecidas')),
                ('nombre_medico', models.CharField(blank=True, default='', max_length=256, verbose_name='Nombre del médico a cargo')),
                ('nombre_clinica', models.CharField(blank=True, default='', max_length=256, verbose_name='Nombre de la clínica')),
                ('telefono_medico', phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128)),
                ('calle_medico', models.CharField(blank=True, default='', help_text='Calle', max_length=256, verbose_name='Calle')),
                ('numero_exterior_medico', models.CharField(blank=True, default='', help_text='Número de calle', max_length=8, verbose_name='Número de calle')),
                ('codigo_postal_medico', models.CharField(blank=True, default='', help_text='Codigo Postal', max_length=8, verbose_name='Codigo Postal')),
                ('colonia_medico', models.CharField(blank=True, default='', max_length=128, verbose_name='Colonia')),
                ('ciudad_medico', models.CharField(blank=True, default='', help_text='Ciudad', max_length=256, verbose_name='Ciudad')),
                ('estado_medico', models.CharField(blank=True, choices=[('Ninguno', 'Ninguno'), ('Aguascalientes', 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('Chiapas', 'Chiapas'), ('Chihuahua', 'Chihuahua'), ('CDMX', 'Ciudad de México'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('Estado de México', 'Estado de México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Roo', 'Quintana Roo'), ('San Luis Potosí', 'San Luis Potosí'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], default='', help_text='Estado', max_length=1024, verbose_name='Estado')),
                ('estado_de_animo', models.CharField(blank=True, default='', max_length=1024, verbose_name='Estado de ánimo')),
                ('infancia', models.CharField(blank=True, default='', max_length=1024, verbose_name='Descripción infancia')),
                ('tipo_embarazo', models.CharField(blank=True, choices=[('Deseado', 'Deseado'), ('Planeado', 'Planeado'), ('Inesperado', 'Inesperado'), ('Rechazado', 'Rechazado'), ('Otro', 'Otro')], default='', max_length=1024, verbose_name='Tipo de embarazo')),
                ('reaccion', models.CharField(blank=True, default='', max_length=1024, verbose_name='Reacción al embarazo')),
                ('apoyo_papa', models.CharField(blank=True, default='', max_length=1024, verbose_name='Apoyo del papá')),
                ('relacion_con_padre', models.CharField(blank=True, choices=[('Casados por la Iglesia', 'Casados por la Iglesia'), ('Casador por el civil', 'Casador por el civil'), ('Aventura', 'Aventura'), ('Violación', 'Violación'), ('Noviazgo', 'Noviazgo'), ('Otro', 'Otro')], default='', max_length=1024, verbose_name='Relación con el padre')),
                ('duracion_relacion', models.CharField(blank=True, default='', max_length=64, verbose_name='Duración de la relación')),
                ('familiares', models.CharField(blank=True, default='', max_length=512, verbose_name='Familiares que saben del embarazo')),
                ('actitud_familiares', models.CharField(blank=True, default='', max_length=512, verbose_name='Actitud que espera de los familiares')),
                ('relacion_voluntaria', models.CharField(blank=True, choices=[('Sí', 'Sí'), ('No', 'No'), ('No respondió', 'No respondió')], default='', max_length=1024, verbose_name='Relaciones voluntarias')),
                ('comunicacion_padre', models.BooleanField(default=True, verbose_name='Comunicación con el padre')),
                ('aborto_considerado', models.BooleanField(default=False, verbose_name='Se consideró el abortó')),
                ('violencia_intrafamiliar', models.BooleanField(default=False, verbose_name='Violencia intrafamiliar')),
                ('maximo_grado_estudios', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('6+', '6+'), ('Otro', 'Otro')], default='Otro', max_length=1024, verbose_name='Máximo grado de estudios')),
                ('nombre_escuela', models.CharField(blank=True, default='', max_length=128, verbose_name='Nombre de la institución escolar')),
                ('tiempo_cursado', models.CharField(blank=True, choices=[('Sin Estudios', 'Sin Estudios'), ('Primaria', 'Primaria'), ('Secundaria', 'Secundaria'), ('Preparatoria', 'Preparatoria'), ('Técnico', 'Técnico'), ('Licenciatura', 'Licenciatura'), ('Postgrado', 'Postgrado'), ('Otro', 'Otro')], default='Otro', max_length=1024, verbose_name='Años cursados')),
            ],
        ),
    ]
