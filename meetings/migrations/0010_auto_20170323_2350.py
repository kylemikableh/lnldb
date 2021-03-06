# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-24 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0009_auto_20161016_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccnoticesend',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='meetingccnoticeevents', to='events.Event'),
        ),
        migrations.AlterField(
            model_name='ccnoticesend',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='meetingannounce',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='meetingannouncements', to='events.Event'),
        ),
        migrations.AlterField(
            model_name='meetingannounce',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False),
        ),
    ]
