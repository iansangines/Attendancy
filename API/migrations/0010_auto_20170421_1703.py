# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 17:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0009_auto_20170418_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assistencia',
            name='dispositiuAlumne',
        ),
        migrations.RemoveField(
            model_name='assistencia',
            name='horaEntrada',
        ),
        migrations.RemoveField(
            model_name='assistencia',
            name='horaSortida',
        ),
        migrations.AddField(
            model_name='assistencia',
            name='entrada',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 21, 17, 3, 57, 520923)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assistencia',
            name='sortida',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='assistencia',
            name='classeAlumne',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.ClasseAlumne'),
        ),
    ]