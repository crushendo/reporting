from __future__ import unicode_literals
from django import forms
from django.db import models
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User

class Field(models.Model):
    id = models.TextField(default = ' ', primary_key=True)
    area = models.TextField(default = ' ', blank=True)
    fieldName = models.TextField(default = ' ', blank=True)
    age = models.TextField(default = ' ', blank=True)
    variety = models.TextField(default = ' ', blank=True)
    chemical = models.TextField(default = ' ', blank=True)
    status = models.TextField(default = ' ', blank=True)
    slug = models.TextField(unique = True)
    
class LabelleData(models.Model):
    id = models.TextField(default = ' ', primary_key=True)
    slug = models.SlugField(unique = True)
    Field = models.TextField(default = ' ', blank=True)
    Age = models.TextField(default = ' ', blank=True)
    Date = models.DateField(null=True)
    Stop = models.TextField(default = ' ', blank=True)
    Adult = models.TextField(default = ' ', blank=True)
    Eggs = models.TextField(default = ' ', blank=True)
    Tapped = models.TextField(default = ' ', blank=True)
    Flush = models.TextField(default = ' ', blank=True)
    LM = models.TextField(default = ' ', blank=True)
    OD = models.TextField(default = ' ', blank=True)
    SM = models.TextField(default = ' ', blank=True)
    Leafminer = models.TextField(default = ' ', blank=True)
    ODLarva = models.TextField(default = ' ', blank=True)
    ODEggs = models.TextField(default = ' ', blank=True)
    SpiderMites = models.TextField(default = ' ', blank=True)
    Other = models.TextField(default = ' ', blank=True)
    
class labelleFieldOrder(models.Model):
    fieldName = models.TextField(default = ' ', blank=True)
    age = models.TextField(default = ' ', blank=True)
    order = models.TextField(default = ' ', blank=True)

class scoutingAreas(models.Model):
    location = models.TextField(default = ' ', blank=True)
    scoutedItem = models.TextField(default = ' ', blank=True)

class sprayTrials(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    field = models.CharField(max_length=64, blank=True, null=True)
    spray_date = models.CharField(max_length=64, blank=True, null=True)
    chemical = models.CharField(max_length=64, blank=True, null=True)
    sprayer = models.CharField(max_length=64, blank=True, null=True)
    position = models.CharField(max_length=64, blank=True, null=True)
    notes = models.TextField(default = ' ', blank=True, null=True)
    num_mean_in = models.CharField(max_length=64, blank=True, null=True)
    num_median_in = models.CharField(max_length=64, blank=True, null=True)
    num_stdev_in = models.CharField(max_length=64, blank=True, null=True)
    vol_mean_in = models.CharField(max_length=64, blank=True, null=True)
    vol_median_in = models.CharField(max_length=64, blank=True, null=True)
    coverage_percent = models.CharField(max_length=64, blank=True, null=True)
    spray_paper = models.ImageField(null=True, blank=True, upload_to="sprayImages")
