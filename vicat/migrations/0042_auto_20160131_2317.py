# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0041_auto_20160131_1420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': '\u041e\u0442\u0437\u044b\u0432', 'verbose_name_plural': '\u041e\u0442\u0437\u044b\u0432'},
        ),
        migrations.AlterField(
            model_name='series',
            name='country',
            field=models.CharField(choices=[('\u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e', '\u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e'), ('\u0420\u043e\u0441\u0441\u0438\u044f', '\u0420\u043e\u0441\u0441\u0438\u044f'), ('\u0421\u0428\u0410', '\u0421\u0428\u0410'), ('\u042f\u043f\u043e\u043d\u0438\u044f', '\u042f\u043f\u043e\u043d\u0438\u044f'), ('\u0424\u0440\u0430\u043d\u0446\u0438\u044f', '\u0424\u0440\u0430\u043d\u0446\u0438\u044f'), ('\u0418\u0441\u043f\u0430\u043d\u0438\u044f', '\u0418\u0441\u043f\u0430\u043d\u0438\u044f'), ('\u041a\u043e\u043b\u0443\u043c\u0431\u0438\u044f', '\u041a\u043e\u043b\u0443\u043c\u0431\u0438\u044f'), ('\u0410\u0440\u0433\u0435\u043d\u0442\u0438\u043d\u0430', '\u0410\u0440\u0433\u0435\u043d\u0442\u0438\u043d\u0430'), ('\u041c\u0435\u043a\u0441\u0438\u043a\u0430', '\u041c\u0435\u043a\u0441\u0438\u043a\u0430')], default='', max_length=50, verbose_name='\u0441\u0442\u0440\u0430\u043d\u0430'),
        ),
        migrations.AlterField(
            model_name='series',
            name='genre',
            field=models.CharField(choices=[('\u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e', '\u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e'), ('\u043a\u043e\u043c\u0435\u0434\u0438\u044f', '\u043a\u043e\u043c\u0435\u0434\u0438\u044f'), ('\u0442\u0440\u0430\u0433\u0435\u0434\u0438\u044f', '\u0442\u0440\u0430\u0433\u0435\u0434\u0438\u044f'), ('\u043c\u0438\u0441\u0442\u0438\u043a\u0430', '\u043c\u0438\u0441\u0442\u0438\u043a\u0430'), ('\u0441\u0435\u043c\u0435\u0439\u043d\u044b\u0439', '\u0441\u0435\u043c\u0435\u0439\u043d\u044b\u0439')], default='', max_length=50, verbose_name='\u0436\u0430\u043d\u0440'),
        ),
        migrations.AlterField(
            model_name='series',
            name='language',
            field=models.CharField(choices=[('\u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e', '\u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e'), ('RU', '\u0440\u0443\u0441\u0441\u043a\u0438\u0439'), ('EN', '\u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439'), ('ES', '\u0438\u0441\u043f\u0430\u043d\u0441\u043a\u0438\u0439'), ('FR', '\u0444\u0440\u0430\u043d\u0446\u0443\u0437\u0441\u043a\u0438\u0439'), ('JP', '\u044f\u043f\u043e\u043d\u0441\u043a\u0438\u0439')], default='', max_length=50, verbose_name='\u044f\u0437\u044b\u043a'),
        ),
        migrations.AlterField(
            model_name='series',
            name='show_type',
            field=models.CharField(choices=[('\u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e', '\u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e'), ('\u0444\u0438\u043b\u044c\u043c', '\u0444\u0438\u043b\u044c\u043c'), ('\u0441\u0435\u0440\u0438\u0430\u043b', '\u0441\u0435\u0440\u0438\u0430\u043b'), ('\u0430\u043d\u0438\u043c\u0435', '\u0430\u043d\u0438\u043c\u0435'), ('\u0430\u043d\u0438\u043c\u0435-\u0441\u0435\u0440\u0438\u0430\u043b', '\u0430\u043d\u0438\u043c\u0435-\u0441\u0435\u0440\u0438\u0430\u043b')], default='', max_length=50, verbose_name='\u0442\u0438\u043f'),
        ),
        migrations.AlterField(
            model_name='series',
            name='subt_lan',
            field=models.CharField(choices=[('\u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e', '\u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e'), ('\u043d\u0435\u0442', '\u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u044e\u0442'), ('RU', '\u0440\u0443\u0441\u0441\u043a\u0438\u0439'), ('EN', '\u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439'), ('ES', '\u0438\u0441\u043f\u0430\u043d\u0441\u043a\u0438\u0439'), ('FR', '\u0444\u0440\u0430\u043d\u0446\u0443\u0437\u0441\u043a\u0438\u0439'), ('JP', '\u044f\u043f\u043e\u043d\u0441\u043a\u0438\u0439')], default='', max_length=50, verbose_name='\u0441\u0443\u0431\u0442\u0438\u0442\u0440\u044b'),
        ),
    ]
