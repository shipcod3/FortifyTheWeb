# metaextractor.py
# description: extracts metadata from target website
# author: @semprix

import ping, time, sys, urllib2, subprocess, socket, ConfigParser, string

from urllib import urlopen
from lxml import etree

f = urlopen (sys.argv[1]).read()
tree = etree.HTML( f )
extractor = tree.xpath( "//meta" )
for i in extractor:
  print etree.tostring( i )
