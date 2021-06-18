from tkinter import *
from Speak import *
from code1 import *


def offline(root,root1):
    speak(" hope to see you again Good Bye! ")
    root.destroy()
    root1.configure(bg='black')
    for widgets in root1.winfo_children():
        widgets.destroy()
