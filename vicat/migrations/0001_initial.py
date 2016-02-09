# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 13:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.CharField(blank=True, max_length=512, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('preview', models.CharField(blank=True, help_text='\u043a\u0430\u0434\u0440 \u0438\u0437 \u044d\u043f\u0438\u0437\u043e\u0434\u0430', max_length=128, verbose_name='\u0444\u043e\u0442\u043e')),
                ('length', models.IntegerField(default=0, verbose_name='\u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c')),
                ('season_num', models.IntegerField(default=0, verbose_name='\u043d\u043e\u043c\u0435\u0440 \u0441\u0435\u0437\u043e\u043d\u0430')),
                ('episode_num', models.IntegerField(default=0, verbose_name='\u043d\u043e\u043c\u0435\u0440 \u044d\u043f\u0438\u0437\u043e\u0434\u0430')),
                ('watch_count', models.IntegerField(default=0, verbose_name='\u043a\u043e\u043b-\u0432\u043e \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u043e\u0432')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u0434\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u042d\u043f\u0438\u0437\u043e\u0434',
                'verbose_name_plural': '\u042d\u043f\u0438\u0437\u043e\u0434\u044b',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.CharField(blank=True, max_length=512, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('preview', models.CharField(blank=True, help_text='\u043a\u0430\u0434\u0440 \u0438\u0437 \u0444\u0438\u043b\u044c\u043c\u0430', max_length=128, verbose_name='\u0444\u043e\u0442\u043e')),
                ('length', models.IntegerField(default=0, verbose_name='\u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c')),
                ('country', models.CharField(blank=True, max_length=128, verbose_name='\u0441\u0442\u0440\u0430\u043d\u0430')),
                ('studio', models.CharField(blank=True, max_length=128, verbose_name='\u0441\u0442\u0443\u0434\u0438\u044f')),
                ('language', models.CharField(blank=True, max_length=128, verbose_name='\u044f\u0437\u044b\u043a')),
                ('dub_lang', models.CharField(blank=True, max_length=128, verbose_name='\u044f\u0437\u044b\u043a \u0434\u0443\u0431\u043b\u044f\u0436\u0430')),
                ('subt_lan', models.CharField(blank=True, max_length=128, verbose_name='\u044f\u0437\u044b\u043a \u0441\u0443\u0431\u0442\u0438\u0442\u0440\u043e\u0432')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u0434\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0421\u0435\u0440\u0438\u0430\u043b',
                'verbose_name_plural': '\u0421\u0435\u0440\u0438\u0430\u043b\u044b',
            },
        ),
        migrations.AddField(
            model_name='episode',
            name='series_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vicat.Series', verbose_name='\u0441\u0435\u0440\u0438\u0430\u043b'),
        ),
    ]