# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0010_leafsamples_tree'),
    ]

    operations = [
        migrations.CreateModel(
            name='leafSampleFields',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_name', models.CharField(max_length=64, null=True, blank=True)),
                ('age', models.CharField(max_length=64, null=True, blank=True)),
                ('irrigation', models.CharField(max_length=64, null=True, blank=True)),
                ('tree', models.CharField(max_length=64, null=True, blank=True)),
            ],
        ),
    ]
