# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feed_models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='user_id',
            field=models.CharField(default=None, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 10, 0, 38, 28, 706250)),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 10, 0, 38, 28, 705699)),
        ),
    ]
