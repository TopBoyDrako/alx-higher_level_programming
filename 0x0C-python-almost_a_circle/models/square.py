#!/usr/bin/python3

"""
This module defines a class Square which inherits from the class Rectangle
def __init__(self, size, x=0, y=0, id=None)
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class inheits from a rectangle and doesn't create new attributes
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[{}] ({}) {}/{} - {}'. \
            format(type(self).__name__, self.id, self.x, self.y, self.width)
