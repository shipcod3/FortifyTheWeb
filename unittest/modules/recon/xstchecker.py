# xstchecker.py
# description: checks if the website is vulnerable to Cross-Site Tracing (XST)
# author: @shipcod3

import sys, httplib

host = raw_input("SET RHOST:")
payload = "<script>alert('TRACE');</script>"

print "[***] Checking: {0} for Cross-Site Tracing \n".format(host)

try:  
    conn = httplib.HTTPConnection(host)
    conn.request("TRACE", "/{0}".format(payload))
    response = conn.getresponse()
    msg = response.read()
    print response.status, response.reason, msg
    
    if response.status == 200 and "<script>alert('TRACE');</script>" in msg:
        print "[!] Vulnerable to Cross-Site Tracing!" 
    else:
        print "[-] Not Vulnerable!"   
except:
    print "[-] Error! Check if host is online..."
