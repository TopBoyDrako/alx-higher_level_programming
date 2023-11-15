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
        """initializes the atributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """this str methid returns a str and print method for the square"""
        return '[{}] ({}) {}/{} - {}'. \
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter method for the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method for the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This method assisngs attributes to each of the arguments"""
        if args:
            self.id = args[0] if len(args) > 0 else getattr(self, 'id', None)
            self.size = args[1] if len(args) > 1 else getattr(self, 'size', None)
            self.x = args[2] if len(args) > 2 else getattr(self, 'x', None)
            self.y = args[3] if len(args) > 3 else getattr(self, 'y', None)
        elif kwargs:
            self.id = kwargs.get('id', getattr(self, 'id', None))
            self.size = kwargs.get('size', getattr(self, 'size', None))
            self.x = kwargs.get('x', getattr(self, 'x', None))
            self.y = kwargs.get('y', getattr(self, 'y', None))
