# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0006_leafsamples'),
    ]

    operations = [
        migrations.AddField(
            model_name='leafsamples',
            name='date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='leafsamples',
            name='guess',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
