# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-22 00:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20181121_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='column',
            old_name='nav_dispaly',
            new_name='nav_display',
        ),
    ]
