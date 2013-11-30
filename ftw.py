# ftw.py - Fortify The Web
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

sys.path.append(r'auxiliary')
from banner import *
from colorful import has_colours, printout


# Check if target is within the argument
if len(sys.argv) < 2:
  print
  exitbanner()

else:

# Fortify the Web when ready
    startbanner()
	
# Check the default http port if we can connect	(80)
print "[*] Checking for default http port (80)"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Using socket to connect to default HTTP port
try:
    s.connect((sys.argv[1], 80))
    cprint ('>> Target is up', 'green')
except socket.error as e:
    cprint ('>> Target is down', 'red')
s.close()

# Check the default secure port if we can connect (443)

print "[*] Checking for default secure port (443)"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Using socket to connect to secure (SSL) HTTP port
try:
    s.connect((sys.argv[1], 443))
    cprint ('>> Target is up', 'green')
except socket.error as e:
    cprint ('>> Target is down', 'red')
s.close()

time.sleep(3) # Give the app a little sleep

