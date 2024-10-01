

def get_hour(total_sec):
    hours = int(total_sec/3600)
    return hours

def get_minutes(total_sec):
    hours = get_hour(total_sec)
    minutes = int(total_sec/60-hours*60)
    return minutes

def get_seconds(total_sec):
    hours = get_hour(total_sec)
    minutes = get_minutes(total_sec)
    seconds = total_sec-(minutes*60+hours*3600)
    return seconds

#Bonus
def get_time(total_sec):
    hours = int(total_sec/3600)
    minutes = int(total_sec/60-hours*60)
    seconds = total_sec-(minutes*60+hours*3600)
    return hours, minutes, seconds
