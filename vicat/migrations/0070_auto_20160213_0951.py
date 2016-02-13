# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 04:21
from __future__ import unicode_literals

from django.db import migrations, models
import vicat.models


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0069_auto_20160213_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='image_episode',
            field=models.ImageField(blank=True, storage=vicat.models.OverwriteStorage(), upload_to=vicat.models.get_upload_path_epis, verbose_name='\u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u0444\u043e\u0442\u043e_\u044d\u043f'),
        ),
    ]