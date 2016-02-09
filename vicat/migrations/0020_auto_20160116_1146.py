# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0019_episode_season_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='ep_in_season_qty',
            field=models.IntegerField(default=0, verbose_name='\u043a\u043e\u043b-\u0432\u043e  \u044d\u043f\u0438\u0437\u043e\u0434\u043e\u0432 \u0432 \u0441\u0435\u0437\u043e\u043d\u0435'),
        ),
        migrations.AddField(
            model_name='episode',
            name='ep_in_series_qty',
            field=models.IntegerField(default=0, verbose_name='\u043a\u043e\u043b-\u0432\u043e  \u044d\u043f\u0438\u0437\u043e\u0434\u043e\u0432 \u0432 \u0441\u0435\u0440\u0438\u0430\u043b\u0435'),
        ),
    ]