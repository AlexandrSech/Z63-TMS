# ORM

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper

engine = create_engine("sqlite:///test1.db", echo=True)

metadata = MetaData()

users_table = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('firstname', String),
    Column('lastname', String),)

metadata.create_all(engine)


class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


mapper(User, users_table)

user = User('Alex', 'Varkalov')

