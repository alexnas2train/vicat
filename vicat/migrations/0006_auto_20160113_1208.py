# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 06:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0005_auto_20160111_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='series_id',
        ),
        migrations.AddField(
            model_name='episode',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vicat.Series'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='episode',
            name='description',
            field=models.CharField(default='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u0435 \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u043e', max_length=512, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='series',
            name='description',
            field=models.CharField(default='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u0435 \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u043e', max_length=512, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='series',
            name='preview',
            field=models.CharField(blank=True, help_text='\u043a\u0430\u0434\u0440 \u0438\u0437 \u0441\u0435\u0440\u0438\u0430\u043b\u0430', max_length=128, verbose_name='\u0444\u043e\u0442\u043e'),
        ),
    ]
