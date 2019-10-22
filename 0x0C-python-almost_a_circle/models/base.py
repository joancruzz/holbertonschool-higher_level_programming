#!/usr/bin/python3


"""
This is a Base module for base class
"""


import json
import os


class Base:
    """Represents a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initiate class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return json representaion of dict"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Write json string to file"""
        with open(cls.__name__ + '.json', 'w+') as f:
            if len(list_objs) is not 0 and list_objs is not None:
                my_list = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(my_list))
            else:
                f.write('[]')

    def from_json_string(json_string):
        """Return list of json string rep"""
        if json_string:
            return json.loads(json_string)
        else:
            return "[]"

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with attributes"""
        if cls.__name__ == 'Square':
            object = cls(1)
            object.update(**dictionary)
            return object

        if cls.__name__ == 'Rectangle':
            object = cls(1, 2)
            object.update(**dictionary)
            return object

    @classmethod
    def load_from_file(cls):
        """ Load a json string from a file and return dictionary """
        try:
            with open(cls.__name__ + ".json", 'r') as f:
                pass
        except FileNotFoundError:
            return []
        with open(cls.__name__ + ".json", 'r') as fp:
            load = cls.from_json_string(f.read())
        return [cls.create(**d) for d in load]
