# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-01 22:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('resource_mgr', '0008_auto_20181101_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='icon',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Organization_icons', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
