# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:30:50 2022

@author: aelbadra
"""

#Define All States (also represents actions):
states = {"Start", "Stop", "Slow Down", "Forward", "Stop-End Trip", 'Just-Turned', 'Turning'}

#Define Different Input Percepts and their values
light = {'red':0, 'green':0, 'yellow':0}
dist_to_light = {'near':0, 'far':0}
destination_reached = {'y':0, 'n':0}
front_car = {'near':0, 'far':0, 'stopped':0}
object_detected = {'y':0, 'n':0}
turn_direction = {'left':0, 'right':0, 'u-turn':0, 'straight':0}

#set initial state
state = 'Start'
print('Initial State = ', state)

#start driving!
while True:
    #read input percept:
    l=0;dtl=0;dst=0;fc=0;o=0;inter=0;turn=0
    if (state == 'Turning'):
        while o not in object_detected:
            o = input("Enter Object Detected (y,n): ")
    else:
        while o not in object_detected:
            o = input("Enter Object Detected (y,n): ")
        while l not in light:
            l = input("Enter Light (red, green, yellow): ")
        while dtl not in dist_to_light:
            dtl = input("Enter Distance to Light (near, far): ")
        while dst not in destination_reached:
            dst = input("Enter Destination Reached? (y, n): ")
        while fc not in front_car:
            fc = input("Enter Front Car Status (near, far, stopped): ")
        while turn not in turn_direction:
            turn = input("Enter turn direction (left, right, u-turn, straight): ")     
    
    #========================
    print("==================================")
    if state == 'Start':
        if l =='red' or l=='yellow' or o=='y':
            state = 'Stop'
            print("state changed to:", state)
            continue
        elif l == 'green':
            state = 'Slow Down'
            print("state changed to:", state)
            continue
        else:
            print('State did not change: ', state)
    #========================
    elif state == 'Stop':
        if dst == 'y':
            state = 'Stop-End Trip'
            print("state changed to:", state)
            print('Trip ended!')
            break
        elif l=='green' and fc=='far' and dst=='n':
            state = 'Slow Down'
            print("state changed to:", state)
            continue
        else:
            print('State did not change: ', state)
    #========================
    elif state == 'Slow Down':
        if dst == 'y':
            state = 'Stop-End Trip'
            print("state changed to:", state)
            print('Trip ended!')
            break #end the trip!
        elif l=='green' and fc=='far' and dst=='n' and turn=='straight':
            state = 'Forward'
            print("state changed to:", state)
            continue
        elif l=='green' and fc=='far' and dst=='n' and turn!='straight':
            state = 'Turning'
            print("state changed to:", state)
            continue
        elif l=='red' or l=='yellow' or fc=='stopped' or o=='y':
            state = 'Stop'
            print("state changed to:", state)
            continue
        else:
            print('State did not change: ', state)
    #========================
    elif state == 'Forward':
        if dst == 'y':
            state = 'Stop-End Trip'
            print("state changed to:", state)
            print('Trip ended!')
            break #end the trip!
        elif (l=='red') or (l=='yellow' and dtl=='far') or o=='y':
            state = 'Stop'
            print("state changed to:", state)
            continue
        elif fc == 'near' or (turn!='straight' and dtl=='near'):
            state = 'Slow Down'
            print("state changed to:", state)
            continue
        else:
            print('State did not change: ', state)
    #========================
    elif state == 'Turning':
        if  o=='y':
            state = 'Stop'
            print("state changed to:", state)
            continue
        else:
           state = 'Just-Turned'
           print("state changed to:", state)
    #========================
    elif state == 'Just-Turned':
        if dst == 'y':
            state = 'Stop-End Trip'
            print("state changed to:", state)
            print('Trip ended!')
            break #end the trip!
        elif (l=='red' and dtl=='near') or (l=='yellow' and dtl=='far') or o=='y':
            state = 'Stop'
            print("state changed to:", state)
            continue
        elif fc == 'near':
            state = 'Slow Down'
            print("state changed to:", state)
            continue
        elif l=='green' and fc=='far' and dst=='n':
            state = 'Forward'
            print("state changed to:", state)
            continue
        elif l=='green' and fc=='far' and dtl=='near':
            state = 'Slow Down'
            print("state changed to:", state)
            continue
        else:
            print('State did not change: ', state)
    #========================
    elif state == 'Stop-End Trip':
        print('Destination Reached! Trip Ended!')
        break
    #========================
    else:
        print("ERROR: Unknown State!!!")
        break