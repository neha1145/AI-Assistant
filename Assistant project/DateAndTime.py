from Speak import *
import datetime

def date_today():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak(date)
    speak(month)
    speak(year)
def current_time():
    time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)