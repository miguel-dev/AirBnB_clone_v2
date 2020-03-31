#!/usr/bin/python3
"""Store data in database"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from os import environ
from models.base_model import Base
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review


class DBStorage():
    """Connects to the database"""
    __engine = None
    __session = None

    def __init__(self):
        """Creates engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                        environ.get("HBNB_MYSQL_USER"),
                        environ.get("HBNB_MYSQL_PWD"),
                        environ.get("HBNB_MYSQL_HOST"),
                        environ.get("HBNB_MYSQL_DB")),
                        pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(bind=engine)

    def all(self, cls=None):
        """Print all records from a table"""
        session = self.__session
        dict_reg = {}
        if not cls:
            classes = [User, City, Amenity, State, Place, Review]
        else:
            classes = [eval(cls)]
        for clas in classes:
            result = session.query(clas).all()
            for reg in result:
                key = "{}.{}".format(type(clas), reg.id)
                dict_reg[key] = reg
        return dict_reg
