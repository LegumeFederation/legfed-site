# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-11 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='location',
            field=models.CharField(default='', max_length=64),
        ),
    ]
