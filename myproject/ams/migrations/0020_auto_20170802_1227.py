# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0019_auto_20170802_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='audio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('audio', models.ImageField(upload_to=b'media', null=True, verbose_name=b'Cover Image', blank=True)),
                ('filefield', models.FileField(upload_to=b'media', null=True, verbose_name=b'File', blank=True)),
                ('link', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'media', null=True, verbose_name=b'Cover Image', blank=True)),
                ('filefield', models.FileField(upload_to=b'media', null=True, verbose_name=b'File', blank=True)),
                ('link', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('video', models.ImageField(upload_to=b'media', null=True, verbose_name=b'Cover Image', blank=True)),
                ('filefield', models.FileField(upload_to=b'media', null=True, verbose_name=b'File', blank=True)),
                ('link', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
    ]
