from django.forms import ModelForm, ModelChoiceField, FileField
from django import forms
from scoutapp.models import Field
from scoutapp.models import LabelleData

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