# Fortify The Web framework
# Web application security testing framework
# ______         _   _  __    _______ _       __          __  _     
#|  ____|       | | (_)/ _|  |__   __| |      \ \        / / | |    
#| |__ ___  _ __| |_ _| |_ _   _| |  | |__   __\ \  /\  / /__| |__  
#|  __/ _ \| '__| __| |  _| | | | |  | '_ \ / _ \ \/  \/ / _ \ '_ \ 
#| | | (_) | |  | |_| | | | |_| | |  | | | |  __/\  /\  /  __/ |_) |
#|_|  \___/|_|   \__|_|_|  \__, |_|  |_| |_|\___| \/  \/ \___|_.__/ 
#                           __/ |                                   
#                          |___/       
#
# description:       FortifyTheWeb Framework core
# author:            @semprix, @shipcod3, @httphacker, @napz, @medz
# platform:          Python
# version:           1.0rc1

# Load python libraries

import cmd, ping, glob, os, time, sys, urllib2, subprocess, socket, ConfigParser, string

from termcolor import colored, cprint
from datetime import datetime
from os import walk

# System Path
sys.path.append(r'helper')
sys.path.append(r'modules/discovery')
sys.path.append(r'modules/recon')
sys.path.append(r'modules/vulnerability')

# Load helper
from helper import *
from banner import *
from greeter import *

# Load modules
from httpheaderanalyzer import *
from subdomainfinder import *
from dnsmisconfig import *

# Configuration directory
config = ConfigParser.ConfigParser()
config.read("config/config.ini")
ftwdir=config.get("path", "ftwdir")

class FortifyTheWebCore(cmd.Cmd):
    banner()
    intro = 'Type show help or show ? to list commands.\n'
    prompt = 'fortifytheweb >'

    # Greeter
    def do_greet(self, line):
        greet()

    ftwmods = ['httpheaderanalyzer', 'subdomainlookup', 'dnsmisconfig']

    # Show commands
    def do_show(self, showopt):
        if showopt == 'modules':
            showmods()
        elif showopt == 'credits':
            showcredits()
        elif showopt == 'help':
            showhelp()
        else:
            print ""
            print "Show options:"
            print "help, modules, credits\n"
    
    # Search function
    def do_search(self, searchopt):
        print "Search function"

    # FortifyTheWeb Modules
    def do_run(self, runopt):
        if runopt == 'httpheaderanalyzer':
            httpheaderanalyzer()
        elif runopt == 'subdomainfinder':
            subdomainfinder()
        elif runopt == 'dnsmisconfig':
            dnsmisconfig()
        else:
            print "[!!!] No module(s) found by that name (this could be a typo)."

    def complete_run(self, text, line, begidx, endidx):
        if not text:
            completions = self.ftwmods[:]
        else:
            completions = [ f
                            for f in self.ftwmods
                            if f.startswith(text)
                            ]
        return completions
    
    def do_shell(self, line):
        output = os.popen(line).read()
        print output
        self.last_output = output

    def do_EOF(self, line):
        return True
    
    def postloop(self):
        print

if __name__ == '__main__':
    FortifyTheWebCore().cmdloop()

## EoF ###