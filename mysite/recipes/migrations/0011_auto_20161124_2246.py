# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 22:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_auto_20161124_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='createted',
            new_name='created',
        ),
    ]