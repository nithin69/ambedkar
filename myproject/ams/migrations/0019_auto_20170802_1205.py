# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0018_auto_20170802_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='filefield',
        ),
        migrations.AddField(
            model_name='resource',
            name='audio',
            field=models.ImageField(upload_to=b'media', null=True, verbose_name=b'Cover Image', blank=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='video',
            field=models.ImageField(upload_to=b'media', null=True, verbose_name=b'Cover Image', blank=True),
        ),
    ]
