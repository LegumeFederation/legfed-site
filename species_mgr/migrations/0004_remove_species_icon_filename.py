# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-04 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('species_mgr', '0003_species_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='species',
            name='icon_filename',
        ),
    ]