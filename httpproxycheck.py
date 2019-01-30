#!/usr/bin/env python
#-*- coding: utf-8 -*-
import requests,logging,time
from concurrent.futures import ThreadPoolExecutor
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
PROXY_FILENAME = "proxy.list"


pool = ThreadPoolExecutor(max_workers = MAX_WORKERS)

proxyfile = open(PROXY_FILENAME)


for proxystr in proxyfile.readlines():

	proxy = proxystr.split(":")
	proxy = {"ip": proxy[0], "port": proxy[1].replace('\n', '')}
	pool.submit(check, CHECK_URL, proxy)



#	time.sleep(SLEEP_SEC)

