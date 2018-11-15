# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0012_labelledata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labelledata',
            name='Date',
            field=models.DateField(db_index=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='labelledata',
            name='Field',
            field=models.CharField(default=' ', max_length=64, db_index=True, blank=True),
        ),
    ]
