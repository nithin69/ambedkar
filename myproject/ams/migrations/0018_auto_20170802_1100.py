# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0017_marquee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marquee',
            name='content',
            field=models.TextField(null=True, blank=True),
        ),
    ]
