# backup_finder.py
# description: finds PHP backup files for known CMS
# author: @shipcod3

import sys
import urllib2, re
from urllib2 import URLError

host = sys.argv[1]
payload = open("payloads.txt")

for backup_files in payload.readlines():
    
    url = "http://{0}/{1}".format(host, backup_files)
    print "    Checking: {0}".format(url)
    try: 
        response = urllib2.urlopen(url)
        msg = response.read()
        status_code = response.getcode()
        print ">> ", status_code
        
        if status_code == 200 and '<?php' in msg:
            print ("[!] This page could be interesting.")         
    except URLError, e:
        print ">> ", e.code
