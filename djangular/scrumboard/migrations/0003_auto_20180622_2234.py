# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-06-22 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0002_auto_20180622_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cards', to='scrumboard.List'),
        ),
    ]
