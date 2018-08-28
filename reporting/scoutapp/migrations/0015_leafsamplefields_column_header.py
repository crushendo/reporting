# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0014_auto_20180502_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='leafsamplefields',
            name='column_header',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
