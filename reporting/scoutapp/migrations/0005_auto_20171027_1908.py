# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0004_spraytrials_spray_paper'),
    ]

    operations = [
        migrations.AddField(
            model_name='spraytrials',
            name='spray_date',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='spraytrials',
            name='spray_paper',
            field=models.ImageField(null=True, upload_to='static/sprayImages', blank=True),
        ),
    ]
