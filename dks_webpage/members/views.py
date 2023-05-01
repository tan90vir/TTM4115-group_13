from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Member
import pyrebase
 
config = {
    "apiKey": "AIzaSyDQu7yTewKm4KPvW-ZDbajKY35gsKqbARE",
    "authDomain": "ttm4115-webpage.firebaseapp.com",
    "projectId": "ttm4115-webpage",
    "storageBucket": "ttm4115-webpage.appspot.com",
    "messagingSenderId": "212572809356",
    "appId": "1:212572809356:web:482bdbce8e8e16d1b973a9",
    "measurementId": "G-XC0DTG2Q5M",
    "databaseURL": "https://ttm4115-webpage-default-rtdb.europe-west1.firebasedatabase.app/"
  }
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def statistics(request):
    day = database.child('Data').child('Days').get().val()
    id = database.child('Data').child('Id').get().val()
    projectname = database.child('Data').child('Projectname').get().val()
    context = {
      'day' : day,
    }
    return render(request,"statistics.html",{"day":day,"id":id,"projectname":projectname })


def jaya(request):
  #template = loader.get_template('jaya.html')
  return render(request,'jaya.html')

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