# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0010_auto_20160114_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='title',
            field=models.CharField(max_length=128, unique=True, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
    ]