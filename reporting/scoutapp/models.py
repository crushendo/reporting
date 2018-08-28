from __future__ import unicode_literals
from django import forms
from django.db import models
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User

class Field(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.TextField(default = ' ', blank=True)
    fieldName = models.TextField(default = ' ', blank=True)
    age = models.TextField(default = ' ', blank=True)
    variety = models.TextField(default = ' ', blank=True)
    chemical = models.TextField(default = ' ', blank=True)
    status = models.TextField(default = ' ', blank=True)
    slug = models.SlugField(unique = True, max_length = 30)
    
class LabelleData(models.Model):
    id = models.AutoField(primary_key=True)
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
    spray_paper = models.ImageField(null=True, blank=True, upload_to="static/sprayImages")
    
class leafSamples(models.Model):
    id = models.AutoField(primary_key=True)
    field_name = models.CharField(max_length=64, blank=True, null=True)
    nitrogen = models.CharField(max_length=64, blank=True, null=True)
    phosphorus = models.CharField(max_length=64, blank=True, null=True)
    potassium = models.CharField(max_length=64, blank=True, null=True)
    magnesium = models.CharField(max_length=64, blank=True, null=True)
    calcium = models.CharField(max_length=64, blank=True, null=True)
    sulfur = models.CharField(max_length=64, blank=True, null=True)
    boron = models.CharField(max_length=64, blank=True, null=True)
    zinc = models.CharField(max_length=64, blank=True, null=True)
    manganese = models.CharField(max_length=64, blank=True, null=True)
    iron = models.CharField(max_length=64, blank=True, null=True)
    copper = models.CharField(max_length=64, blank=True, null=True)
    chloride = models.CharField(max_length=64, blank=True, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    guess = models.CharField(max_length=64, blank=True, null=True)
    age = models.CharField(max_length=64, blank=True, null=True)
    irrigation = models.CharField(max_length=64, blank=True, null=True)
    tree = models.CharField(max_length=64, blank=True, null=True)

class leafSufficiency(models.Model):
    element = models.CharField(max_length=64, blank=True, null=True)
    column_header = models.CharField(max_length=64, blank=True, null=True)
    metric = models.CharField(max_length=64, blank=True, null=True)
    deficient = models.CharField(max_length=64, blank=True, null=True)
    low = models.CharField(max_length=64, blank=True, null=True)
    optimum = models.CharField(max_length=64, blank=True, null=True)
    high = models.CharField(max_length=64, blank=True, null=True)
    excess = models.CharField(max_length=64, blank=True, null=True)
    
class leafSampleFields(models.Model):
    field_name = models.CharField(max_length=64, blank=True, null=True)
    location = models.CharField(max_length=64, blank=True, null=True)
    age = models.CharField(max_length=64, blank=True, null=True)
    irrigation = models.CharField(max_length=64, blank=True, null=True)
    tree = models.CharField(max_length=64, blank=True, null=True)
    
class RustMites(models.Model):
    field_name = models.CharField(max_length=64, blank=True, null=True)
    date = models.DateField(null=True)
    lens_fields = models.CharField(max_length=64, blank=True, null=True)
    low = models.CharField(max_length=64, blank=True, null=True)
    high = models.CharField(max_length=64, blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)
    
class RustMiteFields(models.Model):
    field_name = models.CharField(max_length=64, blank=True, null=True)
    variety = models.CharField(max_length=64, blank=True, null=True)
    location = models.CharField(max_length=64, blank=True, null=True)
    acres = models.CharField(max_length=64, blank=True, null=True)

class SensorLocations(models.Model):
    source_address = models.CharField(max_length=64, blank=True, null=True)
    field_name = models.CharField(max_length=64, blank=True, null=True)
    variety = models.CharField(max_length=64, blank=True, null=True)
    location = models.CharField(max_length=64, blank=True, null=True)
    gps = models.CharField(max_length=64, blank=True, null=True)
    
class SoilMoistureData(models.Model):
    source_address = models.CharField(max_length=64, blank=True, null=True)
    field_name = models.CharField(max_length=64, blank=True, null=True)
    time = models.CharField(max_length=64, blank=True, null=True)
    soil_moisture = models.CharField(max_length=64, blank=True, null=True)
    
    
    
    