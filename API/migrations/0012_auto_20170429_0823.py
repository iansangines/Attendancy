# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-29 08:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0011_classe_assignatura'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClasseProfe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.ClasseAlumne')),
            ],
        ),
        migrations.RemoveField(
            model_name='classe',
            name='professorTutor',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='classes',
        ),
        migrations.AddField(
            model_name='professor',
            name='algo',
            field=models.CharField(default=datetime.datetime(2017, 4, 29, 8, 23, 31, 444390), max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classeprofe',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Professor'),
        ),
    ]
