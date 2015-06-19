# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server_note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='hex_stat',
            field=models.CharField(max_length=32),
        ),
    ]
