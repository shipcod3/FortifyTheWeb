# urlcrawler.py
# description: crawls the URL
# author: @shipcod3

import sys, requests, time, os

from bs4 import BeautifulSoup 

def urlcrawler():
    print ""
    print "[**] Starting Spider......"
    time.sleep(3)
    if sys.argv[2] == '80':
    	print (' [+] Crawling unauthenticated HTTP')
        print ('    >> Checking if client folder exist and writable')
        if not os.path.exists(sys.argv[1]):
            print ('    >> Creating client folder')
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
    	print (' [+] Crawling unauthenticated HTTPS')
        print ('    >> Checking if client folder exist and writable')
        if not os.path.exists(sys.argv[1]):
            print ('    >> Creating client folder')
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

    print'[==] Crawl finishing...'
time.sleep(3)
