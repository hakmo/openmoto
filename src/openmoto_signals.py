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
        
# Thread class for PWM Brake signal
class brakeThread (threading.Thread):
    def __init__(self, threadID, name, output, event):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.out = output
        self.event = event
    def run(self):
        print "Starting " + self.name + '\n'
        self.out(openmoto_bsp.brakelight_min)
        while 1:
            if not self.event.isSet():
                self.out(openmoto_bsp.brakelight_min)
            self.event.wait()
            # Pop briefly to MAX
            self.out(openmoto_bsp.brakelight_max)
            time.sleep(openmoto_bsp.brakelight_delay)
            # Drop back to high
            self.out(openmoto_bsp.brakelight_max-openmoto_bsp.brakelight_step)
            time.sleep(openmoto_bsp.brakelight_delay*10)
        print "Exiting " + self.name + '\n'
    
