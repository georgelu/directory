#pip install tweepy
import json
import urllib2
import requests
import re
from datetime import datetime
from time import strftime
from datetime import timedelta
import calendar

response = urllib2.urlopen('https://api.myjson.com/bins/3dnjr')
data = json.load(response)

currenttime = datetime.now()

#find the date of the next weekday from now
#d = current time, weekday = 0-6 for monday through sunday
def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + timedelta(days_ahead)

#for each event, calculate the next date/time of the event
for item in data:
    next_day = item['daycode'] #day of the week of the event
    day_interval = item['interval'] #week of the month the event takes place, 5 means every week
    next_time = item['timecode'] #starting time of event in human readable format
    hourmin = datetime.strptime(next_time, "%I:%M %p") #next_time as a python object
    
    #find next date if event occurs every week
    if day_interval==5: 
        temp = next_weekday(currenttime,next_day) 
    #find next date if event occurs on a specific day of a specific week
    else: 
        temp = currenttime.replace(day=1)
        adj = (next_day - temp.weekday()) % 7
        temp += timedelta(days=adj)
        temp += timedelta(weeks=day_interval-1)

    next_event_time = temp.replace(hour=hourmin.hour,minute=hourmin.minute)
    item['next_event'] = str(next_event_time)

with open('directory.json', 'w') as outfile:
    json.dump(data, outfile)
