# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-24 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0012_coordinator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='first_sessional',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='marks',
            name='second_sessional',
            field=models.FloatField(null=True),
        ),
    ]
