# grabheader.py
# description: crawls the URL
# author: @shipcod3

import requests
import time

from bs4 import BeautifulSoup 
from colors import *

def urlcrawler():
    print "[*] Crawling the target"
    req  = requests.get("http://" + sys.argv[1])
	
    data = req.text
    
    soup = BeautifulSoup(data)
    
    for link in soup.find_all('a'):
        print(link.get('href'))
	 
    time.sleep(3)
