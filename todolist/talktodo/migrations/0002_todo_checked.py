# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-11 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talktodo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='checked',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]