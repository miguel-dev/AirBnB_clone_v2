#!/usr/bin/python3
"""This is the state class"""
from os import environ
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """Getter for all cities by state"""
            cities_dict = models.storage.all(City)
            list_cities = []
            for key, value in cities_dict.items():
                if value.state_id == self.id:
                    list_cities.append(value)
            return list_cities
