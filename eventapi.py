#pip install tweepy
import json
import urllib2
import requests
import re
import datetime
from datetime import timedelta
import calendar

response = urllib2.urlopen('https://api.myjson.com/bins/3dnjr')
data = json.load(response)

eventbatch = {}
currenttime = datetime.datetime.now()

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

for item in data:
    next_day = item['daycode']
    day_interval = item['interval']
    next_time = item['timecode'].strftime('%I:%M')    
    print next_day, day_interval
    
    #only calculate next events for current month/year
    year = currenttime.year
    month = currenttime.month
    
    if day_interval==5:
        temp = next_weekday(currenttime,next_day) 
    else:
        temp = currenttime.replace(day=1)
        adj = (next_day - temp.weekday()) % 7
        temp += timedelta(days=adj)
        temp += timedelta(weeks=day_interval-1)

    temp = temp.replace(next_time)
    print next_time
    print temp
    
   # monthcal = c.monthdatescalendar(year,month)
   # third_friday = [day for week in monthcal for day in week if day.weekday() == calendar.FRIDAY and day.month == month][3]
   # print third_friday

print json.dumps(eventbatch)


"""
tweet_str = decoded['text'].encode('ascii', 'ignore')
tweet_time = decoded['created_at']
tweet_profpic = decoded['user']['profile_image_url']
tweet_score = random.randint(0,5)
tweet_category = self.show_in_text(tweet_str)

jsonified = {}

jsonified['text'] = tweet_str
jsonified['id'] = tweet_category
jsonified['score'] = tweet_score
jsonified['time'] = tweet_time
jsonified['profpic'] = tweet_profpic
"""
