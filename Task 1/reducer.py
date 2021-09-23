#!/usr/bin/env python3
import sys

current_hour = ''
hour_total = 0

# Combining Mapper Outputs
for line in sys.stdin:
    key, n_accidents = line.strip().split(',')
    hour = ord(key) - ord('a')
    
    if hour != current_hour:
        if current_hour != '':
            print('%s %d' % (current_hour, hour_total))
        hour_total = 0
        current_hour = hour
    
    hour_total += int(n_accidents)

# Post-Loop Outputs
if hour_total:
    print('%s %d' % (current_hour, hour_total))
