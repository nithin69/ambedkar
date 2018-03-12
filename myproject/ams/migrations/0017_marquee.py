# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0016_auto_20170802_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marquee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
    ]
