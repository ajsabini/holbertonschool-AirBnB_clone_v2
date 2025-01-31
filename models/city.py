#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.state import State

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
    elif os.getenv('HBNB_TYPE_STORAGE') == 'fs':
        state_id = ''
        name = ''
        plaes = []
