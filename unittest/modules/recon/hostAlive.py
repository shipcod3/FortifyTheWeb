# hostalive.py
# description: check if host is alive, integrated to core stage 1
# author: @semprix

import subprocess
import shlex
import sys

command_line = "ping -c 1 " + sys.argv[1]

try:
      subprocess.check_call(command_line,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
      print "Website is there."
except subprocess.CalledProcessError:
      print "Couldn't get a ping."