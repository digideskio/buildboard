# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-22 20:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildboard_app', '0007_auto_20160922_2002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name', 'division']},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ('-year', 'semester_type')},
        ),
    ]
