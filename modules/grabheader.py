# Grab header for FTW framework
# Author: @semprix

import sys
import urllib2
import time

def grabheader():
	print "[*] Performing header analysis"
	response = urllib2.urlopen('http://' + sys.argv[1])
	grabserver = response.info().getheader('server')
	print " [+] Grabbing web server version"
	if grabserver is None:
		print " \033[91m>> Failed to get header value *not vulnerable*\033[0m"
	else:
		print " \033[92m>> " + grabserver + "\033[0m"

	grabplatform = response.info().getheader('x-powered-by')
	print " [+] Grabbing platform \033[0m"
	if grabplatform is None:
		print " \033[91m>> No response from server\033[0m"
	else:
		print " \033[92m>> " + grabplatform + "\033[0m"

	grabcontent = response.info().getheader('content-type')
	print " [+] Grabbing content type \033[0m"
	if grabcontent is None:
		print " \033[91m>> Failed to get header value *not vulnerable*\033[0m"
	else:
		print " \033[92m>> " + grabcontent + "\033[0m"
	grabframeopt = response.info().getheader('x-frame-options')
	print " [+] Grabbing x-frame-options \033[0m"
	if grabframeopt is None:
		print " \033[91m>> No x-frame-options *vulnerability to click-jacking is possible*\033[0m"
	else:
		print " \033[92m>> " + grabframeopt + "\033[0m"
	grabxssprotect = response.info().getheader('x-xss-protection')
	print " [+] Grabbing x-xss-protection \033[0m"
	if grabframeopt is None:
		print " \033[91m>> No XSS protection *vulnerability to XSS is possible*\033[0m"
	else:
		print " \033[92m>> " + grabframeopt + "\033[0m"
	
 	response.close()  
 	time.sleep(3)


