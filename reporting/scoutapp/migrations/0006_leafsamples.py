# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0005_auto_20171027_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='leafSamples',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('field_name', models.CharField(max_length=64, null=True, blank=True)),
                ('nitrogen', models.CharField(max_length=64, null=True, blank=True)),
                ('phosphorus', models.CharField(max_length=64, null=True, blank=True)),
                ('potassium', models.CharField(max_length=64, null=True, blank=True)),
                ('magnesium', models.CharField(max_length=64, null=True, blank=True)),
                ('calcium', models.CharField(max_length=64, null=True, blank=True)),
                ('sulfur', models.CharField(max_length=64, null=True, blank=True)),
                ('boron', models.CharField(max_length=64, null=True, blank=True)),
                ('zinc', models.CharField(max_length=64, null=True, blank=True)),
                ('manganese', models.CharField(max_length=64, null=True, blank=True)),
                ('iron', models.CharField(max_length=64, null=True, blank=True)),
                ('copper', models.CharField(max_length=64, null=True, blank=True)),
                ('chloride', models.CharField(max_length=64, null=True, blank=True)),
            ],
        ),
    ]
