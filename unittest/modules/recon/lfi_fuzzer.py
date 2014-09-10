# lfi_fuzzer.py
# description: a simple website lfi scanner / fuzzer
# author: @shipcod3

import sys
import urllib2, re
from urllib2 import URLError
import time

host = sys.argv[1] 
payloads = open("../../../lfi_payloads.txt") # lfi payload
print "Scanning the target: {0}".format(host)
time.sleep(1)

for payload in payloads.readlines():
    
    url = "http://{0}{1}".format(host, payload) # sample target: example.com/lol/index.php?program= 
    
    try: 
        response = urllib2.urlopen(url)
        msg = response.read()
        status_code = response.getcode()
        
        if status_code == 200 and 'root:x:' in msg:
            print "[*] Payload found"
            print ">> POC: {0}".format(url) +"[!] Vulnerable to Local File Inclusion"
            sys.exit(1)
            
    except URLError, e:
        print ">> ", e.code
