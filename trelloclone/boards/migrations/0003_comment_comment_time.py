# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 00:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
