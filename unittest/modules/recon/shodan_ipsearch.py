# shodan_ipsearch.py
# description: looks up the host using Shodan's API
# author: @shipcod3

import shodan
import time 

def shodan_hostlookup():
    #api config here: account.shodan.io
    SHODAN_API_KEY = "uAs67OallytytIdagyHKO1nAWxYetniW"

    try:
        api = shodan.Shodan(SHODAN_API_KEY)
        host = api.host(raw_input("Set Host/IP: "))
        print "\n[**] IP Address: {}".format(host['ip_str'])
        print "[!] ISP: {}".format(host.get('isp', 'n/a'))
        print "[!] Country: {}".format(host.get('country_name', 'n/a'))
        print "[!] Longitude: {}".format(host.get('longitude', 'n/a'))
        print "[!] Longitude: {}".format(host.get('latitude', 'n/a'))
        print "[!] Organization: {}".format(host.get('org', 'n/a'))
        print "[!] Operating System: {}".format(host.get('os', 'n/a'))
        print "[!] Timestamp: {}".format(host.get('timestamp', 'n/a'))
        print "[!!] Printing the port/ports available...."
        time.sleep(1)
       
        for item in host['data']:
            print "[!] Port: {}".format(item['port'])
            print "{}".format(item['data'])
    except Exception, e:
        print 'Error: %s' % e
        sys.exit(1)     
if __name__ == "__main__":
    shodan_hostlookup()
