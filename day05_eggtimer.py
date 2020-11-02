import datetime
from datetime import datetime, time, timedelta


def now_time():
    return (datetime.now())


def get_timer():
    return int(input("How many minutes do you want? "))


def new_time(current_time, minutes):
    return current_time + timedelta(minutes=minutes)


def countdown(alarm_time):
    while alarm_time > datetime.now():
        continue
    else:
        print("time's up")


if __name__ == "__main__":
    current_time = now_time()
    print(f"Current time is {current_time}")
    minutes = get_timer()
    alarm_time = new_time(current_time, minutes)
    print(f"Alarm set for {alarm_time}")
    countdown(alarm_time)
