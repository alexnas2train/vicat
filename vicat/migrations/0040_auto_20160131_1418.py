# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0039_remove_review_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='preview',
            field=models.CharField(blank=True, default='dummy_series.jpg', max_length=128, verbose_name='\u0444\u043e\u0442\u043e'),
        ),
    ]
