#!/usr/bin/python3
"""class definition of a State and an instance Base = declarative_base() """

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String
Base = declarative_base()


class State(Base):
    """ State class that inherits from Base class """
    __tablename__ = 'states'
    id = sqlalchemy.Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(128), nullable=False)
