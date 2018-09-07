from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from scoutapp.models import Field, LabelleData, labelleFieldOrder, scoutingAreas, sprayTrials, leafSamples, leafSufficiency 
from scoutapp.models import leafSampleFields, RustMites, RustMiteFields
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView 
from collections import defaultdict
from django.shortcuts import get_object_or_404
import json, os, csv
import datetime
from scoutapp.forms import fieldForm, labelleMatureNE, labelleMatureNW, labelleMatureSE, labelleMatureSW, labelleMatureC
from scoutapp.forms import sprayForm, leafForm, leafFieldsForm, rustMitesForm, leafSufficiencyForm
from utils.scoutingReport import scoutingReport
from django.core.serializers.json import DjangoJSONEncoder
from reporting.tasks import add
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from django.forms import modelformset_factory
from django.core import serializers
from django.http import JsonResponse
from django.forms.models import model_to_dict

@login_required
def report(request):
    if request.is_ajax():
        selectedLocation = request.POST.get('selectedLocation')
        scoutingList = list(scoutingAreas.objects.filter(location=selectedLocation).order_by("scoutedItem").values_list("scoutedItem", flat=True))
        scoutingListStr = scoutingList[0]
	for i in scoutingList[1:]:
	    scoutingListStr = scoutingListStr + "," + i
	strLen = len(scoutingList)
	return HttpResponse(scoutingListStr, strLen)
    if request.method == "POST":
        location = request.POST.get('location')
        startDateInput = request.POST.get('startDate')
        endDateInput = request.POST.get('endDate')
        scoutedItem = request.POST.get('scoutedItem')
        if location == 'Labelle' and scoutedItem == 'Psyllids':
            reportScript = scoutingReport()
            reportScript.sql2xl(startDateInput, endDateInput)
            reportScript.other_pests()
	    reportScript.update_data()
            reportScript.create_graph()
            #Problem here?
            cwd = os.getcwd()
            print('cwd')
            print(cwd)
	    today = datetime.date.today()
	    report_name = "DUDA_Scouting_Report(" + str(today) + ").xlsx"
            abs_path = '/home/lbadmin/projects18/reporting/scoutapp/utils/Scouting-Report-Temp.xlsx'
            print(abs_path)
            if os.path.exists(abs_path):
                print('cwd')
                with open(abs_path, "r") as excel:
                    data = excel.read()
                    response = HttpResponse(data,content_type='application/vnd.ms-excel')
                    response['Content-Disposition'] = 'attachment; filename="{}"'.format(report_name)
                    return response
    return render(request, 'report.html', { 

        })


def index(request):
    
    return render(request, 'index.html', { 
            
    })


def login(request):
    if request.method=='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        next_url = request.POST.get('next') 
        print("Next: ")
        print(next_url)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("here")
            return HttpResponseRedirect(next_url)
        else:
            return HttpResponseRedirect('/accounts/invalid')
    next = request.POST.get('next', request.GET.get('next', '')) 
    return render(request, 'login.html')

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('loggedin.html',
                             {'full_name': request.user.username})


