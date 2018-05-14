# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0002_labelledata_other'),
    ]

    operations = [
        migrations.CreateModel(
            name='sprayTrials',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64, null=True, blank=True)),
                ('field', models.CharField(max_length=64, null=True, blank=True)),
                ('spray_date', models.CharField(max_length=64, null=True, blank=True)),
                ('chemical', models.CharField(max_length=64, null=True, blank=True)),
                ('sprayer', models.CharField(max_length=64, null=True, blank=True)),
                ('position', models.CharField(max_length=64, null=True, blank=True)),
                ('notes', models.TextField(default=' ', null=True, blank=True)),
                ('num_mean_in', models.CharField(max_length=64, null=True, blank=True)),
                ('num_median_in', models.CharField(max_length=64, null=True, blank=True)),
                ('num_stdev_in', models.CharField(max_length=64, null=True, blank=True)),
                ('vol_mean_in', models.CharField(max_length=64, null=True, blank=True)),
                ('vol_median_in', models.CharField(max_length=64, null=True, blank=True)),
                ('coverage_percent', models.CharField(max_length=64, null=True, blank=True)),
                ('spray_paper', models.ImageField(null=True, upload_to='static/sprayImages', blank=True)),
            ],
        ),
    ]
