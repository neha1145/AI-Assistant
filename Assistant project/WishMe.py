from Speak import *
from DateAndTime import *

def wishme():
#RETURNS HOUR BY WHICH WE DECIDE USING IF ELSE STATEMENT OF THE TIME OF DAY
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("good afternoon sir")
    elif hour>=18 and hour<24:
        speak("good evening sir")
    else:
        speak("good night sir")

    speak("Assistant at your service")