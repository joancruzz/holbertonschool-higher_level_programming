#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dict"""
        st = {}
        if attrs is None:
            return self.__dict__
        for key in attrs:
            if key in self.__dict__.keys():
                st[key] = self.__dict__[key]
        return st

    def reload_from_json(self, json):
        """Replace all attributes of the student instance"""
        for key in json:
            setattr(self, key, json[key])
