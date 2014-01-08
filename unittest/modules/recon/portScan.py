# portScan.py
# description: port scanner for ftw
# author: @semprix

import os, sys, socket

print '[**] Starting port scan'
target = sys.argv[1]
targetIP = socket.gethostbyname(target)
print targetIP
    #scan reserved ports
for i in range(22, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = s.connect_ex((targetIP, i))
    if(result == 0) :
	    print 'Port %d: OPEN' % (i,)
    s.close()

print targetIP