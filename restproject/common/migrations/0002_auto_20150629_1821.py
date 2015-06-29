# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backscratcher',
            name='name',
            field=models.CharField(unique=True, max_length=80, verbose_name='name'),
        ),
    ]
