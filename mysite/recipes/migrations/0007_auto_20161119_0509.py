# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20161118_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='rid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]