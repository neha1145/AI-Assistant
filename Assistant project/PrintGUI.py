from tkinter import *

def print_gui(root,value):
    for widgets in root.winfo_children():
            widgets.destroy() 
    var=StringVar()
    #print(len(value))
    label = Label( root, text=value,relief=FLAT,wraplength=400,height=0)
    #label.config(height=4,width=4)
    var.set(value)
    label.pack(expand=YES,fill="both")
    root.update()