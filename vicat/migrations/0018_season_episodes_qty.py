# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0017_auto_20160114_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='episodes_qty',
            field=models.IntegerField(default=0, verbose_name='\u043a\u043e\u043b-\u0432\u043e \u044d\u043f\u0438\u0437\u043e\u0434\u043e\u0432'),
        ),
    ]
