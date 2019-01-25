#!/usr/bin/env python
import loginit, logging, config
from spider import Spider,Parser





for op in config.spiderConfig:
    parser = Parser(op["proxyre"], op["ipre"], op["portre"], op["proxyre"])
    spider = Spider(op["urls"], parser)
    proxys = spider.getProxys()

    for proxy in proxys:
        logging.info("%s:%s", proxy.ip, proxy.port)
            
