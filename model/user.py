#!/usr/bin/env python
# coding: utf8
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


if __name__ == "__main__":
    import logging
    logging.basicConfig(level = logging.DEBUG)

    engine = create_engine("sqlite:///spider.db", echo = True)
    Base.metadata.create_all(engine)
    """ 
    dbsession = sessionmaker(bind = engine)
    session = dbsession()

    session.add(User(id = "1", name = "aaaa"))
    session.commit()


    user = session.query(User).filter(User.id == "1").one()

    logging.info("[User] %s", user)
    """
