# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-22 17:17


import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('symkalaweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 22, 17, 17, 59, 87000, tzinfo=utc)),
        ),
    ]
