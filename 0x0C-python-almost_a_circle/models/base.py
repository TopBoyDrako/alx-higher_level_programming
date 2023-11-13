#!/usr/bin/python3

"""
This module defines a class with a private and public attribute each
@private attribute = __nb_objects
@public attribute = id
"""


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
