import time, sys
from sys import stdout
from termcolor import colored, cprint

def loader(text):
    for c in text:
        print c,
        sys.stdout.flush()
        time.sleep(0.9)
loader('*=*=*=*=*=*=*=*\n')
