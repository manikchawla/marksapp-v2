# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-10 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0003_auto_20160410_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='subjects',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='course',
        ),
        migrations.AddField(
            model_name='batch',
            name='subjects',
            field=models.ManyToManyField(to='marks.Subject'),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
