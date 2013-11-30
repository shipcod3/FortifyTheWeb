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


# Color definition fork from httphacker

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        return False
has_colours = has_colours(sys.stdout)
def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)

# Check if target is within the argument
if len(sys.argv) < 2:
  print
  printout('Please provide target!\n', RED)
  printout('Usage: python ftw.py path\n', WHITE)
  printout('Example: python ftw.py google.com\n\n', WHITE)
  sys.exit()
else:

# Fortify the Web when ready
	print "*******************************"
	print "FTW (Fortify The Web"
	print "Fortify On Demand - HP Enterprise Security"
	print "*******************************"
	print "Setting Target:", sys.argv[1]
	print "Fortifying the Web now!!!"
	print "\n"
	print "[*] Performing Stage 1 Recon"
	#time.sleep(5)
	print "[*] Checking for default http port"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Using socket to connect to default HTTP port
try:
    s.connect((sys.argv[1], 80))
    cprint ('>> Target is up', 'green')
except socket.error as e:
    cprint ('>> Target is down', 'red')
s.close()

print "[*] Checking for secure http port"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Using socket to connect to secure (SSL) HTTP port
try:
    s.connect((sys.argv[1], 443))
    cprint ('>> Target is up', 'green')
except socket.error as e:
    cprint ('>> Target is down', 'red')
s.close()

time.sleep(5)

