# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0007_auto_20180403_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='leafsamples',
            name='age',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='leafsamples',
            name='irrigation',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
