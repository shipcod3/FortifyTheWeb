# dirfinder.py
# description: brute folder discovery
# author: @napz
import sys, requests, time


host = sys.argv[1]
file_list = sys.argv[2]

file = open(file_list)

for line in file.xreadlines():
    if not line.startswith("#"):
        folder = requests.get(host+line.rstrip('\r\n'), verify=False)
        print host+line.rstrip('\r\n')
        if folder.status_code != 404:
            print host+line.rstrip('\r\n')+"------"+str(folder.status_code)
            time.sleep(1)
