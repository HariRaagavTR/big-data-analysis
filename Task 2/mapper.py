#!/usr/bin/env python3

import requests
import math
import sys
import json

def euclidian_dist(start_lat, start_long, end_lat, end_long):
    t1 = math.pow(start_lat - end_lat, 2)
    t2 = math.pow(start_long - end_long, 2)
    return math.sqrt(t1 + t2)

start_lat = float(sys.argv[1])
start_long = float(sys.argv[2])
dist_lim = float(sys.argv[3])

for line in sys.stdin:
    record = json.loads(line)
    
    curr_lat = float(record['Start_Lat'])
    curr_long = float(record.get('Start_Lng'))
    
    try:
        if(euclidian_dist(start_lat, start_long, curr_lat, curr_long) <= dist_lim):
            response = requests.post(url = "http://20.185.44.219:5000", json = {
                'latitude': curr_lat, 
                'longitude': curr_long
                }).json()
            print('%s,%s,%s' % (response['state'], response['city'], '1'))
    except:
        pass