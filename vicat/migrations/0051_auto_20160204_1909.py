# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0050_series_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='slug',
            field=models.SlugField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='series',
            name='im_sourse',
            field=models.ImageField(blank=True, default='images/None/no_img_ser.jpg', upload_to='images/', verbose_name='\u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a \u0444\u043e\u0442\u043e'),
        ),
        migrations.AlterField(
            model_name='series',
            name='preview',
            field=models.CharField(blank=True, default='images/none/no_img_series.jpg', max_length=128, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u043e\u0442\u043e'),
        ),
    ]
