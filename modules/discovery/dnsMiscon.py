# dnsMiscon.py
# description: checks if the domain has a dns misconfiguration
# author: @shipcod3
# reference: http://www.securityfocus.com/archive/1/486606 

import sys, socket, time

from colors import *

def dnsMiscon():
    print "[**] Checking localhost."+sys.argv[1]+" for DNS Misconfiguration......"
    
    #resolve the host

    print "[+]Resolving the host address"
    try:
        ip_addr = socket.gethostbyaddr("localhost."+sys.argv[1])
        if ip_addr[0] == "localhost":
            printout('  >> Vulnerable to DNS Misconfiguration which leads to Same-Site Scripting', RED)
    except socket.error:
        printout('  >> Unable to resolve host (not vulnerable)*', GREEN)   
    print "[==] DNS Misconfiguration check finishing......"
    print ""
    time.sleep(3)
