# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-03 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_guest_rsvp'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='camping',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
