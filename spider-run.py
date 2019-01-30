#!/usr/bin/env python
import loginit, logging, config, time
from spider import Spider,Parser
from concurrent.futures import ThreadPoolExecutor


MAX_WORKERS = 8 

proxyfile = open("proxy.list", "a")

while True:
    for op in config.spiderConfig:
        parser = Parser(op["proxyre"], op["ipre"], op["portre"], op["proxyre"])
        spider = Spider(op["urls"], parser)

        proxys = spider.getProxys()

        for proxy in proxys:
            proxyfile.write("%s:%s\n" % (proxy.ip, proxy.port))
            logging.debug("add new proxy.")
    
    logging.debug("readly next spiders.")
    time.sleep(60 * 10)
