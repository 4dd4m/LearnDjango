# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 05:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2016, 12, 17, 5, 7, 39, 83498, tzinfo=utc)),
            preserve_default=False,
        ),
    ]