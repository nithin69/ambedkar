# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carosuel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'media/carosuel', blank=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('album', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('categorylist', models.CharField(max_length=20, choices=[(b'Artists', b'Artists'), (b'Albums', b'Albums'), (b'New Release', b'New Release'), (b'Featured', b'Featured'), (b'Radio', b'Radio'), (b'Treanding', b'Treanding'), (b'Other', b'Other')])),
                ('type_category', models.CharField(max_length=20, choices=[(b'Ringtones', b'Ringtones'), (b'Videos', b'Videos'), (b'Albums', b'Albums')])),
                ('artist', models.CharField(max_length=200, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('content', models.FileField(upload_to=b'media', null=True, verbose_name=b'File', blank=True)),
                ('image', models.ImageField(upload_to=b'media', null=True, verbose_name=b'Cover Pic', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
            ],
        ),
    ]
