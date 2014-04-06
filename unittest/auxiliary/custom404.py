import re
import requests

def convertheaders(headers):
	"""Convert headers from dictionary to multiline string"""
	responseheaders = ""
	for key in headers:
		#There will be a minor 'issue' here. If there are multiple
		#set-cookie headers, they will be treated as a one liner only
		#due to how the requests library works. Fix for that will depend
		#on how this will be integrated with the core and other modules, 
		#if such a fix is necessary.
		responseheaders += key + ": " + headers[key] + "\n"
	return responseheaders

def checkcustom404(r,regex):
	"""Check response for custom404 signature"""
	if type(r) == requests.models.Response:
		is_valid = False
		try:
			re.compile(regex)
			is_valid = True
		except re.error:
			print "Invalid regex detected. Program will skip testing with this regex: %s" % regex
			return False	
		if is_valid: 
			mheader = re.search(regex, convertheaders(r.headers), flags=re.IGNORECASE)
			mbody = re.search(regex, r.text, flags=re.IGNORECASE)
			if mheader or mbody:
				return True
			else:
				return False

def checkcustom404s(r, regexlist):
	"""Calls checkcustom404 function for each custom404 signature in list"""
	valid = False
	if type(r) == requests.models.Response and type(regexlist) == list:
		for regex in regexlist:
			valid |= checkcustom404(r , regex)
			if valid:
				break;
		return valid

#Basic Usage
#The functions defined above are meant to be use with requests library.
#A value of True indicates a custom404 signature is detected in the response.

#Sample Usage
#You may run this python code as is.
custom404 = [ "<span>Homer</span>", "<span>Homera</span>", "[", "<span>Homeraaaaa</span>", "<span>Home</span>"]
r = requests.get('http://www.nestle.com')
print checkcustom404s(r,custom404)
