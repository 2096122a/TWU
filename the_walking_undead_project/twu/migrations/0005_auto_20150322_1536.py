# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('twu', '0004_auto_20150320_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='score',
            name='player',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AlterField(
            model_name='score',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
