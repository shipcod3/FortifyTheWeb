# vhostfinder.py
# description: vhost enumeration module for FTW
# author: @medz

import time, urllib, urllib2, json, re, socket, tld, os

from tld import get_tld
from tld.utils import update_tld_names

def vhostfinder():
 
 
    try:
        global ip
        global domain
        domain=raw_input('Set RHOST: ') 
        print '\n'
        ip=socket.gethostbyname(domain)
        query = "ip:"+ip+""
        print '[****] Starting vhost finder......'
        time.sleep (3)
        print ''
        print '['+domain+'] resolves to: ['+ip+']'
        print bing_search(query, 'Web')
        print'[####] Done!!!'
        print ''         
    except:
        print '[!!!!] Error unable to obtain IP of the domain',domain 
        
def bing_search(query, search_type):
    key= 'DQQL52NepCew2q1DwEJdgtd7bfg/lUtwWbSwqjaL04A'
    query = urllib.quote(query)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
    credentials = (':%s' % key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials
    url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$top=50&$format=json'
    request = urllib2.Request(url)
    request.add_header('Authorization', auth)
    request.add_header('User-Agent', user_agent)
    request_opener = urllib2.build_opener()
    response = request_opener.open(request) 
    response_data = response.read()
    json_result = json.loads(response_data)

    
    try:
        for x in range(0, 128):
            aaaa= json_result['d']['results'][x]['Url']
            from urlparse import urlparse
            parsed_uri = urlparse(aaaa)
            domain = '{uri.netloc}'.format(uri=parsed_uri)
            verify_ip=socket.gethostbyname(domain)

            if verify_ip==ip:
#                print verify_ip,ip
                from urlparse import urlparse
                parsed_uri = urlparse(aaaa)
                #domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                domain = '{uri.netloc}'.format(uri=parsed_uri)
                print [x+1],domain    
    except:
        return ''
          
#    try:
#        decoded = json.loads(response_data)
#        res = json.dumps(decoded, sort_keys=True, indent=4) 
#        print res
#    except (ValueError, KeyError, TypeError):
#        print "error occured"
 
if __name__ == "__main__":
    main()

