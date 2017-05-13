# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-13 10:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assistencia',
            name='data',
            field=models.DateField(default=datetime.date(2017, 5, 13)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assistencia',
            name='entrada',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='assistencia',
            name='sortida',
            field=models.TimeField(null=True),
        ),
    ]
