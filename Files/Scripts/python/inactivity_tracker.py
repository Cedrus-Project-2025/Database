from datetime import datetime, timedelta

# Última vez que se accedió a la API
last_access = datetime.now()

def update_last_access():
    global last_access
    last_access = datetime.now()

def is_time_to_backup():
    now = datetime.now()
    diff = now - last_access
    return diff > timedelta(minutes=4)
