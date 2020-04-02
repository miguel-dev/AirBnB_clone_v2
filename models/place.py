#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import environ

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete',
                               backref="place")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """get all reviews by place"""
            reviews_dict = models.storage.all(Review)
            list_reviews = []
            for key, value in reviews_dict.items():
                if value.place_id == self.id:
                    list_reviews.append(value)
            return list_reviews

        @property
        def amenities(self):
            """Get all amenities by place"""
            amenities_dict = models.storage.all(Amenity)
            list_amenities = []
            for key, value in amenities_dict.items():
                if value.place_id == self.id:
                    list_amenities.append(value)
            return list_amenities

        @amenities.setter
        def amenities(self, obj):
            """Appends an amenity id to attribute amenities_id"""
            if obj and isinstance(obj, Amenity):
                    self.amenity_ids.append(obj.id)
