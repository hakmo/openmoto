
import bsp as openmoto_bsp      # bsp should point to the bsp file for your hw

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


# Function for reading test inputs from keyboard
def getTestInputs(events):
    print "Starting getTestInputs"
    while 1:
        key =  ord(msvcrt.getch())
        # Start (s)
        if openmoto_bsp.input_start(key):
            # toggle start event
            if events['start'].isSet():
               events['start'].clear()
            else :
                events['start'].set()
        # Light (l)
        if openmoto_bsp.input_light(key):
            # toggle start event
            if events['light'].isSet():
               events['light'].clear()
            else :
                events['light'].set()
        # Handle special keys (arrow, etc)
        if key == 224:
            key =  ord(msvcrt.getch())
            #print "Key2 is " + str(key)
            if openmoto_bsp.input_turnl(key):
                # toggle left turn event
                if events['leftturn'].isSet():
                    events['leftturn'].clear()
                else :
                    events['leftturn'].set()
            if openmoto_bsp.input_turnr(key):
                # toggle right turn event
                if events['rightturn'].isSet():
                    events['rightturn'].clear()
                else :
                    events['rightturn'].set()
            if openmoto_bsp.input_brake(key):
                # toggle brake event
                if events['brake'].isSet():
                    events['brake'].clear()
                else :
                    events['brake'].set()
    print "Exiting getTestInputs"

    
