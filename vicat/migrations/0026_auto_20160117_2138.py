# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0025_auto_20160117_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='active',
            field=models.BooleanField(default=False, verbose_name='\u0430\u043a\u0442\u0438\u0432'),
        ),
        migrations.AddField(
            model_name='series',
            name='torrent',
            field=models.CharField(blank=True, max_length=512, verbose_name='\u0442\u043e\u0440\u0440\u0435\u043d\u0442'),
        ),
        migrations.AddField(
            model_name='series',
            name='tosearch',
            field=models.BooleanField(default=False, verbose_name='\u0438\u0441\u043a\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='series',
            name='viewed',
            field=models.BooleanField(default=False, verbose_name='\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u043d'),
        ),
    ]
