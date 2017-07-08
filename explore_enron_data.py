#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

ct=0
ans=0
ans1=0
ans2=0
ct2=0
for person_name in enron_data:
	if enron_data[person_name]["poi"]==1:
		ct=ct+1
	if enron_data[person_name]["salary"]!="NaN":
		ans=ans+1
	if enron_data[person_name]["total_payments"]=="NaN":
		ans1=ans1+1
	if enron_data[person_name]["poi"]==1:	
		if enron_data[person_name]["total_payments"]=="NaN":
			ans2=ans2+1
	ct2=ct2+1			

print ct
print ans
print ans1
print ans2
print ct2
print len(enron_data)
print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]		
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["FASTOW ANDREW"]["total_payments"]
print enron_data["LAY KENNETH"]	
