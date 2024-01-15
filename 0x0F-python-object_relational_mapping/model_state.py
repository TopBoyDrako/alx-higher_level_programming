#!/usr/bin/python3
"""
This module is a python script that links to an SQL table called
states and runs some functions
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    This is a subclass that inherits from Base and links to MySQL
    table states.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
