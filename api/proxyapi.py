import sys, logging
sys.path.append("..")
from model import Session, Proxy


def add(proxy):
    session = Session()
    count = session.query(Proxy).filter(Proxy.ip == proxy.ip, Proxy.port == proxy.port).count()
    if not count:
            session.add(proxy)
            session.commit()
    session.close()


def query(offset, limit):
    session = Session()
    proxys = session.query(Proxy).limit(limit).offset(offset)
    session.close()
    return proxys
