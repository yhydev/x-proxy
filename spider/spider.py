#!/usr/bin/env python
# coding: utf8
import requests, logging, re


class Proxys:
	
    def __init__(self, filename):
        self.__filename = filename
        self.__proxyfile = open(filename)
	
    def get(self):
        proxy = self.__proxyfile.readline().replace('\n','')
        if (proxy) < 3:
            self.__proxyfile = open(self.__filename)
            proxy = self.__proxyfile.readline().replace('\n','')

        if re.match('\d{1,3}\.\d{1,3}', proxy):
            return proxy
        return self.get()




def randIP():
    mask8 = int(time.time() % 10)
    mask16 = int(time.time() % 10)
    mask24 = int(time.time() % 10)
    mask32 = int(time.time() % 10)
    return "%s.%s.%s.%s" % (mask8, mask16, mask24, mask32)



class Spider:


    proxys = Proxys("proxy.list")
    


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
        proxies = {} 
        i = 0
        size = len(urls)

        while i < size: 
            try:
                if not proxyflag:
                    proxy = proxys.get()
                    httpproxy = "http://%s" % proxy
                    httpsproxy = "https://%s" % proxy
                    proxies = {"http": httpproxy, "https": httpsproxy}
                
                logging.info(proxies)

#                HEADERS["x-forwarded-for"] = 
                resp = requests.get(urls[i], headers = HEADERS, timeout = 0.4, proxies = proxies)

#                resp = requests.get(urls[i], headers = HEADERS, timeout = 0.4)
                if resp.status_code == 200:
                    proxyflag = True
                    self._proxyText = self._proxyText + resp.text
                    i = i + 1
                else:
                    logging.waring("resp.status_code %d", resp.status_code)
                    proxyflag = False

            except Exception as e:
                logging.debug(e)    
                proxyflag = False
            
                

    def getProxys(self):
        self._spider()
        logging.debug(self._proxyText)
        return self._parser.parse(self._proxyText)
        
        
if __name__ == "__main__":
	logging.basicConfig(level = logging.DEBUG)
	proxys = Proxys("proxy.list")
	logging.debug(proxys.get())
	logging.debug(proxys.get())
