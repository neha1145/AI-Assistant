import pyttsx3 #external library installed using command "pip install pyttsx3"---->FOR TEXT TO SPEECH CONVERSION
import datetime  #BUILT-IN LIBRARY--->FOR KNOWING CURRENT DATE-TIME
import speech_recognition as sr  #EXTERNAL LIBRARY INSTALLED USING pip install SpeechRecognition---->FOR SPEECH TO TEXT CONVERSION
import smtplib  #BUILT-IN FUNCTION--->FOR SENDING EMAILS
import pyautogui
import os
import webbrowser as wb
import psutil#external library for battery and cpu usage
from selenium import webdriver
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
#from front_assistant import *
from tkinter import *
engine=pyttsx3.init() 
#To print in gui
def print_gui(root,value):
    for widgets in root.winfo_children():
            widgets.destroy() 
    var=StringVar()
    #print(value)
    label = Label( root, text=value,relief=FLAT)
    var.set(value)
    label.pack(fill="both")
    root.update()

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

#takeCommand()

#SEND EMAIL FUNCTION
def send_email(root,to,content):
    msg=MIMEMultipart()
    msg['From']='krineha538@gmail.com'
    msg['To']=to
    speak("Give subject to your email")
    msg['Subject']=takeCommand(root)
    
    msg.attach(MIMEText(content,'plain'))
    text=msg.as_string()
    print_gui(root,text)
    server=smtplib.SMTP('smtp.gmail.com',587)
    #server.echo()
    server.starttls()
    server.login('krineha538@gmail.com','Shefali@123')
    server.sendmail('krineha538@gmail.com',to,text)
    server.close()
#Feature description
def desc_self():
    prop="Hello! I am an assistant currently in development mode Till now I am able to greet you, tell you time and date, send mail to your friend and can describe about myself Thank you! hope that you like me"
    speak(prop)

#Repeat after me 
def repeat_words(root):
    commd=takeCommand(root)
    speak(commd)
#Open Microsoft Files
def mic_file(path):
    os.startfile(path)
#Search in chrome
def chrome_search(root):
    speak('What should I search ?')
    chromepath='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    search= takeCommand(root).lower()
    wb.get(chromepath).open_new_tab(search+".com")
    print_gui(root,' ')
#Search in google
def google_search(root):
    #speak('What should i search ?')
    driver = webdriver.Chrome('C:/Program Files/Google/Chrome/Application/chromedriver.exe')
    driver.get('https://www.google.com')
    SearchBox=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    speak('What do you want to search in google ?')
    SearchBox.send_keys(takeCommand(root).lower())
    SearchButton= driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
    SearchButton.click()
    try:
        SearchResult=driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]').text
        speak(SearchResult)
        print_gui(SearchResult)
    except Exception as e:
        print_gui(root,' ')
    
    #print("-----------------------------")

    #print(SearchResult.get_attribute('text'))
    #lines=''
    #for result in SearchResult:
        #print(result.text)
    #print_gui(root,lines)
    #print(lines)
#Shut down and restart
def shut_restart(path):
    os.system(path)
    speak(" hope to see you again Good Bye! ")
    quit()
def take_screenshot(root):
    img= pyautogui.screenshot()
    speak('please give a file name to save your screenshot')
    NameYourFile=takeCommand(root)
    NameYourFile+=".png"
    if NameYourFile!='none':
        pathOfFile="C:\\Users\\lenovo\\OneDrive\\Desktop\\javascript_package\\screenshots of assistant\\"
        img.save(os.path.join(pathOfFile+NameYourFile))
        speak('screenshot saved')
    else:
        speak('screenshot is not saved as you did not provide any file name to save')
#MAIN FUNCTION TO PERFORM TASKS
#if __name__=="__main__":
def start_assistance(root1):
    root=LabelFrame(root1 ,text="Your Commands",bg='white')
    root.pack(fill="both",expand="yes")
    #scrollbar=Scrollbar(root)
    #scrollbar.pack(side=RIGHT,fill=BOTH)
    #root.config(yscrollcommand=scrollbar.set)
    #scrollbar.config(command=root.yview)
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
            try:
                #listbox=Listbox(root)
                #listbox.pack(side=LEFT,fill=BOTH)
                #scrollbar=Scrollbar(root)
                #scrollbar.pack(side=RIGHT,fill=BOTH)
                speak("what do yo want to say")
                #content=takeCommand(root)
                txt=takeCommand(root).lower()
                content=''
                while True:
                    if 'assistant done' in txt:
                        break
                    else:
                        content +=txt+'\n'
                        txt=takeCommand(root).lower()
                
                print_gui(root,content)
                speak(content)
                speak("whom to send?")
                person_to=takeCommand(root)
                print_gui(root,person_to.replace(" ","")+"-------")
                #listbox.insert(END,person_to.replace(" ","")+"-------")
                speak("sending mail to"+person_to)
                speak("Should i send the mail?")
                chk=takeCommand(root)
                print_gui(root,chk)
                #listbox.config(yscrollcommand=scrollbar.set)
                #scrollbar.config(command=listbox.yview)
                if chk=='yes':
                    send_email(root,person_to.replace(" ",""),content)
                    speak("email has been sent")
                    print_gui(root,"email has been sent")
                else:
                    speak("mail not sent")
                    print_gui(root,"email not sent")
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
            repeat_words(root)
        #EXIT THE LOOP
        elif 'offline' in query:
            speak(" hope to see you again Good Bye! ")
            root.destroy()
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
            take_screenshot(root)
        #CPU AND BATTERY USAGE
        #elif 'CPU and Battery Usage' in query:
           
        #JOKES

if __name__=="__main__":
    root=Tk()
    root.title("Assistant")
    root.geometry('400x400')
    root.resizable(0,0)
    root.configure(bg='black')
    button = Button(root, text="RUN", command= lambda: start_assistance(root)) 
    button.pack()
    #h=Scrollbar(root,orient='vertical')
    #h.config(command=t.yview)
    root.mainloop()
