# helper.py
# description: helper for show function
# author: @semprix

def showhelp():
 print "Available commands:"
 print "show, run,, exploit, search"

def showmods():
 print ""
 print "FortifyTheWeb Modules"
 print "------------------------------------"
 print ""
 print ' Command                                     Author                   Description'
 print ""
 print ' modules/recon/httpheaderanalyzer            httphacker               Checks for vulnerability on http header response'
 print ' modules/recon/subdomainfinder               shipcode                 Harvest domain from the target'
 print ' modules/vulnerability/dnsmisconfig          shipcode                 Check if target is vulnerable to DNS misconfiguration'
 print ' modules/discovery/vhostfinder               medz                     Enumerates vhosts on specified target'
 print ' modules/recon/shodanlookup                  shipcode                 Shodan Host Lookup'
 print ' modules/recon/cmsdetector                   semprix                  Checks if the target is a using a specific CMS'
 print ' modules/vulnerability/heartbleedanalyzer    semprix                  Check the target if vulnerable to heartbleed attack'
 print ' modules/discover/httpmetaextractor          semprix                  Extracts httpmeta data from the target application'
 print ' modules/discovery/backupfilefinder          shipcode                 Fuzz the target for known backup files'
 print ' modules/recon/whoislookup                   semprix                  Performs traditional whois lookup on the target'
 print ""

def showsploits():
 print ""
 print "FortifyTheWeb Exploits"
 print "------------------------------------"
 print ""
 print ' Command                                     Author                   Description'
 print ' modules/exploits/whmcs                      shipcode                 Exploits the local file disclosure vulnerability of WHMCS version 3.x.x'
 print ""

def showcredits():
 print ""
 print "***********************"
 print " FortifyTheWeb Credits"
 print "***********************"
 print "semprix, httphacker, napz, shipcode, medz"
 print ""