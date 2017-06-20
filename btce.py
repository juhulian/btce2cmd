#!/usr/bin/python2
# -*- coding: utf-8 -*-

import urllib2, json
from time import strftime

def g(c):
    return "{:8.3f}".format(float(json.loads(urllib2.urlopen("https://btc-e.com/api/2/{}/ticker".format(c)).read())['ticker']['last']))

print("btc-e.com{}{}".format(" "*17, strftime("%Y-%m-%d %H:%M:%S")))
print("btc: {} USD  {} EUR".format(g("btc_usd"), g("btc_eur")))
print("ltc: {} USD  {} EUR  {} BTC".format(g("ltc_usd"), g("ltc_eur"), g("ltc_btc")))
print("eth: {} USD  {} EUR  {} BTC".format(g("eth_usd"), g("eth_eur"), g("eth_btc")))
