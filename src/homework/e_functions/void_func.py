import value_return
import time

def time_printer(current_start):
    while (True == True):
        hour, minute, second = value_return.get_time(current_start)
        print(hour, ":", minute, ":", second)
        time.sleep(1)
        current_start+=1
