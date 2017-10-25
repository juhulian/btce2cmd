#!/usr/bin/python2
# -*- coding: utf-8 -*-

import urllib2, json
from time import strftime

def g(c):
    return float(json.loads(urllib2.urlopen("https://wex.nz/api/2/{}/ticker".format(c)).read())['ticker']['last'])

print("wex.nz{}{}".format(" "*20, strftime("%Y-%m-%d %H:%M:%S")))
print("btc: {:8.3f} USD  {:8.3f} EUR".format(g("btc_usd"), g("btc_eur")))
print("ltc: {:8.3f} USD  {:8.3f} EUR  {:8.3f} BTC".format(g("ltc_usd"), g("ltc_eur"), g("ltc_btc")))
print("eth: {:8.3f} USD  {:8.3f} EUR  {:8.3f} BTC".format(g("eth_usd"), g("eth_eur"), g("eth_btc")))
