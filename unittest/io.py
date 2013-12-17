# io.py
# description: input / output unittesting
# author: @semprix

import os
import sys

print ('Create me file and directory')
if not os.path.exists(sys.argv[1]):
    os.makedirs(sys.argv[1])
    os.chdir(sys.argv[1])
f = open(sys.argv[1] + '.txt', 'w')
print >> f, 'Filename:', sys.argv[1]  # or f.write('...\n')
f.close()