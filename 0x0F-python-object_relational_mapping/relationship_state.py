#!/usr/bin/python3
"""
This is a module that contains a class State which inherits froM
a class Base
"""

from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        The States class which inherits from parent class Base.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
