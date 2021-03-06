# ORM 2

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///test1.db", echo=True)
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


Base.metadata.create_all(engine)

