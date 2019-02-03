# coding: utf8
import sys, logging
sys.path.append("..")
from model import Session, Proxy
import time, logger

def add(proxy):
    session = Session()
    count = session.query(Proxy).filter(Proxy.ip == proxy.ip, Proxy.port == proxy.port).count()
    if 0 == count:
            proxy.createtime = int(time.time())
            session.add(proxy)
            session.commit()
            logger.info("add proxy: %s" % proxy)
    else:
        logger.info("exists proxy: %s" % proxy)
    session.close()


def query(offset, limit):
    session = Session()
    proxys = session.query(Proxy).limit(limit).offset(offset).all()
    session.close()
    return proxys

def updatebyid(id, **kw):
    session = Session()
    session.query(Proxy).filter(Proxy.id == id).update(kw)
    session.commit()
    session.close()



__OFFSET__ = 0
def getrand():
    """
    获取随机Proxy
    """
    global __OFFSET__
  
    proxys = query(__OFFSET__, 1)  
    proxy = None
 
    if len(proxys) == 0 and __OFFSET__ != 0:
        __OFFSET__ =  1
        proxys = query(0, 1)

        if len(proxys) == 1:
            proxy = proxys[0]

    else:
        __OFFSET__ = __OFFSET__ + 1
        proxy = proxys[0]

    
    return proxy
