# portScan.py
# description: ftw port scanner module
# author: @semprix

import sys, os, socket

from colors import *

def portScan():
 
     target    = sys.argv[1]
     targetIP  = socket.gethostbyname(target)

     try:
        for port in range(1,1025):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((targetIP, port))
        if result == 0:
            print "Port {}: \t Open".format(port)
            sock.close()
 
     except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()
 
     except socket.error:
        print "Couldn't connect to server"
        sys.exit()