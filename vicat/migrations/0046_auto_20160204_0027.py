# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicat', '0045_review_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='preview',
            field=models.FileField(blank=True, verbose_name='фото', default='dummy_series.jpg', upload_to=''),
        ),
    ]
