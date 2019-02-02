#!/usr/bin/env python
from __future__ import division
import loginit, logging, config, time
from spider import Spider,Parser
from api import proxyapi
import threading, requests
from concurrent.futures import ThreadPoolExecutor


def crawing():

    logging.info("crawing start..")
    while True:
        for op in config.spiderConfig:
            parser = Parser(op["proxyre"], op["ipre"], op["portre"], op["proxyre"])
            spider = Spider(op["urls"], parser)

            proxys = spider.getProxys()
            
            for proxy in proxys:
                proxyapi.add(proxy)     
            
        logging.info("next crawing.")
        time.sleep(60 * 10)



def checkhttpproxy(proxy, targeturl):

    proxies = {
        "http": "http://%s:%s" % (proxy.ip, proxy.port),
        "https": "https://%s:%s" % (proxy.ip, proxy.port),
    }
    
    
    checkcount = proxy.checkcount + 1
    successcount = proxy.successcount    

    try:
        resp = requests.get(targeturl, timeout = 1, proxies = proxies)
        if resp.status_code == 200:
            successcount += 1
            logging.info("check http proxy success: %s" % proxies)
        else:
            logging.info("check http proxy error status: %s" % proxies)
    except Exception as e:
        logging.debug("check http proxy except %s: " % proxies)
    finally:
        proxyapi.updatebyid(proxy.id, checkcount = checkcount,
             successrate =  int(successcount * 100 / checkcount),
            successcount = successcount)
        


def checkhttpproxys():
    logging.info("check http proxy list start..")
    pool = ThreadPoolExecutor(32)
    while True:
        proxy = proxyapi.getrand()
        if proxy == None:
            logging.info("database not exists proxy")
        else:
            pool.submit(checkhttpproxy, proxy, "http://httpbin.org/ip")

            


if __name__ == "__main__":
    crawingthread = threading.Thread(target = crawing)
    checkthread = threading.Thread(target = checkhttpproxys)
    crawingthread.start()
    checkthread.start()
