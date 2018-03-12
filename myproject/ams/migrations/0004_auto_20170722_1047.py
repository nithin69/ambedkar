# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0003_youtube'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'media', blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='library',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book', models.CharField(max_length=255, null=True, blank=True)),
                ('author', models.CharField(max_length=255, null=True, blank=True)),
                ('status', models.BooleanField(default=True)),
                ('form_date', models.DateField(null=True, blank=True)),
                ('to_date', models.DateField(null=True, blank=True)),
                ('issued', models.CharField(max_length=255, null=True, blank=True)),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='members',
            name='designation',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
