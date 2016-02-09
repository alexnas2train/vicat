# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 12:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vicat', '0034_auto_20160130_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', models.CharField(max_length=1024, verbose_name='\u0442\u0435\u043a\u0441\u0442')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u0434\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u0434\u0430\u0442\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vicat.Series')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a',
                'verbose_name_plural': '\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438',
            },
        ),
        migrations.RemoveField(
            model_name='rewiew',
            name='series',
        ),
        migrations.RemoveField(
            model_name='rewiew',
            name='user',
        ),
        migrations.DeleteModel(
            name='Rewiew',
        ),
    ]