# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0015_leafsamplefields_column_header'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leafsamplefields',
            name='column_header',
        ),
        migrations.AddField(
            model_name='leafsufficiency',
            name='column_header',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
