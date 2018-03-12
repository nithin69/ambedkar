# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
                ('phone', models.CharField(max_length=255, null=True, blank=True)),
                ('move', models.CharField(max_length=255, null=True, blank=True)),
                ('from_zip', models.CharField(max_length=255, null=True, blank=True)),
                ('to_zip', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
    ]
