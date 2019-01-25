#!/usr/bin/env python
import re, ReParser, logging 
from proxy import Proxy
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
            
            logging.debug('proxy match: %s' % proxystr)
            ip = ReParser.findone(self._ipre, proxystr)
            logging.debug('ip match: %s' % ip)
            port = ReParser.findone(self._portre, proxystr)
            logging.debug('port match: %s' % port)
            proto = ReParser.findone(self._protocolre, proxystr)
            logging.debug('protocol match: %s' % proto)
            proxy = Proxy(ip, port, proto)
            proxylist.append(proxy)
        
        return proxylist
