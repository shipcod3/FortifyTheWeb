# portScan.py
# description: ftw port scanner module
# author: @semprix

import sys, os, socket

from colors import *

def portScan():
	print '[**] Starting port scan......'
	target = sys.argv[1]
	targetIP = socket.gethostbyname(target)
	
	for i in range(443, 450):
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

         result = s.connect_ex((targetIP, i))

        if(result == 0) :
            print 'Port %d: OPEN' % (i,)
        s.close()

