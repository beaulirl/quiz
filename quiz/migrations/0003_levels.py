# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-01 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20180401_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(max_length=200)),
            ],
        ),
    ]
