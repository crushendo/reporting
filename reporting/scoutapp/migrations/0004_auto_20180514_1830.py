# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0003_spraytrials'),
    ]

    operations = [
        migrations.CreateModel(
            name='leafSampleFields',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_name', models.CharField(max_length=64, null=True, blank=True)),
                ('location', models.CharField(max_length=64, null=True, blank=True)),
                ('age', models.CharField(max_length=64, null=True, blank=True)),
                ('irrigation', models.CharField(max_length=64, null=True, blank=True)),
                ('tree', models.CharField(max_length=64, null=True, blank=True)),
            ],
        ),
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
                ('date', models.DateField(null=True, blank=True)),
                ('guess', models.CharField(max_length=64, null=True, blank=True)),
                ('age', models.CharField(max_length=64, null=True, blank=True)),
                ('irrigation', models.CharField(max_length=64, null=True, blank=True)),
                ('tree', models.CharField(max_length=64, null=True, blank=True)),
            ],
        ),
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
        migrations.CreateModel(
            name='RustMiteFields',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_name', models.CharField(max_length=64, null=True, blank=True)),
                ('variety', models.CharField(max_length=64, null=True, blank=True)),
                ('location', models.CharField(max_length=64, null=True, blank=True)),
                ('acres', models.CharField(max_length=64, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RustMites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_name', models.CharField(max_length=64, null=True, blank=True)),
                ('date', models.DateField(null=True)),
                ('lens_fields', models.CharField(max_length=64, null=True, blank=True)),
                ('low', models.CharField(max_length=64, null=True, blank=True)),
                ('high', models.CharField(max_length=64, null=True, blank=True)),
                ('notes', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='spraytrials',
            name='spray_paper',
            field=models.ImageField(null=True, upload_to='sprayImages', blank=True),
        ),
    ]
