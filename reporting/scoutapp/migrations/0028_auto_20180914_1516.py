# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-14 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoutapp', '0027_labelledata'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='labelledata',
            index=models.Index(fields=['Date'], name='scoutapp_la_Date_4d5289_idx'),
        ),
    ]
