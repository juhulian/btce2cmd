#!/usr/bin/python2
# -*- coding: utf-8 -*-

import urllib2, json
from time import strftime


try:
    d = json.loads(urllib2.urlopen("https://api.litebit.eu/markets").read())["result"]
    print("EUR buy     sell   {}".format(strftime("%Y-%m-%d %H:%M:%S")))
    for c in ["btc", "bcc", "eth", "etc", "ltc", "xem"]:
        print("{} {:07.2f} {:07.2f}".format(c, d[c]["buy"], d[c]["sell"]))
except Exception as err:
    print(err)
