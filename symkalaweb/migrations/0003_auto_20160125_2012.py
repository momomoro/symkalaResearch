# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-26 01:12


import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('symkalaweb', '0002_auto_20160122_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 26, 1, 12, 17, 944000, tzinfo=utc)),
        ),
    ]
