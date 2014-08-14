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
 print ' Command                       Location                                                  Author                   Description'
 print ""
 print ' httpheaderanalyzer            modules/recon/httpheaderanalyzer                          httphacker               Checks for vulnerability on http header response'
 print ' subdomainfinder               modules/discovery/subdomainfinder                         shipcode                 Harvest domain from the target'
 print ' dnsmisconfig                  modules/vulnerability/dnsmisconfig                        shipcode                 Check if target is vulnerable to DNS misconfiguration'
 print ' CMS detector                  modules/recon/cmsdetector                                 semprix                  Checks if the target is a using a specific CMS'
 print ' Heartbleed Analyser           modules/vulnerability/heartbleedanalyzer                  semprix                  Check the target if vulnerable to heartbleed attack'
 print ' HTTP MetaExtractor            modules/discover/httpmetaextractor                        semprix                  Extracts httpmeta data from the target application'
 print ' Backup file finder            modules/discovery/backupfilefinder                        shipcode                 Fuzz the target for known backup files'
 print ' Whois Lookup                  modules/recon/whoislookup                                 semprix                  Performs traditional whois lookup on the target'
 print ""

def showsploits():
 print ""
 print "FortifyTheWeb Exploits"
 print "------------------------------------"
 print ""
 print ' whmcs                         modules/exploits/whmcs                                    shipcode                 Exploits the local file disclosure vulnerability of WHMCS version 3.x.x'
 print ""

def showcredits():
 print ""
 print "***********************"
 print " FortifyTheWeb Credits"
 print "***********************"
 print "semprix, httphacker, napz, shipcode, medz"
 print ""