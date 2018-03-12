# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0014_secretery'),
    ]

    operations = [
        migrations.AddField(
            model_name='carosuel',
            name='title',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
