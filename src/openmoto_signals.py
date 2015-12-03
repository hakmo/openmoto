# Contains the threads for handling turn signals and tail/brake light

import bsp as openmoto_bsp      # bsp should point to the bsp file for your hw
import threading
import time

# Thread class for PWM Turn signals
class turnThread (threading.Thread):
    def __init__(self, threadID, name, output, event):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.out = output
        self.event = event
    def run(self):
        print "Starting " + self.name + '\n'
        value = openmoto_bsp.turnsignal_min
        while 1:
            if not self.event.isSet():
                step = openmoto_bsp.turnsignal_step
                value = openmoto_bsp.turnsignal_min
            self.event.wait()
            self.out(value)
            time.sleep(openmoto_bsp.turnsignal_delay)
            value += step
            if value >= openmoto_bsp.turnsignal_max or value <= openmoto_bsp.turnsignal_min:
                step = -step
                time.sleep(3*openmoto_bsp.turnsignal_delay)
        print "Exiting " + self.name + '\n'
        
    
