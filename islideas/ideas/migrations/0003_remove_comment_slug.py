# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 18:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_auto_20160315_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
    ]
