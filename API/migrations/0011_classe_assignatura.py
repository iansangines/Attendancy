# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0010_auto_20170421_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe',
            name='assignatura',
            field=models.CharField(default='none', max_length=256),
            preserve_default=False,
        ),
    ]
