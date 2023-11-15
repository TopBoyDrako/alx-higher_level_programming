#!/usr/bin/python3

"""
This module defines a class with a private and public attribute each
@private attribute = __nb_objects
@public attribute = id

"""


from json import dumps, loads
import csv


class Base:
    """
    This class defines a function which manages a public attribute "id"
    in all future classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the public attribute "id" """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string reprsentation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return dumps(list_dictionaries)
