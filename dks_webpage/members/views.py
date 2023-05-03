from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Member
from django.core.files import File
from django.shortcuts import redirect
import pyrebase
import datetime
import os
import json
import sys
print(sys.path[0])
with open(sys.path[0]+'/../../DataCollector/PrivateKey/data.json', 'r') as f:
    config = json.load(f)
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def statistics(request):
    AvgScore1 = database.child('RAT1').child('AvgScore').get().val()
    Rat1 = database.child('RAT1').get().val()
    CorrAnsPerQ1 = database.child('RAT1').child('CorrAnsPerQ').get().val()
    AvgScore2 = database.child('RAT2').child('AvgScore').get().val()
    Rat2 = database.child('RAT2').get().val()
    CorrAnsPerQ2 = database.child('RAT2').child('CorrAnsPerQ').get().val()
    AvgScore3 = database.child('RAT3').child('AvgScore').get().val()
    Rat3 = database.child('RAT3').get().val()
    CorrAnsPerQ3 = database.child('RAT3').child('CorrAnsPerQ').get().val()
    Participants1 = database.child('RAT1').child('TotPartecipants').get().val()
    Participants2 = database.child('RAT2').child('TotPartecipants').get().val()
    Participants3 = database.child('RAT3').child('TotPartecipants').get().val()
    Time1 = database.child('RAT1').child('AvgTime').get().val()
    Time2 = database.child('RAT2').child('AvgTime').get().val()
    Time3 = database.child('RAT3').child('AvgTime').get().val()
    
    Time1 = round(Time1/60)
    Time2 = round(Time2/60)
    Time3 = round(Time3/60)
    
    return render(request, "statistics.html",{"AvgScore1":AvgScore1,"RAT1":Rat1,"CorrAnsPerQ1":CorrAnsPerQ1, "Participants1":Participants1, "Time1":Time1,
                                               "AvgScore2":AvgScore2,"RAT2":Rat2,"CorrAnsPerQ2":CorrAnsPerQ2,"Participants2":Participants2, "Time2":Time2,
                                                "AvgScore3":AvgScore3,"RAT3":Rat3,"CorrAnsPerQ3":CorrAnsPerQ3, "Participants3":Participants3, "Time3":Time3})

def teachers(request):
  return render(request,'teachers.html')


def jaya(request):
  #template = loader.get_template('jaya.html')
  return render(request,'jaya.html')

def button_pushed(request):
  now = datetime.datetime.utcnow()+datetime.timedelta(hours=2)
  month = now.strftime("%m")
  day = now.strftime("%d")
  year = now.strftime("%Y")
  time = now.strftime("%X")
  timestamp = day +"/"+month+"/"+year + "-" + time
  prefix = "RAT1"
  with open('members/ratTimestamp.txt','r') as f:
    lines = f.readlines()
    f.close()
  index_line = None
  for i, line in enumerate(lines):
    if line.startswith(prefix):
      index_line = i
      break
  if index_line is not None:
    lines[index_line] = "RAT1 "+ timestamp + os.linesep
  else:
    lines.append("RAT1 "+ timestamp + os.linesep)
  with open('members/ratTimestamp.txt','w') as f:
    f.writelines(lines)
  return redirect('teachers')

def button_pushed2(request):
  now = datetime.datetime.utcnow()+datetime.timedelta(hours=2)
  month = now.strftime("%m")
  day = now.strftime("%d")
  year = now.strftime("%Y")
  time = now.strftime("%X")
  timestamp = day +"/"+month+"/"+year + "-" + time
  prefix = "RAT2"
  with open('members/ratTimestamp.txt','r') as f:
    lines = f.readlines()
    f.close()
  index_line = None
  for i, line in enumerate(lines):
    if line.startswith(prefix):
      index_line = i
      break
  if index_line is not None:
    lines[index_line] = "RAT2 "+ timestamp + os.linesep
  else:
    lines.append("RAT2 "+ timestamp + os.linesep)
  with open('members/ratTimestamp.txt','w') as f:
    f.writelines(lines)
  return redirect('teachers')

def button_pushed3(request):
  now = datetime.datetime.utcnow()+datetime.timedelta(hours=2)
  month = now.strftime("%m")
  day = now.strftime("%d")
  year = now.strftime("%Y")
  time = now.strftime("%X")
  timestamp = day +"/"+month+"/"+year + "-" + time
  prefix = "RAT3"
  with open('members/ratTimestamp.txt','r') as f:
    lines = f.readlines()
    f.close()
  index_line = None
  for i, line in enumerate(lines):
    if line.startswith(prefix):
      index_line = i
      break
  if index_line is not None:
    lines[index_line] = "RAT3 "+ timestamp + os.linesep
  else:
    lines.append("RAT3 "+ timestamp + os.linesep)
  with open('members/ratTimestamp.txt','w') as f:
    f.writelines(lines)
  return redirect('teachers')

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

def RATS(request):
  template = loader.get_template('RAT_link.html')
  return HttpResponse(template.render())

def RAT2(request):
  template = loader.get_template('RAT2.html')
  return HttpResponse(template.render())

def RAT3(request):
  template = loader.get_template('RAT3.html')
  return HttpResponse(template.render())

def ALL_RATS(request):
  template = loader.get_template('RAT_list.html')
  return HttpResponse(template.render())
