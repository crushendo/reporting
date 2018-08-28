# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('area', models.TextField(default=' ', blank=True)),
                ('fieldName', models.TextField(default=' ', blank=True)),
                ('age', models.TextField(default=' ', blank=True)),
                ('variety', models.TextField(default=' ', blank=True)),
                ('chemical', models.TextField(default=' ', blank=True)),
                ('status', models.TextField(default=' ', blank=True)),
                ('slug', models.SlugField(unique=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LabelleData',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('Field', models.TextField(default=' ', blank=True)),
                ('Age', models.TextField(default=' ', blank=True)),
                ('Date', models.DateField(null=True)),
                ('Stop', models.TextField(default=' ', blank=True)),
                ('Adult', models.TextField(default=' ', blank=True)),
                ('Eggs', models.TextField(default=' ', blank=True)),
                ('Tapped', models.TextField(default=' ', blank=True)),
                ('Flush', models.TextField(default=' ', blank=True)),
                ('LM', models.TextField(default=' ', blank=True)),
                ('OD', models.TextField(default=' ', blank=True)),
                ('SM', models.TextField(default=' ', blank=True)),
                ('Leafminer', models.TextField(default=' ', blank=True)),
                ('ODLarva', models.TextField(default=' ', blank=True)),
                ('ODEggs', models.TextField(default=' ', blank=True)),
                ('SpiderMites', models.TextField(default=' ', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='labelleFieldOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fieldName', models.TextField(default=' ', blank=True)),
                ('age', models.TextField(default=' ', blank=True)),
                ('order', models.TextField(default=' ', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='scoutingAreas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.TextField(default=' ', blank=True)),
                ('scoutedItem', models.TextField(default=' ', blank=True)),
            ],
        ),
    ]
