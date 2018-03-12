# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('graph', models.ImageField(null=True, upload_to=b'media', blank=True)),
                ('stat1_title', models.CharField(max_length=255, null=True, blank=True)),
                ('stat1_value', models.CharField(max_length=255, null=True, blank=True)),
                ('stat2_title', models.CharField(max_length=255, null=True, blank=True)),
                ('stat2_value', models.CharField(max_length=255, null=True, blank=True)),
                ('stat3_title', models.CharField(max_length=255, null=True, blank=True)),
                ('stat3_value', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
