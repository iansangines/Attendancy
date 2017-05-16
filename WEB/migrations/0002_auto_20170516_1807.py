# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-16 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='calendarevent',
            name='start',
            field=models.DateTimeField(verbose_name='Start Date'),
        ),
    ]
