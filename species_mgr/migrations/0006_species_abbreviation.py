# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-18 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('species_mgr', '0005_auto_20181004_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name="Abbreviation (if different from 'Gensp')"),
        ),
    ]
