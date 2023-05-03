"""
Project: DataCollector

How to run the code: python3 DataCollector.py <RAT_name> <startTime>
where
- <RAT_name> can be RAT1, RAT2, etc...
- <startTime> is the starting time of the RAT session (format: dd/mm/yyyy-HH:MM:SS)

In case you want to add more RAT files, remember to update RAT_list!

Two directories must be made at the same position: RATs/ and Solutions/. 
- RATs/ : .csv files with RAT answers from students;
- Solutions/ : .csv files with RAT solutions.

Each .csv file must be named RAT#, where # is the number of the RAT.
"""

import sys
import pandas as pd
import os
import numpy as np
import csv
import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from IPython.display import display

from datetime import datetime


RAT_name = sys.argv[1]
startTime = sys.argv[2]
start_time = datetime.strptime(startTime, '%d/%m/%Y-%H:%M:%S')

###################################### CSV ###################################################################

RAT_list = ['RAT1', 'RAT2', 'RAT3'] # list of all RATs (must be updated in case of more RATs)

if RAT_name in RAT_list:
    print(f"----> {RAT_name} is chosen!")
else:
    sys.exit(f"***ERROR***: the RAT file is not correct.")

RATs_dir_path = os.path.abspath(sys.path[0]+'/RATs') # directory with RATs results from students
RATSol_dir_path = os.path.abspath(sys.path[0]+'/Solutions') # directory with RATs correct answers
StatJSON = os.path.abspath(sys.path[0]+'/StatJSON') # directory with statistics from RATs     

# Find all files under the two directories 
filenames_RATs = os.listdir(RATs_dir_path)
filenames_RATSol = os.listdir(RATSol_dir_path)

RAT_results = {}
RAT_solutions = {}

only_questions_RATs = []
only_questions_RATSol = []
timeStamp = []

for filename in filenames_RATs:
    if RAT_name in filename:
        RAT_results[filename] = pd.read_csv(RATs_dir_path + "/" + filename)
        column_names = list(RAT_results[filename].columns.values)
        only_questions_RATs.append(column_names[2:])

if not(RAT_results):
    sys.exit(f"***ERROR***: file {RAT_name} not found under {RATs_dir_path}!")

for filename in filenames_RATSol:
    if RAT_name in filename:
        RAT_solutions[filename] = pd.read_csv(RATSol_dir_path + "/" + filename)
        only_questions_RATSol.append(list(RAT_solutions[filename].columns.values))

if not(RAT_solutions):
    sys.exit(f"***ERROR***: file {RAT_name} not found under {RATSol_dir_path}!")

# comparing quesions in RAT solutions and RAT results
if only_questions_RATs == only_questions_RATSol:
    print(f"----> Questions are the same in {RATs_dir_path}\\{RAT_name}.csv and {RATSol_dir_path}\\{RAT_name}.csv")
else :
    sys.exit(f"***ERROR***: Questions are NOT the same in {RATs_dir_path}\\{RAT_name}.csv and {RATSol_dir_path}\\{RAT_name}.csv")

# create dictionary with corrections
RAT_answers = {}
RAT_times = {}
answer_list = []

dict_with_solutions = RAT_solutions[RAT_name+'.csv']
dict_with_results = RAT_results[RAT_name+'.csv']

email_list = dict_with_results.loc[:,'Email Address']
timeStamp = list(dict_with_results.loc[:,'Timestamp'])
time_in_seconds = [(datetime.strptime(t, '%d/%m/%Y %H.%M.%S') - start_time).total_seconds() for t in timeStamp]
dict_with_results.drop(['Timestamp','Email Address'], axis=1, inplace=True)
solutions = dict_with_solutions.iloc[0].values

i = 0
for email in email_list:
   answers = dict_with_results.iloc[i].values
   correction_list = [int(answers[i] == solutions[i]) for i in range(len(answers))]
   RAT_answers[email] = correction_list # 1: correct answ; 0: otherwise
   RAT_times[email] = time_in_seconds[i]
   i = i + 1

################################### STATISTICS ###############################################################

# Compute number of partecipants
partecipants=(len(RAT_answers))

vals=list(RAT_answers.values())
mean_grade=round((np.sum(vals)/partecipants)/len(vals[0])*100, 2)

# Compute score average
mVals=np.mean(vals, axis=0)
answs=[]
for val in range(len(mVals)):
    answs.append(round(mVals[val]*100, 2))

# Compute average time spent to do a RAT
# (median is used to avoid considering RAT results with very high elapsed time)
avg_time=np.median(time_in_seconds)

# Create JSON variable with the statistics
json_out = {"AvgScore": mean_grade,
            "AvgTime": avg_time,
            "CorrAnsPerQ": answs,
            "TotPartecipants": partecipants}

# Write JSON to file under StatJSON forlder
out_file = open(StatJSON + "/" + RAT_name+".json", "w")
json.dump({RAT_name:json_out}, out_file, indent = 6)
out_file.close()

#################################### FIREBASE ################################################################

# Fetch the service account key JSON file contents
databaseURL = 'https://ttm4115-webpage-default-rtdb.europe-west1.firebasedatabase.app/'

# Check private key to access the Firebase database
cred_obj = firebase_admin.credentials.Certificate(sys.path[0]+'/PrivateKey/ttm4115_firebase.json')
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL':databaseURL})

# Get a database reference to the name of the RAT in the database
ref = db.reference('/' + RAT_name)

# Write data on the database
ref.set(json_out)
