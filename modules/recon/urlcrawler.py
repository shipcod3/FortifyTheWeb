# urlcrawler.py
# description: crawls the URL
# author: @shipcod3

import sys
import requests
import time

sys.path.append(r'auxiliary')
from bs4 import BeautifulSoup 
from colors import *

def urlcrawler():
    print "[**] Starting Spider"
    time.sleep(3)
    if sys.argv[2] == '80':
    	print (' [+] Crawling HTTP')
    	req  = requests.get("http://" + sys.argv[1])
    	data = req.text
    	soup = BeautifulSoup(data)
    	for link in soup.find_all('a'):
       		print(link.get('href'))

    elif sys.argv[2] == '443':
    	print (' [+] Crawling HTTPS')
    	req  = requests.get("https://" + sys.argv[1])
    	data = req.text
    	soup = BeautifulSoup(data)
    	for link in soup.find_all('a'):
       		print(link.get('href'))

    else:
        printout (' [!] Error performing crawl', RED)

	
	time.sleep(3)
