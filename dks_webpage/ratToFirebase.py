#importing csv and json libraries
import csv
import json
import firebase_admin
import sys
from firebase_admin import credentials
from firebase_admin import firestore
filename=sys.argv[1]

#read the csv file
with open(filename+'.csv') as rat_csv_file:
    data = csv.DictReader(rat_csv_file)
    rat_csv_data = list(data)


cred = credentials.Certificate('ttm4115-webpage-90055da9bc92.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

data = rat_csv_data[0]

db.collection('RATs').document(filename).set(data)
