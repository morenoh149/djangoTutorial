# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-01 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='opened',
            field=models.BooleanField(default=False),
        ),
    ]