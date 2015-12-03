###########
# Globals #
###########
turnsignal_min = 0
turnsignal_max = 255
turnsignal_step = 15
turnsignal_delay = 0.1

brakelight_min = 75
brakelight_max = 255
brakelight_step = 100
brakelight_delay = 0.1


##########
# Inputs #
##########

def input_turnr():      # returns the state of the right turn input
    return 0

def input_start():      # returns the state of the start input
    return 0

def input_horn():       # returns the state of the horn input
    return 0

def input_turnl():      # returns the state of the left turn input
    return 0

def input_config():     # returns the state of the config input
    return 0

def input_light():      # returns the state of the light input
    return 0

def input_brake():      # returns the state of the brake input
    return 0

def input_lock():       # returns the state of the lock input
    return 0


###########
# Outputs #
###########

def output_turnr(o):    # sets right turn output to given value
    print "Right Turn: " + str(o) + '\n'
    return 0

def output_start(o):    # sets start output to given value
    return 0

def output_horn(o):     # sets horn output to given value
    return 0

def output_turnl(o):    # sets left turn output to given value
    print "Left Turn: " + str(o) + '\n'
    return 0

def output_lightlo(o):  # sets light lo output to given value
    return 0

def output_lighthi(o):  # sets light hi output to given value
    return 0

def output_brake(o):    # sets brake output to given value
    return 0

def output_aux(o):      # sets aux output to given value
    return 0


