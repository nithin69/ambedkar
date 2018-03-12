# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0007_auto_20170727_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='link',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='scolarship',
            name='link',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
