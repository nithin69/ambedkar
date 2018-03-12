# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0015_carosuel_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='secretery',
            options={'verbose_name_plural': 'Body Members'},
        ),
    ]
