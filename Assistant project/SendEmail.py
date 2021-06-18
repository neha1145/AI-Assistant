import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from Speak import *
from TakeCommand import *
from PrintGUI import *

def send_email(root,to,content,subject):
    try:
        msg=MIMEMultipart()
        msg['From']='krineha538@gmail.com'
        msg['To']=to
    
        msg['Subject']=subject
    
        msg.attach(MIMEText(content,'plain'))
        text=msg.as_string()
    #print_gui(root,text)
        server=smtplib.SMTP('smtp.gmail.com',587)
    #server.echo()
        server.starttls()
        server.login('krineha538@gmail.com','Shefali@123')
        server.sendmail('krineha538@gmail.com',to,text)
        server.close()
        speak("Email has been sent")
        print_gui(root,'Email has been sent')
    except Exception as e1:
        speak("Email not sent  Please try again")