#!/usr/bin/env python
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
sys.path.append(r'modules/vulnerability')
sys.path.append(r'modules/discovery')
sys.path.append(r'modules/recon')
sys.path.append(r'modules/exploits')

# Load helper
from helper import *
from banner import *
from greeter import *

# Load modules
from httpheaderanalyzer import *
from subdomainfinder import *
from dnsmisconfig import *
from vhostfinder import *
from shodanlookup import *

# Load exploits
from whmcs import *

# Configuration directory
config = ConfigParser.ConfigParser()
config.read("config/config.ini")
ftwdir=config.get("path", "ftwdir")

class FortifyTheWebCore(cmd.Cmd):
    banner()
    intro = 'Type show help or show ? to list commands.\n'
    prompt = 'fortifytheweb >'

    ftwmods = ['httpheaderanalyzer', 'subdomainlookup', 'dnsmisconfig']

    # Show commands
    def do_show(self, showopt):
        """\n* Show command will list down all available modules and exploits, format: show <modules> <exploits>\n"""
        if showopt == 'modules':
            showmods()
        elif showopt == 'exploits':
            showsploits()
        elif showopt == 'credits':
            showcredits()
        else:
            print ""
            print "Show options:"
            print "help, modules, credits\n"
    
    # Search function
    def do_search(self, searchopt):
        """\n* Search within the FortifyTheWeb Core, format: search <string>\n"""
        print "Search function"

    # FortifyTheWeb Modules
    def do_run(self, runopt):
        """\n* Run command will execute the specified module, format: run <module_name>\n"""
        if runopt == 'modules/recon/httpheaderanalyzer':
            httpheaderanalyzer()
        elif runopt == 'modules/recon/subdomainfinder':
            subdomainfinder()
        elif runopt == 'modules/vulnerability/dnsmisconfig':
            dnsmisconfig()
        elif runopt == 'modules/discovery/vhostfinder':
            vhostfinder()
        elif runopt == 'modules/recon/shodanlookup':
            shodanlookup()
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
    
    # FortifyTheWeb Exploits
    def do_exploit(self,exploitopt):
        """\n* Exploit command will execute the specified exploit, format: exploit <exploit_name>\n"""
        if exploitopt == 'modules/exploits/whmcs':
            whmcs()
        else:
            print "[!!!] No exploit(s) found by that name (this could be a typo)."

    def do_shell(self, line):
        """\n* Shell command will allow you to issue a FTWCore external command, format: shell <command>\n"""
        output = os.popen(line).read()
        print output
        self.last_output = output

    def do_quit(self,*args):
        """\n* Quit command will shutdown the application cleanly, format: quit\n"""
        print '[!!!] Shutting down......'
        time.sleep(3)
        print '[!!!] Good bye......'
        return True    

    def do_EOF(self, line):
        return True
    
    def postloop(self):
        print

if __name__ == '__main__':
    FortifyTheWebCore().cmdloop()

## EoF ###
