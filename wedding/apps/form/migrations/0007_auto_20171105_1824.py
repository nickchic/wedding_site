# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-05 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_auto_20171103_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='color_war',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guest',
            name='rehearsal',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guest',
            name='shirt_size',
            field=models.CharField(max_length=5, null=True),
        ),
    ]