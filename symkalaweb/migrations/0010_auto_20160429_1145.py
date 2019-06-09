# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-29 15:45


import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('symkalaweb', '0009_auto_20160427_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 29, 15, 45, 26, 557000, tzinfo=utc)),
        ),
    ]
