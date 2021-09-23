#!/usr/bin/env python3
import sys
import json
from datetime import datetime

for line in sys.stdin:
    record = json.loads(line)
    try:
        cond_1 = any(_p in record['Description'].lower() for _p in ['lane blocked', 'shoulder blocked', 'overturned vehicle'])
        cond_2 = record['Severity'] >= 2
        cond_3 = record['Sunrise_Sunset'].lower() == 'night'
        cond_4 = record['Visibility(mi)'] <= 10
        cond_5 = record['Precipitation(in)'] >= 0.2
        cond_6 = record['Weather_Condition'].lower() in ['heavy snow', 'thunderstorm', 'heavy rain', 'heavy rain showers', 'blowing dust']
    except:
        continue
    if cond_1 and cond_2 and cond_3 and cond_4 and cond_5 and cond_6:
        try:
            hour = datetime.strptime(record['Start_Time'].split(':')[0], '%Y-%m-%d %H').hour
            print('%s,1' % (chr(ord('a') + hour)))
        except:
            pass