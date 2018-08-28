# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0012_leafsamplefields_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='RustMites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_name', models.CharField(max_length=64, null=True, blank=True)),
                ('date', models.DateField(null=True)),
                ('lens_fields', models.CharField(max_length=64, null=True, blank=True)),
                ('low', models.CharField(max_length=64, null=True, blank=True)),
                ('high', models.CharField(max_length=64, null=True, blank=True)),
            ],
        ),
    ]
