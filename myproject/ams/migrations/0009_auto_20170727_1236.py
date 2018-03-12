# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0008_auto_20170727_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='phone',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='scolarship',
            name='phone',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
