# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0049_auto_20160204_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='preview',
            field=models.CharField(blank=True, default='images/none/no_img_series.jpg', max_length=128, verbose_name='\u0444\u043e\u0442\u043e'),
        ),
    ]
