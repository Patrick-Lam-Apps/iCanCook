# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_auto_20161125_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
