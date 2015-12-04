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

def input_turnr(key):       # returns the state of the right turn input
    if key == 77:           # (right arrow)
        return 1
    else:
        return 0

def input_start(key):       # returns the state of the start input
    if key == 115:          # (s)
        return 1
    else:
        return 0

def input_horn(key):        # returns the state of the horn input
    if key == 104:          # (h)
        return 1
    else:
        return 0

def input_turnl(key):       # returns the state of the left turn input
    if key == 75:           # (left arrow)
        return 1
    else:
        return 0

def input_config(key):     # returns the state of the config input
    return 0

def input_light(key):       # returns the state of the light input
    if key == 108:          # (l)
        return 1
    else:
        return 0

def input_brake(key):       # returns the state of the brake input
    if key == 80:           # (down arrow)
        return 1
    else:
        return 0

def input_lock(key):       # returns the state of the lock input
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
    print "Brake: " + str(o) + '\n'
    return 0

def output_aux(o):      # sets aux output to given value
    return 0


