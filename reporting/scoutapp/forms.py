from django.forms import ModelForm, ModelChoiceField, FileField
from django import forms
from scoutapp.models import Field
from scoutapp.models import LabelleData
from scoutapp.models import sprayTrials
from scoutapp.models import leafSamples
from scoutapp.models import leafSampleFields
from scoutapp.models import RustMites
from scoutapp.models import leafSufficiency

class fieldForm(ModelForm):
    class Meta: 
        model = Field 
        fields = ('area', 'fieldName', 'age', 'status', 'slug', 'chemical', 'variety')
        
class labelleMatureNE(ModelForm):
    class Meta:
        model = LabelleData
        fields = ('slug', 'Field', "Age", "Date", "Adult", "Eggs", "Tapped", "Flush", "LM", "OD", "SM")
        
class labelleMatureSE(ModelForm):
    class Meta:
        model = LabelleData
        fields = ('slug', 'Field', "Age", "Date", "Adult", "Eggs", "Tapped", "Flush", "LM", "OD", "SM")

class labelleMatureC(ModelForm):
    class Meta:
        model = LabelleData
        fields = ('slug', 'Field', "Age", "Date", "Adult", "Eggs", "Tapped", "Flush", "LM", "OD", "SM")
        
class labelleMatureNW(ModelForm):
    class Meta:
        model = LabelleData
        fields = ('slug', 'Field', "Age", "Date", "Adult", "Eggs", "Tapped", "Flush", "LM", "OD", "SM")
        
class labelleMatureSW(ModelForm):
    class Meta:
        model = LabelleData
        fields = ('slug', 'Field', "Age", "Date", "Adult", "Eggs", "Tapped", "Flush", "LM", "OD", "SM")

class sprayForm(ModelForm):
    class Meta:
        model = sprayTrials
        fields = ('name', 'field', 'spray_date', 'chemical', 'sprayer', 'position', 'notes', 'spray_paper')
        
class leafForm(ModelForm):
    class Meta:
        model = leafSamples
        fields = ('field_name', 'nitrogen', 'phosphorus', 'potassium', 'magnesium', 'calcium', 'sulfur',
                 'boron', 'zinc', 'manganese', 'iron', 'copper', 'chloride', 'date', 'guess')
        
class leafFieldsForm(ModelForm):
    class Meta:
        model = leafSampleFields
        fields = ( 'field_name', 'irrigation', 'tree', 'age', 'location')
        
class rustMitesForm(ModelForm):
    class Meta:
        model = RustMites
        fields = ('field_name', 'date', 'lens_fields', 'low', 'high')

class leafSufficiencyForm(ModelForm):
    class Meta:
        model = leafSufficiency
        fields = ( 'element', 'metric', 'column_header', 'deficient', 'low', 'optimum', 'high', 'excess')