# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_gamer_no_of_trucks'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamer',
            name='no_Of_Trucks',
            field=models.PositiveIntegerField(default=25),
        ),
    ]
