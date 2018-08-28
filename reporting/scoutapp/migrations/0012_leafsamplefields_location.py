# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0011_leafsamplefields'),
    ]

    operations = [
        migrations.AddField(
            model_name='leafsamplefields',
            name='location',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
