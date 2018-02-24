# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'

from  sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,text

from  etc.config import Config


def connection(database):
    engine = create_engine(database,pool_size=20, max_overflow=0,pool_timeout=30)
    Session = sessionmaker(engine)
    session = Session()
    return session

conn = connection(Config.db)
