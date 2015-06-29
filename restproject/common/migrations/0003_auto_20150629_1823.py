# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20150629_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backscratcher',
            name='name',
            field=models.CharField(max_length=80, verbose_name='name'),
        ),
    ]
