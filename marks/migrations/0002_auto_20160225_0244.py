# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(default='email', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.CharField(default='password', max_length=16),
            preserve_default=False,
        ),
    ]
