# grabheader.py
# description: HTTP Header Analyzer forked by httphacker
# author: @semprix

import sys, urllib2, time

def httpheaderanalyzer():
	print 'Set RHOST:',
	rhost = raw_input()
	print 'Set RPORT:',
	rport = raw_input()
	print ""
	print "[****] Starting header analysis......"
	print ""
	response = urllib2.urlopen('http://' + rhost)

	# Server header settings

	grabserver = response.info().getheader('server')
	print " [+] Grabbing web server version"
	time.sleep(2)
	if grabserver is None:
		print ' >> Failed to get header value *not vulnerable*'
	else:
		print ' >> ' + grabserver

	grabplatform = response.info().getheader('x-powered-by')
	print " [+] Grabbing platform "
	time.sleep(2)
	if grabplatform is None:
		print ' >> No response from server'
	else:
		print ' >> ' + grabplatform

	grabcontent = response.info().getheader('content-type')
	print " [+] Grabbing content type "
	time.sleep(2)
	if grabcontent is None:
		print ' >> Failed to get header value *not vulnerable*'
	else:
		print ' >> ' + grabcontent

	 # Server header security settings
	
	 # Check if this is an SSL port

	if rport == '443':
		print " [+] Grabbing SSL header settings "
		time.sleep(2)
		grabhsts = response.info().getheader('Strict-Transport-Security')
		if grabhsts is None:
			print ' >>  No HSTS Policy *vulnerable*'
		else:
			print ' >> ' + grabhsts + ' *flag found (not vulnerable)*'
		
	else:
		print "[!] Target not using SSL, proceed with http..."
		time.sleep(3)

	grabframeopt = response.info().getheader('x-frame-options')
	print " [+] Grabbing x-frame-options "
	time.sleep(2)
	if grabframeopt is None:
		print ' >>  No x-frame-options *vulnerable to click-jacking possible*'
	else:
		print' >> ' + grabframeopt + ' *flag found (not vulnerable)*'
	
	grabxssprotect = response.info().getheader('x-xss-protection')
	print " [+] Grabbing x-xss-protection "
	time.sleep(2)
	if grabframeopt is None:
		print ' >> No XSS protection *vulnerable to XSS possible*'
	else:
		print ' >> ' + grabframeopt + ' *flag found (not vulnerable)*'
	
	grabxcontent = response.info().getheader('x-content-type-options')
	print " [+] Grabbing x-content-type-options"
	time.sleep(2)
	if grabxcontent is None:
		print ' >> No x-content-type-options *vulnerable to MIME sniffing possible*'
 	else:
		print ' >> ' + grabxcontent + ' *flag found (not vulnerable)*'

 	response.close() 
 	print ""
	print'[####] Done!!!'
	print ""
 	time.sleep(3)


