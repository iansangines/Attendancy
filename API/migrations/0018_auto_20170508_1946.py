# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0017_auto_20170508_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classe',
            name='dies',
        ),
        migrations.AddField(
            model_name='classe',
            name='dia',
            field=models.CharField(blank=True, choices=[(b'dilluns', 'Dilluns'), (b'dimarts', 'Dimarts'), (b'dimecres', 'Dimecres'), (b'dijous', 'Dijous'), (b'divendres', 'Divendres')], max_length=10),
        ),
    ]
