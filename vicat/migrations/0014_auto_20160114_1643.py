# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0013_series_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='slug',
            field=models.SlugField(),
        ),
    ]
