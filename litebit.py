#!/usr/bin/python2
# -*- coding: utf-8 -*-

import urllib2, json
from time import strftime

url = "https://api.litebit.eu/markets"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
       #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       #'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       #'Accept-Encoding': 'none',
       #'Accept-Language': 'en-US,en;q=0.8',
       #'Connection': 'keep-alive'}

req = urllib2.Request(url, headers=hdr)

try:
    res = json.loads(urllib2.urlopen(req).read())["result"]
except urllib2.HTTPError, e:
    print e.fp.read()
else:
    print("EUR buy     sell   {}".format(strftime("%Y-%m-%d %H:%M:%S")))
    for c in ["btc", "bcc", "eth", "etc", "ltc", "xem"]:
        print("{} {:07.2f} {:07.2f}".format(c, res[c]["buy"], res[c]["sell"]))
