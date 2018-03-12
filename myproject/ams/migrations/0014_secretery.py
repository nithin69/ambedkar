# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0013_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secretery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255, null=True, blank=True)),
                ('membership', models.CharField(max_length=255, null=True, verbose_name=b'Membership No.', blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('phone', models.CharField(max_length=255, null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'media', null=True, verbose_name=b'Person Image', blank=True)),
                ('application', models.ImageField(null=True, upload_to=b'media', blank=True)),
            ],
        ),
    ]
