# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freshmaza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carosuel',
            name='image',
            field=models.ImageField(null=True, upload_to=b'carosuel', blank=True),
        ),
    ]
