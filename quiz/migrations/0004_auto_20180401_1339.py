# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-01 13:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_levels'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answers',
            new_name='Answer',
        ),
        migrations.RenameModel(
            old_name='Levels',
            new_name='Level',
        ),
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
        migrations.RenameModel(
            old_name='Tests',
            new_name='Test',
        ),
        migrations.RenameModel(
            old_name='TestQuestions',
            new_name='TestQuestion',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.RenameModel(
            old_name='UserAnswers',
            new_name='UserAnswer',
        ),
    ]