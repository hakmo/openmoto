#!/usr/bin/python

import bsp as openmoto_bsp      # bsp should point to the bsp file for your hw
import threading
import time

# Thread class for PWM Turn signals
class turnThread (threading.Thread):
    def __init__(self, threadID, name, output):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.out = output
        self.value = openmoto_bsp.turnsignal_min
    def run(self):
        print "Starting " + self.name
        blink_turn(self.name, self.out, self.value)
        print "Exiting " + self.name

# Controls the turn signal PWM values
def blink_turn(threadName, output, value):
    step = openmoto_bsp.turnsignal_step
    while 1:
        output(value)
        time.sleep(openmoto_bsp.turnsignal_delay)
        value += step
        if value >= openmoto_bsp.turnsignal_max or value <= openmoto_bsp.turnsignal_min:
            step = -step
        


thread_right = turnThread(1, "RightTurn", openmoto_bsp.output_turnr);

thread_right.start()

print "Exit main"
