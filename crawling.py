#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Author: Thiago(THX)
# Github: gothub.com/thxsena
# Modo de uso: python crawling.py http://www.site.com
#

from bs4 import BeautifulSoup
import requests
import sys


print ('''

╔═╗ ┬─┐ ┌─┐ ┬ ┬ ┬   ┬ ┌┐┌ ┌─┐
║   ├┬┘ ├─┤ │││ │   │ │││ │ ┬
╚═╝ ┴└─ ┴ ┴ └┴┘ ┴─┘ ┴ ┘└┘ └─┘
     -Author:Thiago(THX)-

''')

try:
    
    host = sys.argv[1]

    def web():
        if 'http' not in host:
            r = requests.get('http://'+host)
            go = r.status_code
            if go == 200:
                   ta = r.text
                   soup = BeautifulSoup(ta, "lxml")
                   for link in soup.find_all('a'):
                       print('[+]URL: '+link.get('href'))
    web()

except:
  print('[-]URL NOT FOUND: '+host)
