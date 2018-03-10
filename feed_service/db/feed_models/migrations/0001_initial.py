# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_string', models.CharField(max_length=1024)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2018, 3, 9, 23, 43, 28, 817966))),
            ],
        ),
        migrations.CreateModel(
            name='Downvote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=256)),
                ('answer', models.ForeignKey(to='feed_models.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_string', models.CharField(max_length=1024)),
                ('user_id', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2018, 3, 9, 23, 43, 28, 817479))),
            ],
        ),
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=256)),
                ('answer', models.ForeignKey(to='feed_models.Answer')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='feed_models.Question'),
        ),
    ]
