# Fortify The Web framework
# Web application security testing framework
# ______         _   _  __    _______ _       __          __  _     
#|  ____|       | | (_)/ _|  |__   __| |      \ \        / / | |    
#| |__ ___  _ __| |_ _| |_ _   _| |  | |__   __\ \  /\  / /__| |__  
#|  __/ _ \| '__| __| |  _| | | | |  | '_ \ / _ \ \/  \/ / _ \ '_ \ 
#| | | (_) | |  | |_| | | | |_| | |  | | | |  __/\  /\  /  __/ |_) |
#|_|  \___/|_|   \__|_|_|  \__, |_|  |_| |_|\___| \/  \/ \___|_.__/ 
#                           __/ |                                   
#                          |___/       
#
# description:       FortifyTheWeb Framework core
# author:            @semprix, @shipcod3, @httphacker, @napz, @medz
# platform:          Python
# version:           1.0rc1

# Load python libraries

import ping, time, sys, urllib2, subprocess, socket, ConfigParser, string

from termcolor import colored, cprint
from datetime import datetime

# Load ftw auxiliary

sys.path.append(r'auxiliary')
from banner import *
from colors import *

# Load stage 1 ftw modules

sys.path.append(r'modules/recon')
from grabheader import *
from subdomainLookup import *

sys.path.append(r'modules/discovery')
from dnsMiscon import *

# define your ftw directory installation
config = ConfigParser.ConfigParser()
config.read("config/config.ini")
ftwdir=config.get("path", "ftwdir")

# Check if target is within the argument

if len(sys.argv) <= 2 :
  print
  exitbanner()

else:

# Fortify the Web when ready
    starttime = datetime.now()
    startbanner()

# Run stage 1 banner
    stage1banner()

# Check host if alive

if sys.argv[2] == '80':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    try:
        s.connect((sys.argv[1], 80))
        print "[*] Using port 80 on target"
        print "[*] Checking if http port (80) on target is open"
        printout (' >> HTTP port on target is open', GREEN)
        printout (' >> Marking for http testing', GREEN)

        # Load application modules
        grabheader()
        dnsMiscon()
        subdomainLookup()
        stage2banner()
    except socket.error as e:
        printout (' >> Target seems to be down or port has been blocked', RED)
        s.close()


elif sys.argv[2] == '443':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    try:
        s.connect((sys.argv[1], 443))
        print "[*] Using port 443 on target"
        print "[*] Checking https port (443) on target is open"
        printout (' >> HTTPS port on target is open', GREEN)
        printout (' >> Marking for https testing', GREEN)

        # Load application modules
        grabheader()
        dnsMiscon()
        subdomainLookup()
        stage2banner()
    except socket.error as e:
        printout (' >> Target seems to be down or port has been blocked', RED)
        s.close()

else:
        printout (' [!] Target does not have default http(s) port', RED)
        time.sleep(3) # Give a little time to sleep

# Move scan results to data folder
print "[***] Cleaning up....."
print "[***] Moving report files to data folder"
time.sleep(5)
os.chdir(ftwdir)
os.renames(sys.argv[1], "data/" + sys.argv[1])
print ""
print "[!!!] Shutting down......"
time.sleep(4)
endtime = datetime.now()
total = endtime - starttime
print 'Scan completed in: ', total

