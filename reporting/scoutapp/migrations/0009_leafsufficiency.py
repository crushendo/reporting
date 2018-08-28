# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0008_auto_20180405_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='leafSufficiency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('element', models.CharField(max_length=64, null=True, blank=True)),
                ('metric', models.CharField(max_length=64, null=True, blank=True)),
                ('deficient', models.CharField(max_length=64, null=True, blank=True)),
                ('low', models.CharField(max_length=64, null=True, blank=True)),
                ('optimum', models.CharField(max_length=64, null=True, blank=True)),
                ('high', models.CharField(max_length=64, null=True, blank=True)),
                ('excess', models.CharField(max_length=64, null=True, blank=True)),
            ],
        ),
    ]
