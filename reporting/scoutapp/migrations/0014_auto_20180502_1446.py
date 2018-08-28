# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0013_rustmites'),
    ]

    operations = [
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
        migrations.AddField(
            model_name='rustmites',
            name='notes',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
