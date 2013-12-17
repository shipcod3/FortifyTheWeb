# urlcrawler.py
# description: crawls the URL
# author: @shipcod3

import sys
import requests
import time
import os

sys.path.append(r'auxiliary')
from bs4 import BeautifulSoup 
from colors import *

def urlcrawler():
    print "[**] Starting Spider"
    time.sleep(3)
    if sys.argv[2] == '80':
    	print (' [+] Crawling HTTP')
        print ('    >> Checking if reports folder exist and writable')
        if not os.path.exists(sys.argv[1]):
            print ('        >> Creating reports folder')
            os.makedirs(sys.argv[1])
            os.chdir(sys.argv[1])
            f = open(sys.argv[1] + '.crawl.txt', 'w')
    	req  = requests.get("http://" + sys.argv[1])
    	data = req.text
    	soup = BeautifulSoup(data)
    	for link in soup.find_all('a'):
       		print >> f, (link.get('href'))
        f.close()

    elif sys.argv[2] == '443':
    	print (' [+] Crawling HTTPS')
        print ('    >> Checking if reports folder exist and writable')
        if not os.path.exists(sys.argv[1]):
            print ('        >> Creating reports folder')
            os.makedirs(sys.argv[1])
            os.chdir(sys.argv[1])
            f = open(sys.argv[1] + '.crawl.txt', 'w')
    	req  = requests.get("https://" + sys.argv[1])
    	data = req.text
    	soup = BeautifulSoup(data)
    	for link in soup.find_all('a'):
       		print >> f,(link.get('href'))
        f.close()

    else:
        printout (' [!] Error performing crawl', RED)

	
	time.sleep(3)
