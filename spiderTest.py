#!/usr/bin/env python
import loginit, logging
from spider import Spider,Parser





proxyre = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,4}'
ipre = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
portre = [':\d{2,5}', '\d{2,5}']
prore = ''

urls = ["https://www.my-proxy.com/free-proxy-list-1.html",
"https://www.my-proxy.com/free-proxy-list-2.html",
"https://www.my-proxy.com/free-proxy-list-3.html",
"https://www.my-proxy.com/free-proxy-list-4.html",
"https://www.my-proxy.com/free-proxy-list-5.html",
"https://www.my-proxy.com/free-proxy-list-6.html",
"https://www.my-proxy.com/free-proxy-list-7.html",
"https://www.my-proxy.com/free-proxy-list-8.html",
"https://www.my-proxy.com/free-proxy-list-9.html",
"https://www.my-proxy.com/free-proxy-list-10.html"]

#https://www.proxydocker.com/en/proxylist/port/808
#urls = "https://www.my-proxy.com/free-proxy-list-10.html"
parser = Parser(proxyre, ipre, portre, proxyre)
spider = Spider(urls, parser)
proxys = spider.getProxys()
# Proxys

print("---proxy list---")
for proxy in proxys:
    logging.info("%s %s", proxy.ip, proxy.port)




