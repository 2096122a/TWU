# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twu', '0002_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='player',
        ),
        migrations.DeleteModel(
            name='Score',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
