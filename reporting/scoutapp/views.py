from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from scoutapp.models import Field, LabelleData, labelleFieldOrder, scoutingAreas, sprayTrials
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView 
from collections import defaultdict
from django.shortcuts import get_object_or_404
import json, os
import datetime
from scoutapp.forms import fieldForm, labelleMatureNE, labelleMatureNW, labelleMatureSE, labelleMatureSW, labelleMatureC, sprayForm
from utils.scoutingReport import scoutingReport
from django.core.serializers.json import DjangoJSONEncoder
from reporting.tasks import add

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
    
