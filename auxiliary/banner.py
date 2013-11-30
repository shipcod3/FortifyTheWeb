import sys
import time
import socket
import os

def exitbanner():
	print('\033[94m******************************************\033[0m')
	print('\033[94mFTW (Fortify The Web)\033[0m')
	print('\033[94mFortify On Demand - HP Enterprise Security\033[0m')
	print('\033[94mShadowLabs\033[0m')
	print('\033[94m******************************************\033[0m')
	print('\033[91mPlease provide target!\033[0m')
  	print('\033[91mmUsage: python ftw.py target\033[0m')
  	print('\033[91mExample: python ftw.py google.com 80\033[0m')
  	sys.exit()	
	return;

def startbanner():
	print('\033[94m******************************************\033[0m')
	print('\033[94mFTW (Fortify The Web)\033[0m')
	print('\033[94mFortify On Demand - HP Enterprise Security\033[0m')
	print('\033[94mShadowLabs\033[0m')
	print('\033[94m******************************************\033[0m')
	
	print "Target:", sys.argv[1]
	ip_add = socket.gethostbyaddr(sys.argv[1])
	print "IP Address:", ip_add
	print "Fortifying the Web now!!!"

def stage1():
	print "[Stage 1] Passive Reconnaissance"
	time.sleep(2)




