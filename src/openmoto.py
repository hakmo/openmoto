#!/usr/bin/python

import bsp as openmoto_bsp      # bsp should point to the bsp file for your hw
import openmoto_signals
import openmoto_input

import threading

class inputEvent(dict):
    def __missing__(self, key):
        return 0

eventGroup = inputEvent()

# Set up events
eventGroup['leftturn'] = threading.Event()
eventGroup['rightturn'] = threading.Event()
eventGroup['brake'] = threading.Event()
eventGroup['start'] = threading.Event()
eventGroup['light'] = threading.Event()

# Set up threads
thread_right = openmoto_signals.turnThread(1, "RightTurn", openmoto_bsp.output_turnr, eventGroup['rightturn']);
thread_left = openmoto_signals.turnThread(2, "LeftTurn", openmoto_bsp.output_turnl, eventGroup['leftturn']);
thread_brake = openmoto_signals.brakeThread(3, "Brake", openmoto_bsp.output_brake, eventGroup['brake']);

# Start threads
thread_right.start()
thread_left.start()
thread_brake.start()

# Start getting inputs
openmoto_input.getTestInputs(eventGroup)

print "Exit main"
