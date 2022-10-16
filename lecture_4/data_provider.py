from random import randint

def get_temper(sensor):
    return randint(-20,0) if sensor else randint (0,35)

def get_press(sensor):
    if sensor:
        return randint (710, 730)
    else:
        return randint(730, 750)

def data_collect(sensor = 1):
    return (get_temper(sensor), get_press(sensor))
