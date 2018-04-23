# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-15 18:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]