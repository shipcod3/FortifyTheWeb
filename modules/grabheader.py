import sys
import urllib2

def grabheader():
	print "[*] Performing header analysis"
	response = urllib2.urlopen('http://' + sys.argv[1])
	grabheadresp = response.info().getheader('version')
	if grabheadresp is None:
		print "\033[91m>> Failed to get header value\033[0m"
	else:
		print "Display"
 	response.close()  