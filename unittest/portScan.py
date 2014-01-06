import os, sys
from socket import *


print '[**] Starting port scan'
target = sys.argv[1]
targetIP = gethostbyname(target)

    #scan reserved ports
    for i in range(20, 1025):
        s = socket(AF_INET, SOCK_STREAM)

        result = s.connect_ex((targetIP, i))

        if(result == 0) :
            print 'Port %d: OPEN' % (i,)
        s.close()

print targetIP