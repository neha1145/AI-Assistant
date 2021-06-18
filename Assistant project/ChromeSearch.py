import webbrowser as wb
from Speak import *
from TakeCommand import *
from PrintGUI import *


def chrome_search(root):
    speak('What should I search ?')
    chromepath='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    search= takeCommand(root).lower()
    wb.get(chromepath).open_new_tab(search+".com")
    print_gui(root,' ')