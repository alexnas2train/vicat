# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-06 03:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0056_remove_series_im_sourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='series',
        ),
        migrations.RemoveField(
            model_name='status',
            name='user',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
