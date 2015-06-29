# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackScratcher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('size', models.CharField(max_length=100, verbose_name='size', choices=[(b'XS', b'XS'), (b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL')])),
                ('price', models.DecimalField(verbose_name='price', max_digits=5, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Back Scratcher',
                'verbose_name_plural': 'Back Scratchers',
            },
        ),
    ]
