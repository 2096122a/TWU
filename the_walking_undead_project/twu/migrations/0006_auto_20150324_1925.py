# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twu', '0005_auto_20150322_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='timestamp',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
