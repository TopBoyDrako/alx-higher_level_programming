#!/usr/bin/python3
"""
This module defines a class Student that takes informartion of the students.
It then defines a function in the class used to retrive a dictionary
representation of a Student instance
"""


class Student:
    """
    This class has public instance attributes used to collect information
    from students.It also has a function used to retrive a dictionary
    representation of Student instance
    """

    def __init__(self, first_name, last_name, age):
        """instantiates the public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a __dict__ of an instance of the class Student"""
        return self.__dict__
