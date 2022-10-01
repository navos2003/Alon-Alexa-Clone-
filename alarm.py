import datetime
from playsound import playsound


def alarm_Func(times):
    time = str(datetime.datetime.now().strptime(times,"%I:%M %p"))
    time = time[11:-3]
    hrs = time[:2]
    hrs = int(hrs)
    mins = time[3:5]
    mins = int(mins)
    print(f"\nAlarm set at {times}")

    while True:
        if (hrs != datetime.datetime.now().hour or mins != datetime.datetime.now().minute):
            continue
        print("\nAlarm is running")
        playsound('./commands/Ping1.wav')
        break
