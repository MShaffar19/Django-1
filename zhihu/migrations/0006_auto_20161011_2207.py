# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-11 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhihu', '0005_auto_20161011_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpersonal',
            name='sex',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
