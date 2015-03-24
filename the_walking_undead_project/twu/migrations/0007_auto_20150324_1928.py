# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twu', '0006_auto_20150324_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='timestamp',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
