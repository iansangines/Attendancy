# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-16 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20170513_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='horaFinal',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='classe',
            name='horaInici',
            field=models.DateTimeField(),
        ),
    ]