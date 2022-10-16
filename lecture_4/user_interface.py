import data_provider as prov
import logger as log

def temper_view(sensor):
    data = prov.get_temper(sensor)
    log.temper_logger(data)
    return data

def press_view(sensor):
    data = prov.get_press(sensor)
    log.press_logger(data)
    return data   

    