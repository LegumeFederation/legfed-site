# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-05 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_mgr', '0003_auto_20181005_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='text',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Text (if different from Organization)'),
        ),
    ]