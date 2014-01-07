# bootstrap.py
# description: Dependency checker, bootstrapping FTW.
# author: @semprix

import sys, os, time

ftwmods =['socket','nmap','bs4','requests','termcolor','ping','beautifulsoap']

print "[***] BootStrapping FortifyTheWeb. Please wait....."
print "  [+] Getting OS version"
ftwenv = os.uname()
print        ftwenv

print "  [+] Checking for python modules"
for module_name in ftwmods:
  try:
    __import__(module_name)
    print " ++ Module %s found." %(module_name) 
  except ImportError:
    print "\033[91m -- Please install dependency ==>> (%s). \033[0m" %(module_name)
    print "BootStrap finishing"
    print ""
time.sleep(3)
