# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-10 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0004_auto_20160410_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='name',
            field=models.CharField(max_length=5),
        ),
    ]
