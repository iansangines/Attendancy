# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 18:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_auto_20170416_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumne',
            name='dni',
            field=models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(message=b'El DNI/NIE no es valid', regex=b' (([X-Z]{1})([-]?)(\\d{7})([-]?)([A-Z]{1}))|((\\d{8})([-]?)([A-Z]{1}))')]),
        ),
        migrations.AlterField(
            model_name='dispositiu',
            name='MAC',
            field=models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(code=b'invalid_mac', message=b'MAC no valida', regex=b'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')]),
        ),
        migrations.AlterField(
            model_name='sala',
            name='MAC',
            field=models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(code=b'invalid_mac', message=b'MAC no valida', regex=b'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')]),
        ),
    ]