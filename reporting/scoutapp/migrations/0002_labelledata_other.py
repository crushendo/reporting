# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labelledata',
            name='Other',
            field=models.TextField(default=' ', blank=True),
        ),
    ]
