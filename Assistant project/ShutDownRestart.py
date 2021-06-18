import os
from Speak import *

def shut_restart(path):
    os.system(path)
    speak(" hope to see you again Good Bye! ")
    quit()