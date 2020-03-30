#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        If cls is None, all() returns the __object dictionary
        Otherwise,
            returns a dictionary of objects of that type of class
        """
        if cls is None:
            return FileStorage.__objects
        else:
            d = {}
            for k, v in FileStorage.__objects.items():
                if v.__class__ == cls:
                    d[k] = v
            return d

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = value
                    self.new(value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ deletes an object from the dict __objects if it's inside
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            try:
                del FileStorage.__objects[key]
                self.save()
            except KeyError:
                pass
