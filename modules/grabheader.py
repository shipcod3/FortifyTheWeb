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
	grabcontent = response.info().getheader('Content-type')
	print " [+] Grabbing content type version\033[0m"
	if grabcontent is None:
		print " \033[91m>> Failed to get header value *not vulnerable*\033[0m"
	else:
		print " \033[92m>> " + grabcontent + "\033[0m"
 	response.close()  
 	time.sleep(3)