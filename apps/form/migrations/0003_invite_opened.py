# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-03 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20171103_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='opened',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
