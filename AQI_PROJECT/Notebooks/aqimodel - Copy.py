# -*- coding: utf-8 -*-
"""AqiModel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sPm_nj4b_sitnrYc3QkVFsfwQEJiGuGO
"""

#Read dataset
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import pandas as pd
data=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQVX8PUwUbmiCnYVkPH8sm9e5qiBS6tW0xqYcmV5lSElg2UaJu-e1LPLNOcfnKnGZrEL4xP-rSbSgFr/pub?output=csv")

datam=data[data['Location']=='Navi Mumbai']
datah=data[data['Location']=='Hyderabad']
datad=data[data['Location']=='Delhi']
datab=data[data['Location']=='Bhubaneshwar']
datav=data[data['Location']=='Visakhapatnam']
independent_variables=['Year','Month']

from sklearn.ensemble import RandomForestRegressor
clf = RandomForestRegressor(n_estimators=100,
    random_state=1337,
    max_depth=15,
    min_samples_leaf=1,
    verbose=2)

def fit_m(u):
  ind_var=['Year','Month']
  X=datam[ind_var]
  Y1=datam['so2']
  Y2=datam['no2']
  clf.fit(X,Y1)
  so2=clf.predict(u)
  clf.fit(X,Y2)
  no2=clf.predict(u)
  return so2,no2
           
def fit_h(u):
  ind_var=['Year','Month']
  X=datah[ind_var]
  Y1=datah['so2']
  Y2=datah['no2']
  clf.fit(X,Y1)
  so2=clf.predict(u)
  clf.fit(X,Y2)
  no2=clf.predict(u)
  return so2,no2

def fit_b(u):
  ind_var=['Year','Month']
  X=datab[ind_var]
  Y1=datab['so2']
  Y2=datab['no2']
  clf.fit(X,Y1)
  so2=clf.predict(u)
  clf.fit(X,Y2)
  no2=clf.predict(u)
  return so2,no2

def fit_d(u):
  ind_var=['Year','Month']
  X=datad[ind_var]
  Y1=datad['so2']
  Y2=datad['no2']
  clf.fit(X,Y1)
  so2=clf.predict(u)
  clf.fit(X,Y2)
  no2=clf.predict(u)
  return so2,no2

def fit_v(u):
  ind_var=['Year','Month']
  X=datav[ind_var]
  Y1=datav['so2']
  Y2=datav['no2']
  clf.fit(X,Y1)
  so2=clf.predict(u)
  clf.fit(X,Y2)
  no2=clf.predict(u)
  return so2,no2

def pred_m(so2,no2):
  ind_var=['so2','no2']
  input_df=pd.DataFrame({"so2":so2,"no2":no2},index=[0])
  train_X=datam[ind_var]
  train_Y=datam['so2']
  clf.fit(train_X,train_Y)
  Pred_spm=clf.predict(input_df)
  return Pred_spm
  
def pred_d(so2,no2):
  ind_var=['so2','no2']
  input_df=pd.DataFrame({"so2":so2,"no2":no2},index=[0])
  train_X=datad[ind_var]
  train_Y=datad['so2']
  clf.fit(train_X,train_Y)
  Pred_spm=clf.predict(input_df)
  return Pred_spm
  
def pred_b(so2,no2):
  ind_var=['so2','no2']
  input_df=pd.DataFrame({"so2":so2,"no2":no2},index=[0])
  train_X=datab[ind_var]
  train_Y=datab['so2']
  clf.fit(train_X,train_Y)
  Pred_spm=clf.predict(input_df)
  return Pred_spm
  
def pred_h(so2,no2):
  ind_var=['so2','no2']
  input_df=pd.DataFrame({"so2":so2,"no2":no2},index=[0])
  train_X=datah[ind_var]
  train_Y=datah['so2']
  clf.fit(train_X,train_Y)
  Pred_spm=clf.predict(input_df)
  return Pred_spm
  
def pred_v(so2,no2):
  ind_var=['so2','no2']
  input_df=pd.DataFrame({"so2":so2,"no2":no2},index=[0])
  train_X=datav[ind_var]
  train_Y=datav['so2']
  clf.fit(train_X,train_Y)
  Pred_spm=clf.predict(input_df)
  return Pred_spm

user_inp={}
loc=input("Enter Location : ")
dat=input("Enter Date : ")
aa=dat.split("/")
#for feature in independent_variables:
#temp=input("Enter "+feature+" : ")
user_inp['Month']=int(aa[1],10)
user_inp['Year']=int(aa[2],10)
user_inp_df=pd.DataFrame(data=user_inp , index=[0],columns=independent_variables)

s=str.strip(str.title(loc))
if s == 'Hyderabad':
  so2,no2=fit_h(user_inp_df)
  aqi=pred_h(so2,no2)
elif s == 'Delhi':
  so2,no2=fit_d(user_inp_df)
  aqi=pred_d(so2,no2)
elif s == 'Mumbai':
  so2,no2=fit_m(user_inp_df)
  aqi=pred_m(so2,no2)
elif s == 'Visakhapatnam':
  so2,no2=fit_v(user_inp_df)
  aqi=pred_b(so2,no2)
elif s == 'Bhubaneshwar':
  so2,no2=fit_b(user_inp_df)
  aqi=pred_b(so2,no2)
else:
  print("Entered city is not currently in our DataBase")
 
#print(aqi)

if(aqi>=1 and aqi<=2):
  print("Air Pollution Category \"Excellent\" Air Quality Index %d no health issues"%aqi)

elif(aqi>2 and aqi<=5):
  print("Air Pollution Category \"GOOD\" Air Quality Index %d slight effect to only some Hypersensitive Individuals"%aqi)
  
elif(aqi>5 and aqi<=7):
  print("Air Pollution Category \"LIGHTLY POLLUTED\" Air Quality Index %d Healthy people may feel slight irritation"%aqi)
    
elif(aqi>7 and aqi<=10):
  print("Air Pollution Category \"HEAVILY POLLUTED\" Air Quality Index %d healthy people will show symptoms to heart and Respiratory Diseases"%aqi)
  

elif(aqi>=11 ):
  print("Air Pollution Category \"SEVERELY POLLUTED\" Air Quality Index %d Healthy people will experience reduced endurance in activities and may also show noticeably strong symptoms.\n Other illnesses may be triggered in healthy people.\n Elders and the sick should remain indoors and avoid exercise.\n Healthy individuals should avoid outdoor activities."%aqi)