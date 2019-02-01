from .proxy import Proxy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

engine = create_engine("sqlite:///database.db")
Session = sessionmaker(engine)
Proxy.metadata.create_all(engine)

