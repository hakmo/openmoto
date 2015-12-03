
import bsp as openmoto_bsp

import msvcrt
import threading
import time

### Function for reading inputs
##def getInputs():
##    print "Starting getInputs"
##    while 1:
##        turnr_val = openmoto_bsp.input_turnr()
##        if turnr_val == 1:
##            # set right turn event
##        if turnr_val == 0:
##            # clear right turn event
##        start_val = openmoto_bsp.input_start()
##        if start_val == 1:
##            # set start event
##        if start_val == 0:
##            # clear start event
##        if openmoto_bsp.input_horn():
##            # set horn event
##        if openmoto_bsp.input_turnl():
##            # set left turn event
##        if openmoto_bsp.input_config():
##            # set config event
##        if openmoto_bsp.input_light():
##            # set light event
##        if openmoto_bsp.input_brake():
##            # set brake event
##        if openmoto_bsp.input_lock():
##            # set lock event
##    print "Exiting getInputs"


# Function for reading test inputs
def getTestInputs(events):
    print "Starting getTestInputs"
    while 1:
        key =  msvcrt.getch()
        if key == 'a':
            print "Got a"
            # toggle left turn event
            if events['leftturn'].isSet():
                events['leftturn'].clear()
            else :
                events['leftturn'].set()
        elif key == 'd':
            print "Got d"
            # toggle right turn event
            if events['rightturn'].isSet():
                events['rightturn'].clear()
            else :
                events['rightturn'].set()
    print "Exiting getTestInputs"

    
