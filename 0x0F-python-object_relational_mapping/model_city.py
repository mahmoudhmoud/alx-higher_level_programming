#!/usr/bin/python3

''' kyatika achman mdian '''

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    ''' mdina fiaa dyalha '''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
