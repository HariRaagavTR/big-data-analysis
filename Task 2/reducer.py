#!/usr/bin/env python3
import sys

current_state = ''
current_city = ''
city_total = 0
state_total = 0

backup_list = []

# Combining Mapper Outputs
for line in sys.stdin:
    state, city, n_accidents = line.strip().split(',')
    
    if state != current_state:
        if current_state != '':
            print('%s %d' % (current_city, city_total))
            while backup_list:
                backup_city, backup_count = backup_list.pop()
                print('%s %d' % (backup_city, backup_count))
            print('%s %d' % (current_state, state_total))
        current_state = state
        print('%s' % current_state)
        state_total = 0
    
    if city != current_city:
        if state_total != 0:
            if (current_city in city) and (city[city.find(current_city) + len(current_city)] == ' '):
                backup_list.append((current_city, city_total))
            else:
                print('%s %d' % (current_city, city_total))
                while backup_list:
                    if (backup_list[-1][0] in city) and (city[city.find(backup_list[-1][0]) + len(backup_list[-1][0])] == ' '):
                        break                        
                    else:
                        backup_city, backup_count = backup_list.pop()
                        print('%s %d' % (backup_city, backup_count))
        current_city = city
        city_total = 0

    city_total += int(n_accidents)
    state_total += int(n_accidents)

# Post-Loop Outputs
if state_total:
    print('%s %d' % (current_city, city_total))
    print('%s %d' % (current_state, state_total))