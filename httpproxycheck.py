#!/usr/bin/env python
#-*- coding: utf-8 -*-
import requests,logging,time
from concurrent.futures import ThreadPoolExecutor
from api import proxyapi
logging.basicConfig(level = logging.INFO, format = '%(message)s', filename = "work-proxy.list", filemode = "w")


headers = {
	"user-agent":"Chrome WebKit"
}

def check(url, proxy):
	proxies = {"http":"http://%s:%s" % (proxy['ip'], proxy['port'])}
	try:
		resp = requests.get(url, timeout = 1, proxies = proxies, headers = headers)
		if resp.status_code == 200:
			logging.info("%s:%s", proxy["ip"], proxy["port"])
	except:
		pass

MAX_WORKERS = 100
SLEEP_SEC = 1
#CHECK_URL = "http://www.google.com"
#CHECK_URL = "https://www.baidu.com/s?wd=test"
CHECK_URL = "http://www.httpbin.org/ip"


pool = ThreadPoolExecutor(max_workers = MAX_WORKERS)


offset = 0
limit = 100
while True:

    proxys = proxyapi.query(offset, limit)
    for proxy in proxys:
	    pool.submit(check, CHECK_URL, proxy) 

    if len(proxys) != limit:
        offset = 0
    else
        offset = offset + limit

