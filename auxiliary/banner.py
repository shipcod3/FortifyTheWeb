import sys
import time

sys.path.append(r'auxiliary')
from colorful import *

def exitbanner():
	printout('******************************************\n', BLUE)
	printout('FTW (Fortify The Web)\n', BLUE)
	printout('Fortify On Demand - HP Enterprise Security\n', BLUE)
	printout('ShadowLabs\n', BLUE)
	printout('******************************************\n', BLUE)
	printout('Please provide target!\n', RED)
  	printout('Usage: python ftw.py target\n', WHITE)
  	printout('Example: python ftw.py google.com 80\n\n', WHITE)
  	sys.exit()	
	return;

def startbanner():
	printout('******************************************\n', BLUE)
	printout('FTW (Fortify The Web)\n', BLUE)
	printout('Fortify On Demand - HP Enterprise Security\n', BLUE)
	printout('ShadowLabs\n', BLUE)
	printout('******************************************\n', BLUE)
	print "Target:", sys.argv[1]
	print "Fortifying the Web now!!!"

def stage1():
	print "[Stage 1] Recon"
	print "[*] Checking if host is alive"
	time.sleep(2)




