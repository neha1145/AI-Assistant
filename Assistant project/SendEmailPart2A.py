#from Speak import *
#from TakeCommand import *
#from PrintGUI import *
from tkinter import *
from SendEmail import *
from code1 import *

def email_send_gui(root1):
    try:
        root1.destroy()
        root=Tk()
        root.title("Assistant")
        root.geometry('400x400')
        root.resizable(0,0)
        label1=Label(text='To')
        label1.pack()
        To=Text(root,height=3,width=30)
        To.pack()
        label2=Label(text='Subject')
        label2.pack()
        Subject=Text(root,height=3,width=30)
        Subject.pack()
        label3=Label(text="Content")
        label3.pack()
        Content=Text(root,height=10,width=30)
        Content.pack()
        
        SendButton=Button(root,text="Send",command = lambda: click_event(root,To.get(1.0,END),Content.get(1.0,END),Subject.get(1.0,END)))
        SendButton.pack()
    except Exception as e:
        #print(e)
        speak("unable to send mail")

def click_event(root,To,Content,Subject):
    print_gui(root,'To: '+To+"\n"+"Subject: "+Subject+"\n"+"Content: \n"+Content)
    send_email(root,To,Content,Subject)
    print_gui(root,'')
    start_assistance(root)
    #gui_work()

