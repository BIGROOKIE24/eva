# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-31 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0025_auto_20180831_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='filename',
            field=models.CharField(blank=True, help_text='Name of the video file.', max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(help_text='Name of the sequence.', max_length=255, unique=True),
        ),
    ]
