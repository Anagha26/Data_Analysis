# Python Notebook - Clone of Python Tutorial - Lessons 3, 4, 5, & 6

datasets[0].head(n=5)


city_population = {
  'Tokyo': 13350000, # a key-value pair
  'Los Angeles': 18550000,
  'New York City': 8400000,
  'San Francisco': 1837442
}

city_population.keys()

type(city_population.keys())

city_population.values()

type(city_population.values())

city_population["New York City"] 
## in dictionaries, values are accessed using key

### adding another key value pair to existing
### changing the existing value

city_population["New York City"]=123456

print city_population["New York City"] ## value changed

city_population["Miami"]=9878
print city_population

municipalities = {
    'New York City': [
        'Manhattan',
        'The Bronx',
        'Brooklyn',
        'Queens',
        'Staten Island'
    ],
    'Tokyo': [
        'Akihabara', 
        'Harajuku', 
        'Shimokitazawa', 
        'Nakameguro', 
        'Shibuya', 
        'Ebisu/Daikanyama', 
        'Shibuya District', 
        'Aoyama', 
        'Asakusa/Ueno', 
        'Bunkyo District', 
        'Ginza', 
        'Ikebukuro', 
        'Koto District', 
        'Meguro District', 
        'Minato District', 
        'Roppongi', 
        'Shinagawa District', 
        'Shinjuku', 
        'Shinjuku District', 
        'Sumida District', 
        'Tsukiji', 
        'Tsukishima']
}

print type(municipalities)
print type(municipalities['Tokyo'])
print type(municipalities['Tokyo'][0])

##municipalities is a dictionary, 
##municipalities['Tokyo'] is a list,
##and municipalities['Tokyo'][0] is a string.

print len(municipalities["Tokyo"])


print municipalities["Tokyo"]

## to retrieve list you can enter the key followed by the index
print municipalities["Tokyo"][4]

cities=["Tokyo","Los Angeles","New York","San Francisco"]

print cities

cities[1]

import numpy as np


city_population

population_values=city_population.values()

population_values

np.mean(population_values)

datasets[0].head(n=1)

import pandas as pd


data=datasets[0]

data.head(2)

data=data.fillna('') #replace missing values with empty strings:

data.head(2)

data.get_dtype_counts()

data.info()

cities[0]

city_population["Tokyo"]

data["url"]

data[:3] ## first three rows

data[4:7] ## last 4 to 6th rows

data[4997:] # from 4997 onwards

data.loc[1] ## selecting specific row from data

data["title"][:3] ## selecting no of rows from specific column



import pandas as pd

data.head()

data.title.value_counts()[:20] #20 most viewed pages

## Bar Charts
import matplotlib.pyplot as mpt
import matplotlib as mp

data["title"].value_counts()[:20].plot(kind="barh")

data["title"]=='Watsi | Fund medical treatments for people around the world'

newdataframe_index=data["title"]=='Watsi | Fund medical treatments for people around the world'

newdataframe_index



watsi_homepage=data[newdataframe_index]
watsi_homepage.head()  ##FILTERING data with new index

watsi_homepage["referrer"].value_counts()[:20]

watsi_homepage["referrer_domain"].value_counts()[:10]

medical_index=data["referrer"].str.contains("medical", case=False)

medical_referrals=data[medical_index]
medical_referrals


medical_referrals["referrer"].tolist()

data["platform"].value_counts()

data["New Column"]=2 ## new column with value 2

data.head(2)

data["New Column"]=
"Overwritten" ## overwiritng column from value '2' to 'overwriiten'
data.head(2)

mobile = ['iPhone', 'Android', 'iPad', 'Opera Mini', 'IEMobile', 'BlackBerry']

print 'iPad' in mobile
print 'jeep' in mobile
print 'Opera Mini' in mobile

if "Opera Mini" in mobile:
  print "GREAT SUCCESS" #if for true statement prints value

if "The marriage" in mobile:
  print "oh no"   # if for false statement prints nothing

if "The marriage" in mobile:
  print "oh no" 
else:
    print "its not there"
  # ifelse

operas = ['The Marriage of Figaro', 'The Magic Flute', 'La traviata']

if "The Marriage of Figaro" in operas:
  print "yes"
elif "The Marriage of dfdf" in operas:
  print "yes or dfdf"
else:
  print "No"

def function_to_check(a):
  if a in mobile:
    print "yes it is"
  else:
    print "no"
function_to_check("tikka")

## functions practice

## dynamic value by variable 'argu'
def functionx(argu):
  if argu+10>15:
   print "yes"
  else: 
    print"No"
  
functionx(13)  

## functions practice
def functionx():
  if 10+2>15:
   print "yes"
  else: 
    print"No"
functionx()
  



mobile

def addition(abc):
  if abc+10>15:
    print "this values is greater"
  else:
    print "this is small value"
addition(0.5)

mobile

def newfunction(abc):
  if abc in mobile:
    print "its in mobile"
  else:
    print " :( "

newfunction("iPad")

#apply

def newfunction(abc):
  if abc in mobile:
    return "Mobile"
  elif abc=="Desktop":
    return "Desktop"
  else:
    return " :( "

data["platform"].apply(newfunction)

data["Platform Type"]=data["platform"].apply(newfunction)

data.head()

data[["platform", "Platform Type"]]

# Simple plot 
### .plot(kind="bar") OR
### .plot(kind="barh")

data["platform"].value_counts().plot(kind='bar')

data[["Platform Type", "platform"]].head()

data["Platform Type"].value_counts().plot(kind="bar")

data[["Platform Type", "platform"]][15:20]



