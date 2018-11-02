# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0022_delete_labelledata'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelleData',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('Field', models.TextField(default=' ', max_length=64, blank=True)),
                ('Age', models.TextField(default=' ', max_length=64, blank=True)),
                ('Date', models.TextField(default=' ', max_length=64, blank=True)),
                ('Stop', models.TextField(default=' ', max_length=64, blank=True)),
                ('Adult', models.TextField(default=' ', max_length=64, blank=True)),
                ('Eggs', models.TextField(default=' ', max_length=64, blank=True)),
                ('Tapped', models.TextField(default=' ', max_length=64, blank=True)),
                ('Flush', models.TextField(default=' ', max_length=64, blank=True)),
                ('LM', models.TextField(default=' ', max_length=64, blank=True)),
                ('OD', models.TextField(default=' ', max_length=64, blank=True)),
                ('SM', models.TextField(default=' ', max_length=64, blank=True)),
                ('Leafminer', models.TextField(default=' ', max_length=64, blank=True)),
                ('ODLarva', models.TextField(default=' ', max_length=64, blank=True)),
                ('ODEggs', models.TextField(default=' ', max_length=64, blank=True)),
                ('SpiderMites', models.TextField(default=' ', max_length=64, blank=True)),
                ('Other', models.TextField(default=' ', max_length=64, blank=True)),
            ],
        ),
    ]
