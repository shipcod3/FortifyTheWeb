# ftw.py - Fortify The Web
# 
#
#
#

# Required Python libs

import ping, socket
import time
import sys
import urllib2
import subprocess
import socket
from termcolor import colored, cprint

# Load auxiliary

sys.path.append(r'auxiliary')
from banner import *

# Check if target is within the argument
if len(sys.argv) <= 2 :
  print
  exitbanner()

else:

# Fortify the Web when ready
    startbanner()
    stage1()

# Check host if alive

if sys.argv[2] == '80':
    print "[*] Checking for default http port (80)"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Using socket to connect to default HTTP port
    try:
        s.connect((sys.argv[1], 80))
        cprint ('>> Target is up', 'green')
        cprint ('>> Marking for http testing', 'green')
    except socket.error as e:
        cprint ('>> Target is down', 'red')
        s.close()

elif sys.argv[2] == '443':
    print "[*] Checking for default secure http port (443)"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Using socket to connect to default HTTP port
    try:
        s.connect((sys.argv[1], 443))
        cprint ('>> Target is up', 'green')
        cprint ('>> Marking for https testing', 'green')
    except socket.error as e:
        cprint ('>> Target is down', 'red')
        s.close()

else:
     cprint ('[-] Not a default HTTP port', 'red')
     cprint ('[*] Shutting down....', 'red')
     time.sleep(3) # Give a little time to sleep


 # Load modules for testing

