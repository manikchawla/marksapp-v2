# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-23 22:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0010_auto_20160421_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks',
            name='external_practical',
        ),
        migrations.RemoveField(
            model_name='marks',
            name='internal_practical',
        ),
    ]