# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-18 18:59


import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('symkalaweb', '0003_auto_20160118_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 18, 18, 59, 57, 741000, tzinfo=utc)),
        ),
    ]
