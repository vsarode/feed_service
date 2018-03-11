# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feed_models', '0002_auto_20180310_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 10, 3, 5, 27, 253035)),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 10, 3, 5, 27, 252422)),
        ),
    ]
