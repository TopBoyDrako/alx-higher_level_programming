#!/usr/bin/python3

"""
This module contains a subclass inheriting from attributes and methods
from it's parent class
"""



class MyInt(int):

    """
    This class is a rebel. It has the operators == and != inverted
    """

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
