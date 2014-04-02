#!/usr/bin/python
import urllib2
def basicauthhandler(target, username, password):
	"""Returns a Basic Authentication Handler based on the given arguments"""
	auth = urllib2.HTTPPasswordMgrWithDefaultRealm()
	auth.add_password(None, target, username, password)
	return urllib2.HTTPBasicAuthHandler(auth)

def proxyhandler(proxy, port):
	"""Returns a Proxy Handler based on the given arguments"""
	return urllib2.ProxyHandler({'http': 'http://'+proxy+':'+port+'/'})

#Basic Usage 
#Call the necessary handler creation functions first, then pass the returned objects to build_opener function to create opener
#Pass the opener object to install_opener function, and all subsequent calls made by urlopen will use the defined settings 
#
#handle1 = basicauthhandler('www.example.com', 'foo','bar')
#handle2 = proxyhandler('www.proxy.com', 8080)
#opener =  urllib2.build_opener(handle1, handle2, ...)
#urllib2.install_opener(opener)
#output = urllib2.urlopen(target)
#do_something(output)

#Sample Usage 
#You may run this file as is, make sure to use Burp and bind listener port to 8080 for this sample code
opener = urllib2.build_opener(basicauthhandler('natas0.natas.labs.overthewire.org','natas0','natas0'),proxyhandler('127.0.0.1','8080'))
urllib2.install_opener(opener)
output = urllib2.urlopen('http://natas0.natas.labs.overthewire.org')
print output.getcode()
