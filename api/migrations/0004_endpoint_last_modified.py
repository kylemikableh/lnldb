# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-10 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200628_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoint',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
