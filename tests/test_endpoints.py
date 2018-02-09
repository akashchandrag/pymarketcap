#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from random import choice
from urllib.request import urlopen
from tqdm import tqdm

import pytest

from pymarketcap import Pymarketcap
pym = Pymarketcap()

coin = choice(pym.coins)
exchange = choice(pym.exchange_slugs)

endpoints = [
    ("_cache_symbols",     "https://files.coinmarketcap.com/generated/search/quick_search.json"),
    ("ticker",            ["https://api.coinmarketcap.com/v1/ticker/",
                           "https://api.coinmarketcap.com/v1/ticker/%s" % coin]),
    ("markets",            "https://coinmarketcap.com/currencies/%s/" % coin),
    ("ranks",              "https://coinmarketcap.com/gainers-losers/"),
    ("historical",         "https://coinmarketcap.com/currencies/%s/historical-data/" % coin),
    ("recently",           "https://coinmarketcap.com/new/"),
    ("exchange",           "https://coinmarketcap.com/exchanges/%s/" % exchange),
    ("exchanges",          "https://coinmarketcap.com/exchanges/volume/24-hour/all/"),
    ("tokens",             "https://coinmarketcap.com/tokens/views/all/"),
    ("graphs.currency",    "https://graphs2.coinmarketcap.com/currencies/%s/" % coin),
    ("graphs.global_cap", ["https://graphs2.coinmarketcap.com/global/marketcap-total/",
                           "https://graphs2.coinmarketcap.com/global/marketcap-altcoin/"]),
    ("graphs.dominance",   "https://graphs2.coinmarketcap.com/global/dominance/"),
]

def assert_up(ep):
    req = urlopen(ep)
    assert req.getcode() != 404
    req.close()

def test_endpoints():
    for method, eps in tqdm(endpoints):
        if type(eps) != list:
            eps = [eps]
        for ep in eps:
            tqdm.write("%18s() --> %s" % (method, ep))
            assert_up(ep)
            time.sleep(2)
