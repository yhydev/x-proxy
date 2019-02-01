#!/usr/bin/env python
# coding: utf8
from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Proxy(Base):
    """proxy 数据库对象"""
    __tablename__ = "proxy"

    id = Column(Integer, primary_key = True, autoincrement = True)    
    ip = Column(String(15))
    port = Column(Integer)
    checkcount = Column(Integer, default = 0)
    successcount = Column(Integer, default = 0)




