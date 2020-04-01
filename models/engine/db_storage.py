#!/usr/bin/python3
"""Store data in database"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
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
        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=engine)

    def all(self, cls=None):
        """Print all records from a table"""
        session = self.__session
        dict_reg = {}
        classes = []
        if not cls:
            classes.extend([User, City, State, Place, Review])
        else:
            classes.append(cls)
        for clas in classes:
            result = session.query(clas).all()
            for reg in result:
                key = "{}.{}".format(clas.__name__, reg.id)
                dict_reg[key] = reg
        return dict_reg

    def new(self, obj):
        """Add the object to current database session"""
        session = self.__session
        session.add(obj)

    def save(self):
        """Save session in database"""
        session = self.__session
        session.commit()

    def delete(self, obj=None):
        """Delete object from session"""
        session = self.__session
        session.delete(obj)

    def reload(self):
        """Reload session from database"""
        Base.metadata.create_all(self.__engine)
        metasession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(metasession)
        self.__session = Session()
