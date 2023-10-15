#!/usr/bin/python3
"""This is a base class that holds dates attributes in
object eas created perform some serialization and
deserialization of an objects
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    This class represents the basemodel
    of an objects

    """

    def __init__(self, *args, **kwargs):
        """Initialization of new an
        attributes.

        Args:
            *args (any): unused arguments
            **kwargs (dict): this is the key and values
            pass to the constructor

        Attributes:
            id (str) - a unique id of an objects
            created_at (str) - date which the object is created
            updated_at (str) - date which objects are updated
        """

        dateformat = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, dateformat)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """  this class updates the the object
        with the current date when the date is
        saved

        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ This convert the objects to dictionary representation
        of an objects

        """
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """ return the string representation of an objects"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
