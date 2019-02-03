#!/usr/bin/env python
# coding: utf8
import requests, re, sys
sys.path.append("..")
from api import proxyapi
import logger
def randIP():
    mask8 = int(time.time() % 10)
    mask16 = int(time.time() % 10)
    mask24 = int(time.time() % 10)
    mask32 = int(time.time() % 10)
    return "%s.%s.%s.%s" % (mask8, mask16, mask24, mask32)


def getproxies():
    proxy = proxyapi.getrand()
    if proxy != None:
        httpproxy = "http://%s:%s" % (proxy.ip, proxy.port)
        httpsproxy = "https://%s:%s" % (proxy.ip, proxy.port)
        return {"http": httpproxy, "https": httpsproxy}
     



class Spider:


    def __init__(self, url, parser):
        self._targetUrl = url
        self._parser = parser
        self._proxyText = ''


    def _spider(self):
        HEADERS = {
	        "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
        }

        urls = self._targetUrl
        if isinstance(urls, str):
            urls = [urls]
        proxies = None
        i = 0
        size = len(urls)

        while i < size:
    
            proxies = getproxies()

            try:
                #数据库是否存在proxy 
                if proxies == None:
                    logger.info("datebase not exists proxies.")
                    resp = requests.get(urls[i], headers = HEADERS, timeout = 1)
                else:
                    logger.info("use proxies %s" % proxies)           
                    resp = requests.get(urls[i], headers = HEADERS, timeout = 1, proxies = proxies)

                if resp.status_code == 200:
                    logger.info("成功爬取数据。")
                    self._proxyText = self._proxyText + resp.text
                    i = i + 1
                else:
                    logger.waring("resp.status_code %d" % resp.status_code)

            except Exception as e:
                logger.error(e)
#                logger.exception(e)    
            
                

    def getProxys(self):
        self._spider()
        return self._parser.parse(self._proxyText)
        
