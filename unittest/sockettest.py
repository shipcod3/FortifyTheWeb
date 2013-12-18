# sockettest.py
# description: implementation of socket connection
# author: @semprix

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('google.com', 22))
    print "Port 22 reachable"
except socket.error as e:
    print "Error on connect: %s" % e
s.close()