#!/usr/bin/env python
#-*- coding: utf-8 -*-
import requests,logging,time
from concurrent.futures import ThreadPoolExecutor
logging.basicConfig(mode = 'w',level = logging.INFO, format = '%(message)s', filename = "work-proxy.list")




def check(url, proxy):
	proxies = {"http":"http://%s:%s" % (proxy['ip'], proxy['port'])}
	try:
		resp = requests.get(url, timeout = 1, proxies = proxies)
		if resp.status_code == 200:
			logging.info("%s:%s", proxy["ip"], proxy["port"])
	except:
		pass

MAX_WORKERS = 100
SLEEP_SEC = 1
CHECK_URL = "https://www.google.com"
#CHECK_URL = "https://www.baidu.com"
PROXY_FILENAME = "proxy.list"


pool = ThreadPoolExecutor(max_workers = MAX_WORKERS)

proxyfile = open(PROXY_FILENAME)


for proxystr in proxyfile.readlines():

	proxy = proxystr.split(":")
	proxy = {"ip": proxy[0], "port": proxy[1].replace('\n', '')}
	pool.submit(check, CHECK_URL, proxy)



#	time.sleep(SLEEP_SEC)

