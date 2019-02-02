#!/usr/bin/env python
# coding: utf8
import requests, logging, re, sys
sys.path.append("..")
from api import proxyapi

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
        #代理是否有效，有效则不用获取新的代理
        proxyflag = False
        proxies = None
        i = 0
        size = len(urls)

        while i < size:
    
            if not proxyflag:
                proxies = getproxies()

            try:
                #数据库是否存在proxy 
                if proxies == None:
                    logging.info("datebase not exists proxies.")
                    resp = requests.get(urls[i], headers = HEADERS, timeout = 0.4)
                else:
                    logging.info("use proxies %s" % proxies)           
                    resp = requests.get(urls[i], headers = HEADERS, timeout = 0.4, proxies = proxies)

                if resp.status_code == 200:
                    logging.info("成功爬取数据。")
                    proxyflag = True
                    self._proxyText = self._proxyText + resp.text
                    i = i + 1
                else:
                    logging.waring("resp.status_code %d" % resp.status_code)
                    proxyflag = False

            except Exception as e:
                logging.error(e)
#                logging.exception(e)    
                proxyflag = False
            
                

    def getProxys(self):
        self._spider()
        logging.debug(self._proxyText)
        return self._parser.parse(self._proxyText)
        
