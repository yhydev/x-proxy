#!/usr/bin/env python
import loginit, logging, config
from spider import Spider,Parser
from concurrent.futures import ThreadPoolExecutor


MAX_WORKERS = 30

pool = ThreadPoolExecutor(max_workers = MAX_WORKERS)

for op in config.spiderConfig:
    parser = Parser(op["proxyre"], op["ipre"], op["portre"], op["proxyre"])
    spider = Spider(op["urls"], parser)
    #proxys = spider.getProxys()

    proxys = pool.submit(spider.getProxys).result()

    for proxy in proxys:
        logging.info("%s:%s", proxy.ip, proxy.port)
            
