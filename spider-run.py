#!/usr/bin/env python
from __future__ import division
import logger, config, time
from spider import Spider,Parser
from api import proxyapi
import threading, requests
from concurrent.futures import ThreadPoolExecutor
import apiserver


def crawing():

    logger.info("crawing start..")
    while True:
        for op in config.spiderConfig:

            urls = op["urls"]
            if isinstance(urls, str):
                urls = [urls]
            
            for url in urls:
                parser = Parser(op["proxyre"], op["ipre"], op["portre"], op["proxyre"])
                spider = Spider(url, parser)

                proxys = spider.getProxys()
                logger.info("crawl proxys %s" % proxys)

                if len(proxys) == 0:
                    logger.warning("crawl error for urls: %s" % op["urls"])

                for proxy in proxys:
                    proxyapi.add(proxy)     
                
        logger.info("next crawing.")
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
            logger.info("check http proxy success: %s" % proxies)
        else:
            logger.info("check http proxy error status: %s" % proxies)
    except Exception as e:
        logger.error("check http proxy except %s: " % proxies)
    finally:
        proxyapi.updatebyid(proxy.id, checkcount = checkcount,
             successrate =  int(successcount * 100 / checkcount),
            successcount = successcount)
        


def checkhttpproxys():
    logger.info("check http proxy list start..")
    pool = ThreadPoolExecutor(32)
    for i in range(0, 64):
        proxy = proxyapi.getrand()
        if proxy == None:
            logger.info("database not exists proxy")
        else:
            pool.submit(checkhttpproxy, proxy, "http://httpbin.org/ip")
        

            


if __name__ == "__main__":

    apiserverthread = threading.Thread(target = apiserver.run)
    apiserverthread.start()

    crawingthread = threading.Thread(target = crawing)
    crawingthread.start()
       
    while True:
        checkthread = threading.Thread(target = checkhttpproxys)
        checkthread.setDaemon(True)
        checkthread.start()
        checkthread.join()
