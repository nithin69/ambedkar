# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0020_auto_20170802_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'media', null=True, verbose_name=b'Cover Image', blank=True)),
                ('filefield', models.FileField(upload_to=b'media', null=True, verbose_name=b'File', blank=True)),
                ('link', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='library',
            name='cover',
            field=models.ImageField(upload_to=b'media', null=True, verbose_name=b'Cover Image', blank=True),
        ),
    ]
