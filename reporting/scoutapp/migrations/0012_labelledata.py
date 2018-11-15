# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0011_delete_labelledata'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelleData',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('Field', models.CharField(default=' ', max_length=64, blank=True)),
                ('Age', models.CharField(default=' ', max_length=64, blank=True)),
                ('Date', models.DateField(null=True, blank=True)),
                ('Stop', models.CharField(default=' ', max_length=64, blank=True)),
                ('Adult', models.IntegerField(null=True, blank=True)),
                ('Eggs', models.IntegerField(null=True, blank=True)),
                ('Tapped', models.CharField(default=' ', max_length=64, null=True, blank=True)),
                ('Flush', models.CharField(default=' ', max_length=64, null=True, blank=True)),
                ('LM', models.CharField(default=' ', max_length=64, blank=True)),
                ('OD', models.CharField(default=' ', max_length=64, blank=True)),
                ('SM', models.CharField(default=' ', max_length=64, blank=True)),
                ('Leafminer', models.CharField(default=' ', max_length=64, blank=True)),
                ('ODLarva', models.CharField(default=' ', max_length=64, blank=True)),
                ('ODEggs', models.CharField(default=' ', max_length=64, blank=True)),
                ('SpiderMites', models.CharField(default=' ', max_length=64, blank=True)),
                ('Other', models.CharField(default=' ', max_length=64, blank=True)),
            ],
        ),
    ]
