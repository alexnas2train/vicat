# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0040_auto_20160131_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='preview',
            field=models.CharField(blank=True, default='dummy_episode.jpg', max_length=128, verbose_name='\u0444\u043e\u0442\u043e'),
        ),
    ]
