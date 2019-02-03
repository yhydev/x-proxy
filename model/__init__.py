from .proxy import Proxy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import sys

engine = create_engine("sqlite:///database.db")
sessionfactory = sessionmaker(engine)
Session = scoped_session(sessionfactory)

Proxy.metadata.create_all(engine)

