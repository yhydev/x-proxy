#!/usr/bin/env python
import re, logging 
from .xparser import *
import sys
sys.path.append("..")
from model import Proxy
class Parser:
    
    def __init__(self, proxyre, ipre, portre, protocolre):
        self._proxyre = proxyre
        self._ipre = ipre
        self._portre = portre
        self._protocolre = protocolre

    def parse(self, text):


        matchlist = re.findall(self._proxyre, text)
        proxylist = []
        strtype = type('')
        listtype = type([])
         
        for proxystr in matchlist:
            
            ip = findone(self._ipre, proxystr)
            port = findone(self._portre, proxystr)
            proto = findone(self._protocolre, proxystr)
            proxy = Proxy(ip = ip, port = port)
            proxylist.append(proxy)
            logging.debug("parser.parse %s" % proxy)
        return proxylist
