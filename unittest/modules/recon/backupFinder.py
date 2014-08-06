# backup_finder.py
# description: sample for backup file finder
# author: @shipcod3

import sys
import httplib

host = sys.argv[1]
backup_files = [
                'wp-config.php-',
                'wp-config.php.bak',
                'wp-config.php.save',
                'wp-config.php.swp',
                'wp-config.php.swo',
                'wp-config.php.conf',
                'wp-config.php.old',
                'wp-config.txt', 
                'wp-config.php~',
                'config.php-',
                'config.php.bak',
                'config.php.save',
                'config.php.swp',
                'config.php.swo',
                'config.php.conf',
                'config.php.old',
                'config.txt',
                'config.php~',
               ]

for backup_file in backup_files:
    conn = httplib.HTTPConnection(host)
    conn.request('GET', '/' + backup_file)

    url = 'http://{0}/{1}'.format(host, backup_file)
    print '    Checking: {0}'.format(url)

    response = conn.getresponse()
    print '    >> ', response.status, response.reason
    
    msg = response.read()

    conn.close()
    
    if response.status == 200 and '<?php' in msg:
        print ("[!] The file '{0}' "
               "could be interesting.").format(backup_file)
