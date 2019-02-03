from api import proxyapi
from model import Proxy
import logging

if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO)
    pfile = open("work-proxy.list")

    proxystr = pfile.readline()
    while proxystr:
        proxyarr = proxystr.split(':')
        proxy = Proxy(ip = proxyarr[0], port = proxyarr[1].replace('\n',''))
        proxyapi.add(proxy)
        proxystr = pfile.readline()

        
