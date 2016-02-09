# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0057_auto_20160206_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='preview',
            field=models.CharField(blank=True, default='images/None/no_img_epis.jpg', max_length=128, null=True, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u043e\u0442\u043e'),
        ),
        migrations.AlterField(
            model_name='series',
            name='preview',
            field=models.CharField(blank=True, default='images/None/no_img_series.jpg', max_length=128, null=True, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u043e\u0442\u043e'),
        ),
    ]
