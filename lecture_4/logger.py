from datetime import datetime as dt

def temper_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; temperature; {}\n'
                    .format(time, data))

def press_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; pressure; {}\n'
                    .format(time, data))
