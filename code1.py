import pyttsx3 #external library installed using command "pip install pyttsx3"---->FOR TEXT TO SPEECH CONVERSION
import datetime  #BUILT-IN LIBRARY--->FOR KNOWING CURRENT DATE-TIME
import speech_recognition as sr  #EXTERNAL LIBRARY INSTALLED USING pip install SpeechRecognition---->FOR SPEECH TO TEXT CONVERSION
import smtplib  #BUILT-IN FUNCTION--->FOR SENDING EMAILS
import pyautogui
import os
import webbrowser as wb
from selenium import webdriver

engine=pyttsx3.init() 

#USER DEFINED FUNCTION
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#KNOW THE CURRENT TIME
def current_time():
    time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)

#speak("Welcome back")
#current_time()

#KNOW TODAY'S DATE WITH YEAR AND MONTH
def date_today():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak(date)
    speak(month)
    speak(year)
#date_today()

#GREETINGS FUNCTION
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
#wishme()

#SPEECH TO TEXT CONVERSION
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        #r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print(query)
        speak("You said   ")
        speak(query)
       
    except Exception as e:
        print(e)
        speak("Please repeat")  
        return "None"
    return query

#takeCommand()

#SEND EMAIL FUNCTION
def send_email(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    #server.echo()
    server.starttls()
    server.login('krineha538@gmail.com','Shefali@123')
    server.sendmail('krineha538@gmail.com',to,content)
    server.close()
#Feature description
def desc_self():
    prop="Hello! I am an assistant currently in development mode Till now I am able to greet you, tell you time and date, send mail to your friend and can describe about myself Thank you! hope that you like me"
    speak(prop)

#Repeat after me 
def repeat_words():
    commd=takeCommand()
    speak(commd)




#MAIN FUNCTION TO PERFORM TASKS
if __name__=="__main__":
    wishme()
    speak("Welcome back! Hope you are doing well How can I help you?")
    while True:
        query=takeCommand().lower()
        #TIME FUNCTION CALLING
        if 'time' in query:
            current_time()

        #DATE FUNCTION CALLING
        elif 'date' in query:
            date_today()


        #SEND EMAIL FUNCTION CALLING
        elif 'send email' in query:
            try:
                speak("what do yo want to say")
                content=takeCommand()
                speak("whom to send?")
                person_to=takeCommand()
                print(person_to.replace(" ","")+"-------")
                speak("sending mail to"+person_to)
                speak("Should i send the mail?")
                chk=takeCommand()
                if chk=='yes':
                    send_email(person_to.replace(" ",""),content)
                    speak("email has been sent")
                else:
                    speak("mail not sent")
            except Exception as e:
                print(e)
                speak("unable to send mail")
        #DESCRIBES ABOUT ITS ABILITY
        elif 'tell me about yourself' in query:
            desc_self()
        #WISH AGAIN
        elif 'wish me' in query:
            speak("  You are radiant You can achieve anything in your life ")

        #repeat after me
        elif 'repeat my words' in query:
            repeat_words()
        #EXIT THE LOOP
        elif 'offline' in query:
            speak(" hope to see you again Good Bye! ")
            quit()
        elif 'open word' in query:
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007')
        elif 'open powerpoint' in query:
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office PowerPoint 2007')
        elif 'open excel' in query:
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007')
        elif 'search in chrome' in query:
            speak('What should I search ?')
            chromepath='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search= takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")
        elif 'google search' in query:
            speak('What should i search ?')
            driver = webdriver.Chrome('C:/Program Files/Google/Chrome/Application/chromedriver.exe')
            driver.get('https://www.google.com')
            SearchBox=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            speak('What do you want to search in google ?')
            SearchBox.send_keys(takeCommand().lower())

            SearchButton= driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
            SearchButton.click()