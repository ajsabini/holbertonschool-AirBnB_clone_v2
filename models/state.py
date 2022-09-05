#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """ State class """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        ___tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all,delete", backref="state")
    elif getenv('HBNB_TYPE_STORAGE') == 'sf':
        @property
        def cities(self):
            citylist = []
            city_dict = models.storage.all(models.city.City)
            for key, value in city_dict.items():
                if value.state_id == self.id:
                    citylist.append(value)
            return citylist
