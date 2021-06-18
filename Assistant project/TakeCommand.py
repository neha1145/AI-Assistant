import speech_recognition as sr
from Speak import *
from PrintGUI import *

def takeCommand(root):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        var1="Listening..."
        print_gui(root,var1)
        r.adjust_for_ambient_noise(source,duration=1)
        #r.pause_threshold=1
        audio=r.listen(source)
    try:
        var2="Recognizing..."
        print_gui(root,var2)
        query=r.recognize_google(audio)
        print_gui(root,query)
        speak("You said   ")
        speak(query)
       
    except Exception as e:
        print(e)
        speak("Please repeat")  
        return "None"
    return query