def invalid_login(request):
    return render(request, 'invalid_login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


@login_required
def labelleMature(request):
    if request.is_ajax(): 
        ajaxMode = str(request.POST.get('ajaxMode'))
        if ajaxMode == 'dataAjax':
            openAreas = Field.objects.filter(status='Open').filter(age='Mature').order_by("area").values_list("area", flat=True)
            allData = request.POST.getlist('allData[]')
            allKeys = request.POST.getlist('allKeys[]')
            i = 0
            message = "never"
            message = "not created"
            while i < len(allData):
                index = 0
                counter = 0
                currentKey = allKeys[i]
                currentData = allData[i]
                # keyList is comma delineated and id's what data it holds. Separate out to find fields indicating
                # where to place the data
                keyList = currentKey.split(",")
                scoutDate = keyList[0]
                fieldName = keyList[1]
                scoutedStop = keyList[2]
                scoutedItem = keyList[3]
                
                fieldAge = 'Mature'
                # Next see if there is already a row with this date/field. If so, update with new field. If not, generate one
                if LabelleData.objects.filter(Date=scoutDate).filter(Field=fieldName).filter(Stop=scoutedStop).exists():
                    obj = LabelleData.objects.get(Date=str(scoutDate), Field=str(fieldName), Stop=str(scoutedStop))
                    created = False
                    
                else:
                    obj = LabelleData(Date=str(scoutDate), Field=str(fieldName), Age=fieldAge, Stop=str(scoutedStop))
                    created = True
                    message = "created"
                    lastRow = int(LabelleData.objects.latest('id').id)
                    obj.slug = lastRow + 1
                    obj.id = lastRow + 1
                    message = str(obj.id)
                if created == True:
                    #LabelleData.objects.select_related().filter(Date=scoutDate).filter(Field=fieldName).filter(Age=fieldAge).update(Stop=scoutedStop)
                    lastRow = int(LabelleData.objects.latest('id').id)
                    obj.slug = lastRow + 1
                    obj.id = lastRow + 1
                    if scoutedItem == 'Adults':
                        obj.Adult = currentData
                    elif scoutedItem == 'Eggs':
                        obj.Eggs = currentData
                    elif scoutedItem == 'Tapped':
                        obj.Tapped = currentData
                    elif scoutedItem == 'Flush':
                        obj.Flush = currentData
                    elif scoutedItem == 'LM':
                        obj.LM = currentData
                    elif scoutedItem == 'OD':
                        obj.OD = currentData
                    elif scoutedItem == 'SM':
                        obj.SM = currentData
                    elif scoutedItem == 'Leafminer':
                        obj.Leafminer = currentData
                    elif scoutedItem == 'ODLarva':
                        obj.ODLarva = currentData
                    elif scoutedItem == 'ODEggs':
                        obj.ODEggs = currentData
                    elif scoutedItem == 'Spidermites':
                        obj.SpiderMites = currentData
		    elif scoutedItem == 'Other':
                        obj.Other = currentData
                    obj.save()
                    message = str(lastRow)
                else:
                    #only update existing row
                    if scoutedItem == 'Adults':
                        obj.Adult = currentData
                    elif scoutedItem == 'Eggs':
                        obj.Eggs = currentData
                    elif scoutedItem == 'Tapped':
                        obj.Tapped = currentData
                    elif scoutedItem == 'Flush':
                        obj.Flush = currentData
                    elif scoutedItem == 'LM':
                        obj.LM = currentData
                    elif scoutedItem == 'OD':
                        obj.OD = currentData
                    elif scoutedItem == 'SM':
                        obj.SM = currentData
                    elif scoutedItem == 'Leafminer':
                        obj.Leafminer = currentData
                    elif scoutedItem == 'ODLarva':
                        obj.ODLarva = currentData
                    elif scoutedItem == 'ODEggs':
                        obj.ODEggs = currentData
                    elif scoutedItem == 'Spidermites':
                        obj.SpiderMites = currentData
                    elif scoutedItem == 'Other':
                        obj.Other = currentData
		    obj.save()
                    
                i += 1
            
            return HttpResponse(message)
        if ajaxMode == 'imageAjax':
            #Checking which stops have been completed in the selected field that day: first get field and date
            areaSelected = str(request.POST.get('selection1'))
            fieldSelected = str(request.POST.get('selection2'))
            date = str(request.POST.get('datepicker'))
            # TODO: Convert date format
            d1 = datetime.datetime.strptime(date, '%m/%d/%Y')
            datepicker = datetime.date.strftime(d1, "%Y-%m-%d")
            #Now check the database for these filters and see which stops have data entered for them, and add done stops to an array
            stopsArray = ['NW','NE','C','SW','SE']
            doneArray = []
            i = 0
            while i < 5:
                if LabelleData.objects.filter(Date=datepicker).filter(Field=fieldSelected).filter(Stop=stopsArray[i]).exists():
                    if not doneArray:
                        doneArray.append(stopsArray[i])
                    else:
                        doneArray.append(',' + stopsArray[i])
                i += 1
            #Then go through the done array
            i = 0
            imageName = 'fieldStops'
            imagesArray = ['fieldStops.svg']
            while i < len(doneArray):
                imagesArray.extend(doneArray[i] + '.svg')
                i += 1
            blah = 'blah'
            return HttpResponse(doneArray)
    openAreas = Field.objects.filter(status='Open').filter(age='Mature').order_by("area").values_list("area", flat=True).distinct()
    fieldDict = defaultdict(list, flat=True)
    j=0
    fieldList = 0
    currentArea = 0
    while j < len(openAreas):
        currentArea = openAreas[j]
        fieldList = list(Field.objects.filter(area=currentArea).filter(status='Open').filter(age='Mature').order_by("fieldName").values_list("fieldName", flat=True).distinct())
        lenFieldList = len(fieldList)
        k = 0
        while k < lenFieldList:
            currentField = fieldList[k]
            fieldDict[currentArea].append(currentField)
            k = k + 1
        j = j + 1 
    form_class = fieldForm
    form = form_class
    jsonDict = json.dumps(fieldDict)
    return render(request, 'labelle/scouting/mature.html', { 
        'form': form,
        'jsonDict': jsonDict,
        'fieldList': fieldList,
        'openAreas': openAreas,
        'fieldDict': fieldDict,
        'currentArea': currentArea,  
    })


@login_required
def labelleMatureForm(request):
    formArea = str(request.POST.get("SelectArea"))
    formField = str(request.POST.get("SelectField"))
    formStop = str(request.POST.get("formStop"))
    formDate = str(request.POST.get("datepicker"))
    d1 = datetime.datetime.strptime(formDate, '%m/%d/%Y')
    d2 = datetime.date.strftime(d1, "%Y-%m-%d")
    form_class = fieldForm
    if LabelleData.objects.filter(Date=d2).filter(Field=formField).filter(Stop=formStop).exists():
        obj = LabelleData.objects.get(Date=d2, Field=formField, Stop=formStop)
        pastAdults = obj.Adult
        pastEggs = obj.Eggs
        pastTapped = obj.Tapped
        pastFlush = obj.Flush
        pastOD = obj.OD
        pastLM = obj.LM
        pastSM = obj.SM
        pastFlag = "True"
    else:
        pastAdults = ""
        pastEggs = ""
        pastTapped = ""
        pastFlush = ""
        pastOD = ""
        pastLM = ""
        pastSM = ""
        pastFlag = "False"
    formAge = 'Mature'
    if formStop == 'NW':
        form_class = labelleMatureNW
    elif formStop == 'SW':
        form_class = labelleMatureSW
    elif formStop == 'C':
        form_class = labelleMatureC
    elif formStop == 'NE':
        form_class = labelleMatureNE
    elif formStop == 'SE':
        form_class = labelleMatureSE
    form = form_class
    return render(request, 'labelle/scouting/mature_form.html', { 
        'form': form,
        'formField': formField,
        'formStop': formStop,
        'formDate': formDate,
        'pastAdults': pastAdults,
        'pastEggs': pastEggs,
        'pastTapped': pastTapped,
        'pastFlush': pastFlush,
        'pastOD': pastOD,
        'pastLM': pastLM,
        'pastSM': pastSM,
        'pastFlag': pastFlag
    })

@login_required
def labelleYoung(request):
    if request.is_ajax(): 
        ajaxMode = str(request.POST.get('ajaxMode'))
        if ajaxMode == 'dataAjax':
            openAreas = Field.objects.filter(status='Open').filter(age='Young').order_by("area").values_list("area", flat=True)
            allData = request.POST.getlist('allData[]')
            allKeys = request.POST.getlist('allKeys[]')
            i = 0
            message = "never"
            message = "not created"
            while i < len(allData):
                index = 0
                counter = 0
                currentKey = allKeys[i]
                currentData = allData[i]
                # keyList is comma delineated and id's what data it holds. Separate out to find fields indicating
                # where to place the data
                keyList = currentKey.split(",")
                scoutDate = keyList[0]
                fieldName = keyList[1]
                scoutedStop = keyList[2]
                scoutedItem = keyList[3]
                fieldAge = 'Young'
                # Next see if there is already a row with this date/field. If so, update with new field. If not, generate one
                if LabelleData.objects.filter(Date=scoutDate).filter(Field=fieldName).filter(Stop=scoutedStop).exists():
                    obj = LabelleData.objects.get(Date=str(scoutDate), Field=str(fieldName), Stop=str(scoutedStop))
                    created = False
                else:
                    obj = LabelleData(Date=str(scoutDate), Field=str(fieldName), Age=fieldAge, Stop=str(scoutedStop))
                    created = True
                    message = "created"
                    lastRow = int(LabelleData.objects.latest('id').id)
                    obj.slug = lastRow + 1
                    obj.id = lastRow + 1
                    message = str(obj.id)
                if created == True:
                    lastRow = int(LabelleData.objects.latest('id').id)
                    obj.slug = lastRow + 1
                    obj.id = lastRow + 1
                    if scoutedItem == 'Adults':
                        obj.Adult = currentData
                    elif scoutedItem == 'Eggs':
                        obj.Eggs = currentData
                    elif scoutedItem == 'Tapped':
                        obj.Tapped = currentData
                    elif scoutedItem == 'Flush':
                        obj.Flush = currentData
                    elif scoutedItem == 'LM':
                        obj.LM = currentData
                    elif scoutedItem == 'OD':
                        obj.OD = currentData
                    elif scoutedItem == 'SM':
                        obj.SM = currentData
                    elif scoutedItem == 'Leafminer':
                        obj.Leafminer = currentData
                    elif scoutedItem == 'ODLarva':
                        obj.ODLarva = currentData
                    elif scoutedItem == 'ODEggs':
                        obj.ODEggs = currentData
                    elif scoutedItem == 'Spidermites':
                        obj.SpiderMites = currentData
                    obj.save()
                    message = str(lastRow)
                else:
                    #only update existing row
                    if scoutedItem == 'Adults':
                        obj.Adult = currentData
                    elif scoutedItem == 'Eggs':
                        obj.Eggs = currentData
                    elif scoutedItem == 'Tapped':
                        obj.Tapped = currentData
                    elif scoutedItem == 'Flush':
                        obj.Flush = currentData
                    elif scoutedItem == 'LM':
                        obj.LM = currentData
                    elif scoutedItem == 'OD':
                        obj.OD = currentData
                    elif scoutedItem == 'SM':
                        obj.SM = currentData
                    elif scoutedItem == 'Leafminer':
                        obj.Leafminer = currentData
                    elif scoutedItem == 'ODLarva':
                        obj.ODLarva = currentData
                    elif scoutedItem == 'ODEggs':
                        obj.ODEggs = currentData
                    elif scoutedItem == 'Spidermites':
                        obj.SpiderMites = currentData
                    obj.save() 
                i += 1
            return HttpResponse(message)
        if ajaxMode == 'imageAjax':
            #Checking which stops have been completed in the selected field that day: first get field and date
            areaSelected = str(request.POST.get('selection1'))
            fieldSelected = str(request.POST.get('selection2'))
            date = str(request.POST.get('datepicker'))
            # TODO: Convert date format
            d1 = datetime.datetime.strptime(date, '%m/%d/%Y')
            datepicker = datetime.date.strftime(d1, "%Y-%m-%d")
            #Now check the database for these filters and see which stops have data entered for them, and add done stops to an array
            stopsArray = ['NW','NE','C','SW','SE']
            doneArray = []
            i = 0
            while i < 5:
                if LabelleData.objects.filter(Date=datepicker).filter(Field=fieldSelected).filter(Stop=stopsArray[i]).exists():
                    if not doneArray:
                        doneArray.append(stopsArray[i])
                    else:
                        doneArray.append(',' + stopsArray[i])
                i += 1
            #Then go through the done array
            i = 0
            imageName = 'fieldStops'
            imagesArray = ['fieldStops.svg']
            while i < len(doneArray):
                imagesArray.extend(doneArray[i] + '.svg')
                i += 1
            blah = 'blah'
            return HttpResponse(doneArray)
    openAreas = Field.objects.filter(status='Open').filter(age='Young').order_by("area").values_list("area", flat=True).distinct()
    fieldDict = defaultdict(list, flat=True)
    j=0
    fieldList = 0
    currentArea = 0
    while j < len(openAreas):
        currentArea = openAreas[j]
        fieldList = list(Field.objects.filter(area=currentArea).filter(status='Open').filter(age='Young').order_by("fieldName").values_list("fieldName", flat=True).distinct())
        lenFieldList = len(fieldList)
        k = 0
        while k < lenFieldList:
            currentField = fieldList[k]
            fieldDict[currentArea].append(currentField)
            k = k + 1
        j = j + 1 
    form_class = fieldForm
    form = form_class
    jsonDict = json.dumps(fieldDict)
    
    return render(request, 'labelle/scouting/young.html', { 
        'form': form,
        'jsonDict': jsonDict,
        'fieldList': fieldList,
        'openAreas': openAreas,
        'fieldDict': fieldDict,
        'currentArea': currentArea,  
    })


@login_required
def labelleYoungForm(request):
    formArea = str(request.POST.get("SelectArea"))
    formField = str(request.POST.get("SelectField"))
    formStop = str(request.POST.get("formStop"))
    formDate = str(request.POST.get("datepicker"))
    d1 = datetime.datetime.strptime(formDate, '%m/%d/%Y')
    d2 = datetime.date.strftime(d1, "%Y-%m-%d")
    form_class = fieldForm
    if LabelleData.objects.filter(Date=d2).filter(Field=formField).filter(Stop=formStop).exists():
        obj = LabelleData.objects.get(Date=d2, Field=formField, Stop=formStop)
        pastAdults = obj.Adult
        pastEggs = obj.Eggs
        pastLeafminer = obj.Leafminer
        pastODEggs = obj.ODEggs
        pastODLarva = obj.ODLarva
        pastSpiderMites = obj.SpiderMites
        pastFlag = "True"
    else:
        pastAdults = ""
        pastEggs = ""
        pastLeafminer = ""
        pastODEggs = ""
        pastODLarva = ""
        pastSpiderMites = ""
        pastFlag = "False"
    formAge = 'Mature'
    if formStop == 'NW':
        form_class = labelleMatureNW
    elif formStop == 'SW':
        form_class = labelleMatureSW
    elif formStop == 'C':
        form_class = labelleMatureC
    elif formStop == 'NE':
        form_class = labelleMatureNE
    elif formStop == 'SE':
        form_class = labelleMatureSE
    form = form_class
    message="not yet"
    return render(request, 'labelle/scouting/young_form.html', { 
        'message': message,
        'form': form,
        'formField': formField,
        'formStop': formStop,
        'formDate': formDate,
        'pastAdults': pastAdults,
        'pastEggs': pastEggs,
        'pastLeafminer': pastLeafminer,
        'pastODEggs': pastODEggs,
        'pastODLarva': pastODLarva,
        'pastSpiderMites': pastSpiderMites,
        'pastFlag': pastFlag
    })

def sprayInput(request):
    openAreas = Field.objects.order_by("area").values_list("area", flat=True).distinct()
    trialList = sprayTrials.objects.order_by("name").values_list("name", flat=True).distinct()
    fieldDict = defaultdict(list, flat=True)
    j=0
    fieldList = 0
    currentArea = 0
    while j < len(openAreas):
        currentArea = openAreas[j]
        fieldList = list(Field.objects.filter(area=currentArea).order_by("fieldName").values_list("fieldName", flat=True).distinct())
        lenFieldList = len(fieldList)
        k = 0
        while k < lenFieldList:
            currentField = fieldList[k]
            fieldDict[currentArea].append(currentField)
            k = k + 1
        j = j + 1 
    form_class = sprayForm
    form = form_class
    jsonDict = json.dumps(fieldDict)
    if request.method == "POST":
        form = sprayForm(request.POST, request.FILES)
        if form.is_valid():
            form_area = str(request.POST.get("selectArea"))
            field_name = str(request.POST.get("field"))
            trial_name = str(request.POST.get("name"))
            spray_date = str(request.POST.get("datepicker"))
            position = str(request.POST.get("position"))
            chemical = str(request.POST.get("chemical"))
            sprayer = str(request.POST.get("sprayer"))
            notes = str(request.POST.get("notes"))
            obj = sprayTrials(name=trial_name, field=field_name, chemical=chemical, spray_date=spray_date, position=position, sprayer=sprayer, notes=notes)
            obj.spray_paper = form.cleaned_data['spray_paper']
            obj.save()
            
            #Run celery task daemon below
            last_obj = sprayTrials.objects.latest('id')
            row_id = str(last_obj.id)
            print(row_id)
            image_path = str(sprayTrials.objects.filter(id=row_id).values_list("spray_paper", flat=True))
            add.delay(image_path, row_id)
            
            #m = sprayTrials.objects.get(id=row_id)
            #m.model_pic = form.cleaned_data['image']
            #m.save()
            return HttpResponseRedirect('/')
        else:
            # form instance will have errors so we pass it into template
            return render(request, 'labelle/spray_input.html', {'form': form})
    
    return render(request, 'labelle/spray_input.html', { 
        'form': form,
        'jsonDict': jsonDict,
        'fieldList': fieldList,
        'openAreas': openAreas,
        'fieldDict': fieldDict,
        'currentArea': currentArea, 
        'trialList': trialList
    })

def sprayReport(request):
    name_list = sprayTrials.objects.order_by("name").values_list("name", flat=True)
    field_list = sprayTrials.objects.order_by("name").values_list("field", flat=True)
    date_list = sprayTrials.objects.order_by("name").values_list("spray_date", flat=True)
    chemical_list = sprayTrials.objects.order_by("name").values_list("chemical", flat=True)
    sprayer_list = sprayTrials.objects.order_by("name").values_list("sprayer", flat=True)
    position_list = sprayTrials.objects.order_by("name").values_list("position", flat=True)
    notes_list = sprayTrials.objects.order_by("name").values_list("notes", flat=True)
    num_mean_list = sprayTrials.objects.order_by("name").values_list("num_mean_in", flat=True)
    num_med_list = sprayTrials.objects.order_by("name").values_list("num_median_in", flat=True)
    num_stdev_list = sprayTrials.objects.order_by("name").values_list("num_stdev_in", flat=True)
    vol_mean_list = sprayTrials.objects.order_by("name").values_list("vol_mean_in", flat=True)
    vol_median_list = sprayTrials.objects.order_by("name").values_list("vol_median_in", flat=True)
    coverage_list = sprayTrials.objects.order_by("name").values_list("coverage_percent", flat=True)
    
    names_distinct = sprayTrials.objects.order_by("name").values_list("name", flat=True).distinct()
    fields_distinct = sprayTrials.objects.order_by("field").values_list("field", flat=True).distinct()
    dates_distinct = sprayTrials.objects.order_by("spray_date").values_list("spray_date", flat=True).distinct()
    chemicals_distinct = sprayTrials.objects.order_by("chemical").values_list("chemical", flat=True).distinct()
    sprayers_distinct = sprayTrials.objects.order_by("sprayer").values_list("sprayer", flat=True).distinct()
    position_distinct = sprayTrials.objects.order_by("position").values_list("position", flat=True).distinct
    

    name_json = json.dumps(list(name_list), cls=DjangoJSONEncoder)
    field_json = json.dumps(list(field_list), cls=DjangoJSONEncoder)
    date_json = json.dumps(list(date_list), cls=DjangoJSONEncoder)
    chemical_json = json.dumps(list(chemical_list), cls=DjangoJSONEncoder)
    sprayer_json = json.dumps(list(sprayer_list), cls=DjangoJSONEncoder)
    position_json = json.dumps(list(position_list), cls=DjangoJSONEncoder)
    notes_json = json.dumps(list(notes_list), cls=DjangoJSONEncoder)
    
    form_class = sprayForm
    form = form_class
    
    return render(request, 'spray_report.html', { 
        'form': form,
        'name_json': name_json,
        'field_json': field_json,
        'date_json': date_json,
        'chemical_json': chemical_json,
        'sprayer_json': sprayer_json,
        'position_json': position_json,
        'notes_json': notes_json,
        'num_mean_list': num_mean_list,
        'num_med_list': num_med_list,
        'num_stdev_list': num_stdev_list,
        'vol_mean_list': vol_mean_list,
        'vol_median_list': vol_median_list,
        'coverage_list': coverage_list,
        'names_distinct': names_distinct,
        'fields_distinct': fields_distinct,
        'dates_distinct': dates_distinct,
        'chemicals_distinct': chemicals_distinct,
        'sprayers_distinct': sprayers_distinct,
        'position_distinct': position_distinct
        
    })

@login_required
def labelle_leaf_samples(request):
    if request.method == 'POST':
        form = leafFieldsForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            obj = leafSampleFields()
            obj.field_name = form.cleaned_data['field_name']
            obj.age = form.cleaned_data['age']
            obj.irrigation = form.cleaned_data['irrigation']
            obj.tree = form.cleaned_data['tree']
            obj.location = form.cleaned_data['location']
            obj.save()
            # redirect to a new URL:
            # return HttpResponseRedirect('/manage')
    form_class = leafFieldsForm
    form = form_class
    message = 'hi'
    leafFields = leafSampleFields.objects.all().order_by("field_name")
    print leafFields
    nutrients = leafSufficiency.objects.values("element", "metric", "deficient", "low", "optimum", "high", 
                                               "excess", "column_header", "id")
    
    return render(request, 'manage_labelle/leaf_samples.html', { 
        'message': message,
        'form': form,
        'leafFields': leafFields,
        'nutrients': nutrients
    })

@login_required(redirect_field_name='next')
def leafRemove(request):
    leafFormSet = modelformset_factory(leafSamples, fields=('id', 'field_name', 'guess'), extra=0)
    if request.method == "POST":
        #form = leafForm(request.POST, request.FILES)
        remove_date = str(request.POST.get("datepicker"))
        d1 = datetime.datetime.strptime(remove_date, '%m/%d/%Y')
        remove_date = datetime.date.strftime(d1, "%Y-%m-%d")
        leafSamples.objects.filter(date=remove_date).delete()
        print(remove_date)
        form_class = leafForm
        form = form_class
        return render(request, 'labelle/leaf_input.html', { 
            'form': form,
        })    
        
    else:
        form_class = leafForm
        form = form_class
    return render(request, 'labelle/leaf_remove.html', { 
        'form': form,
    })

@login_required
def manage(request):
    message = 'hi'
    return render(request, 'manage.html', { 
        'message': message
    })

@login_required
def labelle_leaf_samples_add_field(request):
    if request.method == 'POST':
        form = leafFieldsForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            obj = leafSampleFields()
            obj.field_name = form.cleaned_data['field_name']
            obj.age = form.cleaned_data['age']
            obj.irrigation = form.cleaned_data['irrigation']
            obj.tree = form.cleaned_data['tree']
            obj.location = form.cleaned_data['location']
            obj.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/manage')
    form_class = leafFieldsForm
    form = form_class
    message = 'hi'
    leafFields = leafSampleFields.objects.order_by("field_name").values_list("field_name", flat=True)
    #leafFields = json.dumps(leafFields, cls=DjangoJSONEncoder)
    
    print leafFields
    
    return render(request, 'manage_labelle/leaf_samples_add_field.html', { 
        'message': message,
        'form': form,
        'leafFields': leafFields
    })

@login_required
def labelle_leaf_samples_edit_field(request):
    flag = str(request.POST.get("flag"))
    if flag == "postId":
        edit_id = str(request.POST.get("editId"))
        print(edit_id)
        edit_record = leafSampleFields.objects.get(id=edit_id)
        form_class = leafFieldsForm(instance=edit_record)
        form = form_class
        message = 'hi'
        leafFields = leafSampleFields.objects.order_by("field_name").values_list("field_name", flat=True)
        return render(request, 'manage_labelle/leaf_samples_edit_field.html', { 
            'message': message,
            'form': form,
            'edit_id': edit_id,
            'leafFields': leafFields
        })
    form = leafFieldsForm(request.POST)
    # Check if the form is valid:
    if form.is_valid():
        edit_id = str(request.POST.get("editId"))
        obj = leafSampleFields.objects.get(id=edit_id)
        obj.field_name = form.cleaned_data['field_name']
        obj.age = form.cleaned_data['age']
        obj.irrigation = form.cleaned_data['irrigation']
        obj.tree = form.cleaned_data['tree']
        obj.location = form.cleaned_data['location']
        obj.save()
        # redirect to a new URL:
        return HttpResponseRedirect('/manage_labelle/leaf_samples')
    return HttpResponseRedirect('/')

@login_required
def labelle_leaf_samples_add_nutrient(request):
    if request.method == 'POST':
        form = leafSufficiencyForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            obj = leafSufficiencyForm()
            obj.element = form.cleaned_data['element']
            obj.metric = form.cleaned_data['metric']
            obj.deficient = form.cleaned_data['deficient']
            obj.low = form.cleaned_data['low']
            obj.optimum = form.cleaned_data['optimum']
            obj.high = form.cleaned_data['high']
            obj.excess = form.cleaned_data['excess']
            obj.column_header = form.cleaned_data['column_header']
            obj.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/manage')
    form_class = leafSufficiencyForm
    form = form_class
    message = 'hi'
    return render(request, 'manage_labelle/leaf_samples_add_nutrient.html', { 
        'message': message,
        'form': form,
    })

@login_required
def labelle_leaf_samples_edit_nutrient(request):
    flag = str(request.POST.get("flag"))
    if flag == "postId":
        edit_id = str(request.POST.get("nutrientId"))
        print(edit_id)
        edit_record = leafSufficiency.objects.get(id=edit_id)
        form_class = leafSufficiencyForm(instance=edit_record)
        form = form_class
        message = 'hi'
        return render(request, 'manage_labelle/leaf_samples_edit_nutrient.html', { 
            'message': message,
            'form': form,
            'edit_id': edit_id,
        })
    form = leafSufficiencyForm(request.POST)
    # Check if the form is valid:
    if form.is_valid():
        edit_id = str(request.POST.get("editId"))
        obj = leafSufficiency.objects.get(id=edit_id)
        obj.element = form.cleaned_data['element']
        obj.metric = form.cleaned_data['metric']
        obj.deficient = form.cleaned_data['deficient']
        obj.low = form.cleaned_data['low']
        obj.optimum = form.cleaned_data['optimum']
        obj.high = form.cleaned_data['high']
        obj.excess = form.cleaned_data['excess']
        obj.column_header = form.cleaned_data['column_header']
        obj.save()
        # redirect to a new URL:
        return HttpResponseRedirect('/manage_labelle/leaf_samples')
    return HttpResponseRedirect('/')

@login_required
def rustMites(request):
    if request.method == 'POST':
        date = str(request.POST.get('datepicker'))
        d1 = datetime.datetime.strptime(date, '%m/%d/%Y')
        date = datetime.date.strftime(d1, "%Y-%m-%d")
        selected_field = str(request.POST.get('SelectField'))
        selected_area = str(request.POST.get('SelectArea'))
        lens_fields = str(request.POST.get('lensFields'))
        low_mites = str(request.POST.get('lowMites'))
        high_mites = str(request.POST.get('highMites'))
        notes = str(request.POST.get('notes'))
        obj = RustMites()
        obj.date = date
        obj.field_name = selected_field
        obj.lens_fields = lens_fields
        obj.low = low_mites
        obj.high = high_mites
        obj.notes = notes
        obj.save()
        
    locations_list = RustMiteFields.objects.order_by("location").values_list("location", flat=True).distinct()
    fields_dict = {}
    for location in locations_list:
        fields_list = RustMiteFields.objects.filter(location=location).order_by("field_name").values_list("field_name", flat=True)
        fields_dict[location] = list(fields_list)
    print(type(fields_dict))
    print(fields_dict)
    form_class = rustMitesForm
    form = form_class
    fields_json = json.dumps(fields_dict, cls=DjangoJSONEncoder)
    return render(request, 'labelle/scouting/rust_mites.html', { 
        'form': form,
        'locations_list': locations_list,
        'fields_json': fields_json
        
    })

def rustMiteReport(request):
    # If request is AJAX, grab the POST variables
    if request.is_ajax():
        flag = request.POST.get("flag")
        if flag == 'table':
            start_date = request.POST.get("startDate")
            d1 = datetime.datetime.strptime(start_date, '%m/%d/%Y')
            start_date = datetime.date.strftime(d1, "%Y-%m-%d")
            end_date = request.POST.get("endDate")
            d1 = datetime.datetime.strptime(end_date, '%m/%d/%Y')
            end_date = datetime.date.strftime(d1, "%Y-%m-%d")
            # Then create a dictionary of dictionaries for all (latest) data within the given date range, then send back in JSON
            mites_data = {}
            fields_list = RustMiteFields.objects.values_list("field_name", flat=True)
            for field in fields_list:
                print(field)
                rowDict = {'field_name': '', 'date': '', 'lens_fields': '', 'low': '', 'high': '',  'notes': ''}
                keys_list = ['field_name', 'date', 'lens_fields', 'low', 'high', 'notes']
                for key in keys_list:
                    if key == 'date':
                        try:
                            d1 = RustMites.objects.filter(field_name=field).filter(
                                date__range=[start_date, end_date]).values_list(key, flat=True).latest('id')
                    	    d2 = str(datetime.date.strftime(d1, '%m/%d/%y'))
                    	    rowDict[key] = d2
                        except:
                            print('date conversion fail')
                    else:
                        try:
                            rowDict[key] = RustMites.objects.filter(field_name=field).filter(
                                date__range=[start_date, end_date]).values_list(key, flat=True).latest('id')
                        except:
                            print("failed")
                mites_data[field] = rowDict
            print(mites_data)
            return JsonResponse(mites_data, safe=False)
        else:
            graph_field = request.POST.get("graphField")
            start_date = request.POST.get("graphStartDate")
            d1 = datetime.datetime.strptime(start_date, '%m/%d/%Y')
            start_date = datetime.date.strftime(d1, "%Y-%m-%d")
            end_date = request.POST.get("graphEndDate")
            d1 = datetime.datetime.strptime(end_date, '%m/%d/%Y')
            end_date = datetime.date.strftime(d1, "%Y-%m-%d")
            fields_distinct = RustMites.objects.order_by("field_name").values_list("field_name", flat=True).distinct()
            if graph_field == "All":
                print("all")
                mites_history = []
                dates_distinct = RustMites.objects.order_by("date").filter(
                                    date__range=[start_date, end_date]).values_list("date", flat=True).distinct()
                week_num_list = []
                for date in dates_distinct:
                    week_num_list.append(date.isocalendar()[1])
                week_nums_distinct = list(set(week_num_list))
                i = 0
                # Nust order week_nums_distinct by ascending date
                week_nums_distinct.sort()
                for week in week_nums_distinct:
                    current_lows = []
                    current_highs = []
                    current_lens = []
                    totals_dict = []
                    print(week)
                    print(week_nums_distinct)
                    print(week_num_list)
                    indices = [j for j, x in enumerate(week_num_list) if x == week]
                    print(indices)
                    for num in indices:
                        print(num)
                        print(dates_distinct[num])
                        for field in fields_distinct:
                            print(field)
                            current_lows.append(list(RustMites.objects.order_by("date").filter(date=dates_distinct[num]).filter(
                                    field_name=field).values_list("low", flat=True).distinct()))
                            current_highs.append(list(RustMites.objects.order_by("date").filter(date=dates_distinct[num]).filter(
                                    field_name=field).values_list("high", flat=True).distinct()))
                            current_lens.append(list(RustMites.objects.order_by("date").filter(date=dates_distinct[num]).filter(
                                    field_name=field).values_list("lens_fields", flat=True).distinct()))
                    # Calculate the total percentage of infested per lense field in this week and add to data list
                    ii = 0
                    flat_lows = []
                    while ii < len(current_lows):
                        jj = 0
                        while jj < len(current_lows[ii]):
                            print(current_lows[ii][jj])
                            flat_lows.append(current_lows[ii][jj])
                            jj = jj+1
                        ii= ii + 1
                    ii = 0
                    flat_highs = []
                    while ii < len(current_highs):
                        jj = 0
                        while jj < len(current_highs[ii]):
                            print(current_highs[ii][jj])
                            flat_highs.append(current_highs[ii][jj])
                            jj = jj+1
                        ii= ii + 1
                    ii = 0
                    flat_lens = []
                    while ii < len(current_lens):
                        jj = 0
                        while jj < len(current_lens[ii]):
                            print(current_lens[ii][jj])
                            flat_lens.append(current_lens[ii][jj])
                            jj = jj+1
                        ii= ii + 1
                    
                    print(flat_lows)
                    flat_lows = map(int, flat_lows)
                    flat_highs = map(int, flat_highs)
                    flat_lens = map(int, flat_lens)
                    print("here")
                    week_lows = sum(flat_lows)
                    week_highs = sum(flat_highs)
                    week_lens = sum(flat_lens)
                    week_percentage = float((week_lows + week_highs) / week_lens)
                    print(week_percentage)
                    week_date = dates_distinct[indices[0]]
                    week_list = ['All', week_date, week_lens, week_lows, week_highs]
                    mites_history.append(week_list)
                    print(mites_history)
                
            else:
                mites_history = RustMites.objects.order_by("date").filter(field_name=graph_field).filter(
                                date__range=[start_date, end_date]).values_list(
                                "field_name", "date", "lens_fields", "low", "high").distinct()
            mites_history_json = json.dumps(list(mites_history), cls=DjangoJSONEncoder)
            print(mites_history)
            return JsonResponse(mites_history_json, safe=False)
            
    #
    # Query most recent mites scouting data for table
    #
    mites_data = {}
    fields_list = RustMiteFields.objects.values_list("field_name", flat=True)
    #for every field, create a temporary dictionary with columns as keys and data as values
    for field in fields_list:
        print(field)
        rowDict = {'field_name': '', 'date': '', 'lens_fields': '', 'low': '', 'high': '', 'notes': ''}
        keys_list = ['field_name', 'date', 'lens_fields', 'low', 'high', 'notes']
        for key in keys_list:
            if key == 'date':
                try:
                    d1 = RustMites.objects.filter(field_name=field).values_list(key, flat=True).latest('id')
                    d2 = str(datetime.date.strftime(d1, '%m/%d/%y'))
                    rowDict[key] = d2
                except:
                    print('date conversion fail')
            else:
                try:
                    rowDict[key] = RustMites.objects.filter(field_name=field).values_list(key, flat=True).latest('id')
                except:
                    print("failed")
        # Add each temporary dictionary to a master dictionary of dictionaries, and then convert to JSON to pass to template
        mites_data[field] = rowDict
    print(mites_data)
    mites_json = json.dumps(mites_data, cls=DjangoJSONEncoder)
    
    #
    # Also, get data over the past year for the first alphabetical field for default time graph
    #
    start_date = datetime.date.today() - datetime.timedelta(days=365)
    end_date = datetime.date.today()
    fields_distinct = RustMites.objects.order_by("field_name").values_list("field_name", flat=True).distinct()
    mites_history = RustMites.objects.order_by("date").filter(field_name=fields_distinct[0]).filter(
                    date__range=[start_date, end_date]).values_list("field_name", "date", "lens_fields", "low", "high").distinct()
    
    mites_history_json = json.dumps(list(mites_history), cls=DjangoJSONEncoder)
    print(mites_history)
    
    return render(request, 'rust_mite_report.html', {
            "mites_json": mites_json,
            "mites_history_json": mites_history_json,
            "fields_distinct": fields_distinct
            })

def leafInput(request):
    leafFormSet = modelformset_factory(leafSamples, fields=('id', 'field_name', 'guess'), extra=0)
    if request.method == "POST":
        #form = leafForm(request.POST, request.FILES)
        formset = leafFormSet(request.POST)
        if formset.is_valid():
            instances = formset.save()
        form_class = leafForm
        form = form_class
        return render(request, 'labelle/leaf_input.html', { 
            'form': form,
        })    
        
    else:
        form_class = leafForm
        form = form_class
    return render(request, 'labelle/leaf_input.html', { 
        'form': form,
    })


def leafCheck(request):
    form = leafForm(request.POST, request.FILES)
    if form.is_valid():
        reader = csv.reader(request.FILES['spray_paper'])
        sample_date = str(request.POST.get("datepicker"))
        d1 = datetime.datetime.strptime(sample_date, '%m/%d/%Y')
        sample_date = datetime.date.strftime(d1, "%Y-%m-%d")
        field_list = leafSampleFields.objects.values_list("field_name", flat=True)
        uncertain_list = []
        certain_list = []
        uncertain_name_list = []
        guess_name_list = []
        uncertain_ids = []
        elements_list = leafSufficiency.objects.values_list("element", "column_header")
        columns = next(reader)
        i = 0
        columns_dict = {}
        for column in columns:
            print(column)
            for element in elements_list:
                print(element)
                if element[1] == column:
                    columns_dict[element[0]] = i
                    continue
            i += 1
        print(columns_dict)
        for row in reader:
            field_name = row[2]
            if field_name == 'SampleID':
                continue
            print(field_name)
            guess = process.extractOne(field_name, field_list)
            if guess[1] < 100:
                uncertain_list.append(row)
            else:
                certain_list.append(field_name)
                date = sample_date
                nitrogen = row[columns_dict.get('nitrogen')]
                phosphorus = row[columns_dict['phosphorus']]
                potassium = row[columns_dict['potassium']]
                magnesium = row[columns_dict['magnesium']]
                calcium = row[columns_dict['calcium']]
                sulfur = row[columns_dict['sulfur']]
                boron = row[columns_dict['boron']]
                zinc = row[columns_dict['zinc']]
                manganese = row[columns_dict['manganese']]
                iron = row [columns_dict['iron']]
                copper = row[columns_dict['copper']]
                chloride = row[columns_dict['chloride']]
                obj = leafSamples(field_name=guess[0], nitrogen=nitrogen, phosphorus=phosphorus, 
                                   potassium=potassium, magnesium=magnesium, calcium=calcium, sulfur=sulfur, 
                                   boron=boron, zinc=zinc, manganese=manganese, iron=iron, copper=copper, 
                                   chloride=chloride, date=date)
                obj.save()
        remaining_list = list(set(field_list) - set(certain_list))
        i = 0
        while i < len(uncertain_list):
            field_name = uncertain_list[i][2]
            uncertain_name_list.append(field_name)
            print(field_name)
            guess = process.extractOne(field_name, remaining_list)
            guess_name_list.append(guess)
            date = sample_date
            nitrogen = uncertain_list[i][5]
            phosphorus = uncertain_list[i][6]
            potassium = uncertain_list[i][7]
            magnesium = uncertain_list[i][8]
            calcium = uncertain_list[i][9]
            sulfur = uncertain_list[i][10]
            boron = uncertain_list[i][11]
            zinc = uncertain_list[i][12]
            manganese = uncertain_list[i][13]
            iron = uncertain_list[i] [14]
            copper = uncertain_list[i][15]
            chloride = uncertain_list[i][26]
            obj = leafSamples(field_name=field_name, nitrogen=nitrogen, phosphorus=phosphorus, 
                               potassium=potassium, magnesium=magnesium, calcium=calcium, sulfur=sulfur, 
                               boron=boron, zinc=zinc, manganese=manganese, iron=iron, copper=copper, 
                               chloride=chloride, date=date, guess=guess[0])
            obj.save()
            uncertain_ids.append(leafSamples.objects.latest('id').id)
            print(guess)
            i += 1
        print(uncertain_ids)
        uncertain_objs = leafSamples.objects.filter(id__in=uncertain_ids)
        leafFormSet = modelformset_factory(leafSamples, fields=('id', 'field_name', 'guess'), extra=0)
        formset = leafFormSet(queryset=leafSamples.objects.filter(id__in=uncertain_ids))
        print(uncertain_objs)
    else:
        print form.errors
        print request.FILES
        #form = UploadFileForm()
    return render(request, 'labelle/leaf_check.html', { 
        'uncertain_name_list': uncertain_name_list,
        'guess_name_list': guess_name_list,
        'uncertain_objs': uncertain_objs,
        'form': form,
        'formset': formset,
    })  

def leafReport(request):
    if request.is_ajax():
        flag = str(request.POST.get('flag'))
        
        if flag == 'element':
            #Get all POST data from AJAX request
            line_selected_field = str(request.POST.get('selectedField'))
            line_selected_element = str(request.POST.get('selectedElement'))
            line_start_date = str(request.POST.get('lineStartDate'))
            line_end_date = str(request.POST.get('lineEndDate'))

            #Put dates in correct format for queries 
            line_start_date = datetime.datetime.strptime(line_start_date, '%m/%d/%Y').strftime('%Y-%m-%d')
            line_end_date = datetime.datetime.strptime(line_end_date, '%m/%d/%Y').strftime('%Y-%m-%d') 

            # Query correct element data for line graph selection
            elements_distinct = ('nitrogen', 'phosphorus', 'potassium', 'magnesium', 'calcium', 'sulfur',
                     'boron', 'zinc', 'manganese', 'iron', 'copper', 'chloride')
            if line_selected_element == "nitrogen":
                element_year = leafSamples.objects.order_by("date").filter(field_name=line_selected_field).filter(
                    date__range=[line_start_date, line_end_date]).values_list("field_name", "date", "nitrogen").distinct()
                element_year_json = json.dumps(list(element_year), cls=DjangoJSONEncoder)
            elif line_selected_element == "phosphorus":
                element_year = leafSamples.objects.order_by("date").filter(field_name=line_selected_field).filter(
                    date__range=[line_start_date, line_end_date]).values_list("field_name", "date", "phosphorus").distinct()
                element_year_json = json.dumps(list(element_year), cls=DjangoJSONEncoder)
            elif line_selected_element == "potassium":
                element_year = leafSamples.objects.order_by("date").filter(field_name=line_selected_field).filter(
                    date__range=[line_start_date, line_end_date]).values_list("field_name", "date", "potassium").distinct()
                element_year_json = json.dumps(list(element_year), cls=DjangoJSONEncoder)
            elif line_selected_element == "magnesium":
                element_year = leafSamples.objects.order_by("date").filter(field_name=line_selected_field).filter(
                    date__range=[line_start_date, line_end_date]).values_list("field_name", "date", "magnesium").distinct()
                element_year_json = json.dumps(list(element_year), cls=DjangoJSONEncoder)
            elif line_selected_element == "calcium":
                element_year = leafSamples.objects.order_by("date").filter(field_name=line_selected_field).filter(
                    date__range=[line_start_date, line_end_date]).values_list("field_name", "date", "calcium").distinct()
                element_year_json = json.dumps(list(element_year), cls=DjangoJSONEncoder)
            elif line_selected_element == "sulfur":
                element_year = leafSamples.objects.order_by("date").filter(field_name=line_selected_field).filter(
                    date__range=[line_start_date, line_end_date]).values_list("field_name", "date", "sulfur").distinct()
                element_year_json = json.dumps(list(element_year), cls=DjangoJSONEncoder)
            elif line_selected_element == "boron":
                element_year = leafSamples.objects.order_by("date").filter(field_name=line_selected_field).filter(
                    date__range=[line_start_date, line_end_date]).values_list("field_name", "date", "boron").distinct()
                element_year_json = json.dumps(list(element_year), cls=DjangoJSONEncoder)
            elif line_selected_element == "zinc":
                element_year = leafSamples.objects.order_by("date").filter(field_name=line_selected_field).filter(
                    date__range=[line_start_date, line_end_date]).values_list("field_name", "date", "zinc").distinct()
                element_year_json = json.dumps(list(element_year), cls=DjangoJSONEncoder)
            elif line_selected_element == "manganese":
                element_year = leafSamples.objects.order_by("date").filter(field_name=line_selected_field).filter(
                    date__range=[line_start_date, line_end_date]).values_list("field_name", "date", "manganese").distinct()
                element_year_json = json.dumps(list(element_year), cls=DjangoJSONEncoder)
            elif line_selected_element == "iron":
                element_year = leafSamples.objects.order_by("date").filter(field_name=line_selected_field).filter(
                    date__range=[line_start_date, line_end_date]).values_list("field_name", "date", "iron").distinct()
                element_year_json = json.dumps(list(element_year), cls=DjangoJSONEncoder)
            elif line_selected_element == "copper":
                element_year = leafSamples.objects.order_by("date").filter(field_name=line_selected_field).filter(
                    date__range=[line_start_date, line_end_date]).values_list("field_name", "date", "copper").distinct()
                element_year_json = json.dumps(list(element_year), cls=DjangoJSONEncoder)
            elif line_selected_element == "chloride":
                element_year = leafSamples.objects.order_by("date").filter(field_name=line_selected_field).filter(
                    date__range=[line_start_date, line_end_date]).values_list("field_name", "date", "chloride").distinct()
                element_year_json = json.dumps(list(element_year), cls=DjangoJSONEncoder)

            elements_json = json.dumps(list(elements_distinct), cls=DjangoJSONEncoder)

            return JsonResponse(element_year_json, safe=False)
        
        if flag == 'content':
            bar_selected_field = str(request.POST.get('barSelectedField'))
            bar_date = str(request.POST.get('barDate'))
            bar_date = datetime.datetime.strptime(bar_date, '%B %Y').strftime('%Y-%m-%d')
            time_delta = datetime.timedelta(days=30)
            bar_date_end = datetime.datetime.strptime(bar_date, '%Y-%m-%d') + time_delta
            print(bar_date)
            print(bar_date_end)
            # Query to update leaf content bar graph, then serialize the data to JSON
            content_data = leafSamples.objects.filter(field_name=bar_selected_field).filter(
                    date__range=[bar_date, bar_date_end]).first()
            print(content_data)
            print(bar_selected_field)
            content_data_json = serializers.serialize('json', [content_data])
            
            return JsonResponse(content_data_json, safe=False)
        
        if flag == 'sufficiency':
            suff_selected_field = str(request.POST.get('suffSelectedField'))
            suff_date = str(request.POST.get('suffDate'))
            suff_date = datetime.datetime.strptime(suff_date, '%B %Y').strftime('%Y-%m-%d')
            time_delta = datetime.timedelta(days=30)
            suff_date_end = datetime.datetime.strptime(suff_date, '%Y-%m-%d') + time_delta
            print(suff_selected_field)

            # Numerical analysis of leaf content for sufficiency range
            recent_data = leafSamples.objects.filter(field_name=suff_selected_field).filter(
                    date__range=[suff_date, suff_date_end]).latest('id')
            recent_dict = model_to_dict(recent_data, fields=['nitrogen', 'phosphorus', 'potassium', 'magnesium', 'calcium', 'sulfur',
                                        'boron', 'zinc', 'manganese', 'iron', 'copper', 'chloride'])
            keys_list = recent_dict.keys()
            values_list = recent_dict.values()
            sufficiency_dict = {'field': '', 'date': '', 'nitrogen': '', 'phosphorus': '', 'potassium': '', 'magnesium': '', 
                                'calcium': '', 'sulfur': '', 'boron': '', 'zinc': '', 'manganese': '', 'iron': '', 
                                'copper': '', 'chloride': ''}
            sufficiency_dict['field'] = recent_data.field_name
            sufficiency_dict['date'] = recent_data.date
            i = 0
            while i < len(keys_list):
                ranges = leafSufficiency.objects.get(element=keys_list[i])
                if values_list[i] == "":
                    i += 1
                    continue
                current_level = float(values_list[i])
                deficient_level = float(ranges.deficient)
                low_level = float(ranges.low)
                optimum_level = float(ranges.optimum)
                high_level = float(ranges.high)
                excess_level = float(ranges.excess)
                if current_level < deficient_level:
                    index = 20 * (current_level / deficient_level)
                elif current_level < low_level:
                    index = 20 + 20 * ((current_level - deficient_level) / (low_level - deficient_level))
                elif current_level < optimum_level:
                    index = 40 + 20 * ((current_level - low_level) / (optimum_level - low_level))
                elif current_level < high_level:
                    index = 60 + 20 * ((current_level - optimum_level) / (high_level - optimum_level))
                elif current_level < excess_level:
                    index = 80 + 20 * ((current_level - high_level) / (excess_level - high_level))
                else:
                    index = 100
                sufficiency_dict[keys_list[i]] = index
                i += 1
            message = "hi"
            return JsonResponse(sufficiency_dict, safe=False)
        
        if flag == 'comparison':
            selected_fields = request.POST.getlist('comFieldList[]')
            com_date = (request.POST.get('comDate'))
            com_date = datetime.datetime.strptime(com_date, '%B %Y').strftime('%Y-%m-%d')
            time_delta = datetime.timedelta(days=30)
            com_date_end = datetime.datetime.strptime(com_date, '%Y-%m-%d') + time_delta
            comparison_data = {}
            print(selected_fields)
            print(com_date)
            
            for field in selected_fields:
                # Numerical analysis of leaf content for sufficiency range
                recent_data = leafSamples.objects.filter(field_name=field).filter(
                        date__range=[com_date, com_date_end]).latest('id')
                recent_dict = model_to_dict(recent_data, fields=['nitrogen', 'phosphorus', 'potassium', 'magnesium', 'calcium', 'sulfur',
                                            'boron', 'zinc', 'manganese', 'iron', 'copper', 'chloride'])
                keys_list = recent_dict.keys()
                values_list = recent_dict.values()
                comparison_dict = {'field': '', 'date': '', 'nitrogen': '', 'phosphorus': '', 'potassium': '', 'magnesium': '', 
                                    'calcium': '', 'sulfur': '', 'boron': '', 'zinc': '', 'manganese': '', 'iron': '', 
                                    'copper': '', 'chloride': ''}
                comparison_dict['field'] = recent_data.field_name
                comparison_dict['date'] = recent_data.date
                i = 0
                while i < len(keys_list):
                    ranges = leafSufficiency.objects.get(element=keys_list[i])
                    if values_list[i] == "":
                        i += 1
                        continue
                    current_level = float(values_list[i])
                    deficient_level = float(ranges.deficient)
                    low_level = float(ranges.low)
                    optimum_level = float(ranges.optimum)
                    high_level = float(ranges.high)
                    excess_level = float(ranges.excess)
                    if current_level < deficient_level:
                        index = 20 * (current_level / deficient_level)
                    elif current_level < low_level:
                        index = 20 + 20 * ((current_level - deficient_level) / (low_level - deficient_level))
                    elif current_level < optimum_level:
                        index = 40 + 20 * ((current_level - low_level) / (optimum_level - low_level))
                    elif current_level < high_level:
                        index = 60 + 20 * ((current_level - optimum_level) / (high_level - optimum_level))
                    elif current_level < excess_level:
                        index = 80 + 20 * ((current_level - high_level) / (excess_level - high_level))
                    else:
                        index = 100
                    comparison_dict[keys_list[i]] = index
                    i += 1
                comparison_data[field] = comparison_dict
            print(comparison_data) 
            #comparison_data_json = serializers.serialize('json', [comparison_data])
            
            
            message = "hi"
            return JsonResponse(comparison_data, safe=False)
    
            
         
    # First query the leaf sample data for the default graphs: all data from most recent sample for the DRIS 
    # and bar graph, and the last year of nitrogen data for the line graph
    fields_distinct = leafSamples.objects.values_list("field_name", flat=True).distinct()
    recent_data = leafSamples.objects.filter(field_name=str(fields_distinct[0])).latest('id')
    today = datetime.date.today()
    today_str = datetime.datetime.strptime(str(today), "%Y-%m-%d")
    time_delta = datetime.timedelta(days=365)
    last_year = today - time_delta
    element_year = leafSamples.objects.order_by("date").values_list("field_name", "date", "nitrogen").distinct()
    fields_distinct = leafSamples.objects.order_by("field_name").values_list("field_name", flat=True).distinct()
    elements_distinct = ('nitrogen', 'phosphorus', 'potassium', 'magnesium', 'calcium', 'sulfur',
                 'boron', 'zinc', 'manganese', 'iron', 'copper', 'chloride')
    recent_data_json = serializers.serialize('json', [recent_data])
    element_year_json = json.dumps(list(element_year), cls=DjangoJSONEncoder)
    elements_json = json.dumps(list(elements_distinct), cls=DjangoJSONEncoder)
    
    # Numerical analysis of leaf content for sufficiency range
    recent_dict = model_to_dict(recent_data, fields=['nitrogen', 'phosphorus', 'potassium', 'magnesium', 'calcium', 'sulfur',
                                'boron', 'zinc', 'manganese', 'iron', 'copper', 'chloride'])
    keys_list = recent_dict.keys()
    values_list = recent_dict.values()
    sufficiency_dict = {'field': '', 'date': '', 'nitrogen': '', 'phosphorus': '', 'potassium': '', 'magnesium': '', 
                        'calcium': '', 'sulfur': '', 'boron': '', 'zinc': '', 'manganese': '', 'iron': '', 
                        'copper': '', 'chloride': ''}
    sufficiency_dict['field'] = recent_data.field_name
    sufficiency_dict['date'] = recent_data.date
    i = 0
    while i < len(keys_list):
        ranges = leafSufficiency.objects.get(element=keys_list[i])
        if values_list[i] == "":
            i += 1
            continue
        current_level = float(values_list[i])
        deficient_level = float(ranges.deficient)
        low_level = float(ranges.low)
        optimum_level = float(ranges.optimum)
        high_level = float(ranges.high)
        excess_level = float(ranges.excess)
        if current_level < deficient_level:
            index = 20 * (current_level / deficient_level)
        elif current_level < low_level:
            index = 20 + 20 * ((current_level - deficient_level) / (low_level - deficient_level))
        elif current_level < optimum_level:
            index = 40 + 20 * ((current_level - low_level) / (optimum_level - low_level))
        elif current_level < high_level:
            index = 60 + 20 * ((current_level - optimum_level) / (high_level - optimum_level))
        elif current_level < excess_level:
            index = 80 + 20 * ((current_level - high_level) / (excess_level - high_level))
        else:
            print("Error: " + str(current_level) + " " + str(keys_list[i]))
            index = 100
        sufficiency_dict[keys_list[i]] = index
        i += 1
        
    form_class = leafForm
    form = form_class
    
    return render(request, 'leaf_report.html', { 
        'form': form,
        'fields_distinct': fields_distinct,
        'elements_distinct': elements_distinct,
        'recent_data': recent_data,
        'recent_data_json': recent_data_json,
        'element_year_json': element_year_json,
        'sufficiency_dict': sufficiency_dict
    })
    
