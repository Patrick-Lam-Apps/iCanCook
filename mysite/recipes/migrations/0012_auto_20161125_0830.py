# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_auto_20161125_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantitytype',
            name='name',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
