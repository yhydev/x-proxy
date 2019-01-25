#!/usr/bin/env python

import requests, logging
from .commtype import *


class Spider:

    def __init__(self, url, parser):
        self._targetUrl = url
        self._parser = parser
        self._proxyText = ''
    pass


    def _spider(self):
        urls = self._targetUrl
        url_t = type(self._targetUrl)
        if url_t == strtype:
            urls = [urls]
    
        for url in urls:
            try:
                resp = requests.get(url, headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}, timeout = 3)
                if resp.status_code == 200:
                    self._proxyText = self._proxyText + resp.text

            except Exception as e:
                logging.error("Can't access:%s",url)
                

    def getProxys(self):
        self._spider()
        logging.debug(self._proxyText)
        return self._parser.parse(self._proxyText)
        
        

