#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel, Base):
    """ State class """

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        ___tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all,delete", backref="state")
    elif os.getenv('HBNB_TYPE_STORAGE') == 'fs':
        name = ''

        @property
        def cities(self):
            citylist = []
            city_dict = models.storage.all(City)
            for key, value in city_dict.items():
                if value.state_id == self.id:
                    citylist.append(value)
            return citylist
