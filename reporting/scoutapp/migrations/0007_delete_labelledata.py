# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0006_sensorlocations_soilmoisturedata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LabelleData',
        ),
    ]
