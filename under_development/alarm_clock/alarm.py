import datetime
from playsound import playsound
alarmHour = int(input("Enter hour: "))
alarmMin = int(input("Enter minute: "))
alarmAm = input("Enter AM/PM: ")

if alarmAm=="pm":
    alarmHour+=12

while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("Its time...")
        playsound("alarm.mp3")
        break