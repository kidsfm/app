# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
