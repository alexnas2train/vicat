# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0026_auto_20160117_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='show_type',
            field=models.CharField(blank=True, max_length=256, verbose_name='\u0442\u0438\u043f \u043f\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438'),
        ),
    ]
