# dnsMiscon.py
# description: checks if the domain has a dns misconfiguration
# author: @shipcod3

import sys, socket, time

from colors import *

def dnsMiscon():
    print "[**] Checking localhost."+sys.argv[1]+" for DNS Misconfiguration......"
    
    #resolve the host

    print "[+]Resolving the host address"
    ip_addr = socket.gethostbyaddr("localhost."+sys.argv[1])
    if ip_addr[0] == "localhost":
        printout('  >> Vulnerable to DNS Misconfiguration which leads to Same-Site Scripting', RED)
    else:
        printout('  >> Not Vulnerable', GREEN)     
    
    print "[==] Done checking for DNS Misconfiguration"
    time.sleep(3)
