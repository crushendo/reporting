# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0005_leafsufficiency_column_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorLocations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_address', models.CharField(max_length=64, null=True, blank=True)),
                ('field_name', models.CharField(max_length=64, null=True, blank=True)),
                ('variety', models.CharField(max_length=64, null=True, blank=True)),
                ('location', models.CharField(max_length=64, null=True, blank=True)),
                ('gps', models.CharField(max_length=64, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SoilMoistureData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_address', models.CharField(max_length=64, null=True, blank=True)),
                ('field_name', models.CharField(max_length=64, null=True, blank=True)),
                ('time', models.CharField(max_length=64, null=True, blank=True)),
                ('soil_moisture', models.CharField(max_length=64, null=True, blank=True)),
            ],
        ),
    ]
