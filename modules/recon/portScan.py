# portScan.py
# description: fortify the web port scanner module
# author: @semprix

import sys, os, socket

from colors import *

def portScan():
	print '[**] Starting port scan......'
	target = sys.argv[1]
	targetIP = socket.gethostbyname(target)
	
	print targetIP