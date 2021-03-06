# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-01-23 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('species_mgr', '0006_species_abbreviation'),
        ('intermine_mgr', '0002_auto_20190828_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='intermine',
            name='species',
            field=models.ManyToManyField(blank=True, to='species_mgr.Species', verbose_name='species with FASTA/BLAST sequences'),
        ),
    ]
