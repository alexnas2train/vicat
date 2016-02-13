# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-12 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0061_auto_20160207_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='image_series',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='\u0444\u043e\u0442\u043e \u0441\u0435\u0440\u0438\u0430\u043b\u0430'),
        ),
        migrations.AlterField(
            model_name='series',
            name='preview_episode',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='\u0444\u043e\u0442\u043e \u044d\u043f\u0438\u0437\u043e\u0434\u0430'),
        ),
        migrations.AlterField(
            model_name='series',
            name='preview_series',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='\u0444\u043e\u0442\u043e \u0441\u0435\u0440\u0438\u0430\u043b\u0430'),
        ),
    ]