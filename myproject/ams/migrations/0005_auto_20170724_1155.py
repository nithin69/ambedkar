# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0004_auto_20170722_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='application',
            field=models.ImageField(null=True, upload_to=b'media', blank=True),
        ),
        migrations.AddField(
            model_name='members',
            name='image',
            field=models.ImageField(upload_to=b'media', null=True, verbose_name=b'Person Image', blank=True),
        ),
        migrations.AddField(
            model_name='members',
            name='phone',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='news',
            name='application',
            field=models.ImageField(null=True, upload_to=b'media', blank=True),
        ),
        migrations.AddField(
            model_name='news',
            name='designation',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='news',
            name='phone',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
