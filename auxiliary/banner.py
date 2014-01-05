# banner.py
# description: banner used at core
# author: @semprix

import sys, time, socket, os

sys.path.append(r'auxiliary')
from timer import *
from colors import *

def startbanner():

	print" \033[94m ______         _   _  __    _______ _       __          __  _\033[0m"  
	print" \033[94m|  ____|       | | (_)/ _|  |__   __| |      \ \        / / | |\033[0m"    
	print" \033[94m| |__ ___  _ __| |_ _| |_ _   _| |  | |__   __\ \  /\  / /__| |__\033[0m"  
	print" \033[94m|  __/ _ \| '__| __| |  _| | | | |  | '_ \ / _ \ \/  \/ / _ \ '_ \ \033[0m" 
	print" \033[94m| | | (_) | |  | |_| | | | |_| | |  | | | |  __/\  /\  /  __/ |_) |\033[0m"
	print" \033[94m|_|  \___/|_|   \__|_|_|  \__, |_|  |_| |_|\___| \/  \/ \___|_.__/ \033[0m"
	print" \033[94m                           __/ |                        ShadowLabs  \033[0m"
	print"  \033[94m                         |___/       \033[0m"
	print""
	print(' \033[94m******************************************\033[0m')
	print(' \033[94mFTW (Fortify The Web)\033[0m')
	print(' \033[94mDevs: @semprix, @httphacker, @shipcod3, @napz\033[0m')
	print(' \033[94mVersion: v1.0\033[0m')
	print(' \033[94m******************************************\033[0m')
	print ""

	print "Target:", sys.argv[1]
	try:
		reversedns = socket.gethostbyname(sys.argv[1])
		print "IP Address:", reversedns
		print "Fortifying the Web now!!!"
	except socket.error as e:
		printout (' >> Hostname lookup failed, application will now shutdown', RED)
		time.sleep(3)
		print "[*] Shutting down"
		timer()
		sys.exit()

def stage1banner():
	print "\033[94m[Starting Stage 1] Passive Reconnaissance\033[0m"
	time.sleep(2)


def exitbanner():

	print" \033[94m ______         _   _  __    _______ _       __          __  _\033[0m"  
	print" \033[94m|  ____|       | | (_)/ _|  |__   __| |      \ \        / / | |\033[0m"    
	print" \033[94m| |__ ___  _ __| |_ _| |_ _   _| |  | |__   __\ \  /\  / /__| |__\033[0m"  
	print" \033[94m|  __/ _ \| '__| __| |  _| | | | |  | '_ \ / _ \ \/  \/ / _ \ '_ \ \033[0m" 
	print" \033[94m| | | (_) | |  | |_| | | | |_| | |  | | | |  __/\  /\  /  __/ |_) |\033[0m"
	print" \033[94m|_|  \___/|_|   \__|_|_|  \__, |_|  |_| |_|\___| \/  \/ \___|_.__/ \033[0m"
	print" \033[94m                           __/ |                        ShadowLabs  \033[0m"
	print"  \033[94m                         |___/       \033[0m"
	print""
	print(' \033[94m******************************************\033[0m')
	print(' \033[94mFTW (Fortify The Web)\033[0m')
	print(' \033[94mDevs: @semprix, @httphacker, @shipcod3, @napz\033[0m')
	print(' \033[94mVersion: v1.0\033[0m')
	print(' \033[94m******************************************\033[0m')
	print(' \033[91mPlease provide target!\033[0m')
  	print(' \033[91mUsage: python ftw.py target\033[0m')
  	print(' \033[91mExample: python ftw.py google.com 80\033[0m')
  	print""
  	sys.exit()	
	return;






