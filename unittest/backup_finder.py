# backup_finder.py
# description: sample for backup file finder
# author: @shipcod3

import sys
import httplib

host = sys.argv[1]
backup_files = ['wp-config.txt', 'wp-config.php~']

for backup_file in backup_files:
    conn = httplib.HTTPConnection(host)
    conn.request('HEAD', '/' + backup_file)

    url = 'http://{0}/{1}'.format(host, backup_file)
    print '    Checking: {0}'.format(url)

    response = conn.getresponse()
    print '    >> ', response.status, response.reason

    conn.close()
    
    if response.status == 200:
        print ("[!] The file '{0}' "
               "could be interesting.").format(backup_file)
