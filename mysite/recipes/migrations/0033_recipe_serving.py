# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0032_auto_20161204_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='serving',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]