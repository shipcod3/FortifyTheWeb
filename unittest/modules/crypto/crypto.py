# crypto.py
# description: implementation of hash library
# author: @semprix

import hashlib

hashtxt = hashlib.sha224("Who reads my hash").hexdigest()
print hashtxt