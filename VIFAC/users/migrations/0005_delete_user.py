# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 03:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170320_1919'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
