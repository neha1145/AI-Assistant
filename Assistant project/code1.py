#import pyttsx3 #external library installed using command "pip install pyttsx3"---->FOR TEXT TO SPEECH CONVERSION
#import datetime  #BUILT-IN LIBRARY--->FOR KNOWING CURRENT DATE-TIME
#import speech_recognition as sr  #EXTERNAL LIBRARY INSTALLED USING pip install SpeechRecognition---->FOR SPEECH TO TEXT CONVERSION
#import smtplib  #BUILT-IN FUNCTION--->FOR SENDING EMAILS
import pyautogui#-----for scrnshoot
import os
import time
import psutil#external library for battery and cpu usage
from tkinter import *



from GoogleSearch import *
from Speak import *
from TakeCommand import *
from DateAndTime import *
from WishMe import *
from SendEmailPart2A import *
from offline import *
from OpenOffice import *
from DescribeSelf import *
from RepeatWords import *
from ChromeSearch import *
from ShutDownRestart import *
#from TakeScreenShot import *

def take_screenshot(root1):
    try:
        root1.destroy()
        time.sleep(5)
        img= pyautogui.screenshot()
        root=Tk()
        root.title("Assistant")
        root.geometry('400x400')
        root.resizable(0,0)
        speak('please give a file name to save your screenshot')
        label_scrn=Label(text="File name")
        label_scrn.pack()
        FileName=Text(root,height=3,width=30)
        FileName.pack()
        Submit=Button(root,text="Save",command = lambda: save_file(root,FileName.get(1.0,'end-1c'),img))
        Submit.pack()
    except Exception as e:
        pass
def save_file(root,NameYourFile,img):
    #NameYourFile=takeCommand(root)
    NameYourFile+=".png"
    if NameYourFile!='none':
        pathOfFile="C:\\Users\\lenovo\\OneDrive\\Desktop\\javascript_package\\screenshots of assistant\\"
        img.save(os.path.join(pathOfFile+NameYourFile))
        speak('screenshot saved')
    else:
        speak('screenshot is not saved as you did not provide any file name to save')
    print_gui(root,'')
    start_assistance(root)

def start_assistance(root1):
    for widgets in root1.winfo_children():
        widgets.destroy()
    root=LabelFrame(root1 ,text="Your Commands",bg='white')
    root.pack(fill="both",expand="yes")
    wishme()
    speak("Welcome back! Hope you are doing well How can I help you?")
    while True:
        query=takeCommand(root).lower()
        #TIME FUNCTION CALLING
        if 'time' in query:
            current_time()

        #DATE FUNCTION CALLING
        elif 'date' in query:
            date_today()


        #SEND EMAIL FUNCTION CALLING
        elif 'send email' in query:
            email_send_gui(root1)

        #DESCRIBES ABOUT ITS ABILITY
        elif 'tell me about yourself' in query:
            desc_self()
        #WISH AGAIN
        elif 'wish me' in query:
            speak("  You are radiant You can achieve anything in your life ")

        #repeat after me
        elif 'repeat my words' in query:
            repeat_words(root)
        #EXIT THE LOOP
        elif 'offline' in query:
            offline(root,root1)
            button = Button(root1, text="RUN", command= lambda: start_assistance(root1)) 
            button.pack()
            break
        #OPEN MICROSOFT WORD
        elif 'open word' in query:
            mic_file('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007')
        #OPEN MICROSOFT POWERPOINT
        elif 'open powerpoint' in query:
            mic_file('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office PowerPoint 2007')
        #OPEN MICROSOFT EXCEL
        elif 'open excel' in query:
            mic_file('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007')
        #SEARCH IN CHROME
        elif 'search in chrome' in query:
            chrome_search(root)
        #GOOGLE SEARCH
        elif 'google search' in query:
            google_search(root)
        #SHUTDOWN AND RESTART MACHINE
        elif 'logout' in query:
            shut_restart("shutdown -l")
        elif 'shutdown' in query:
            shut_restart("shutdown /s /t 1")
        elif 'restart' in query:
            shut_restart("shutdown /r /t 1")
        #SCREENSHOT
        elif 'screenshot' in query:
            take_screenshot(root1)
        #CPU AND BATTERY USAGE
        #elif 'CPU and Battery Usage' in query:
           
        #JOKES
def gui_work():
    root=Tk()
    root.title("Assistant")
    root.geometry('400x400')
    root.resizable(0,0)
    root.configure(bg='black')
    button = Button(root, text="RUN", command= lambda: start_assistance(root)) 
    button.pack()
    root.mainloop()


if __name__=="__main__":
    gui_work()
