# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0003_spraytrials'),
    ]

    operations = [
        migrations.AddField(
            model_name='spraytrials',
            name='spray_paper',
            field=models.ImageField(null=True, upload_to='static/sprayImages'),
        ),
    ]
