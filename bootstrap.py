# bootstrap.py
# description: Dependency checker, bootstrapping FTW.
# author: @semprix

import sys, os, time, ConfigParser, platform

ftwmods =['socket','bs4','requests','termcolor','ping', 'ConfigParser']

# define your ftw directory installation
config = ConfigParser.ConfigParser()
config.read("config/config.ini")
ftwdir=config.get("path", "ftwdir")

print "[***] BootStrapping FortifyTheWeb. Please wait....."
time.sleep (5)
print "[+] Getting OS version"
ftwenv = platform.platform()
print        ftwenv
print "[+] Checking FTW data path"
print "[**] Data path found on:" + ftwdir + " (define path if needed)"
print ""
print "[+] Checking for required python modules"
for module_name in ftwmods:
  try:
    __import__(module_name)
    print " ++ Module %s found." %(module_name) 
  except ImportError:
    print "\033[91m -- Please install dependency ==>> (%s). \033[0m" %(module_name)
print ""
print "BootStrap finishing"
time.sleep(3)
