#!/usr/bin/python3

"""
This module defines a subclass Rectangle that inherits from Base
the superclass. It contains 4 different private attributes used to
define the rectangle shape

private attributes are:
__width
__height
__x
__y

The __init__ function initalizes the private attribute and calls the parent
class using the super() function

The private attributes are validated using getters and setter method for
each of them.

def area() - This returns the area of the rectangle
def display() - This displays the rectangle using the # character
__str__ - this method formats the string representation of the rectangle
def update() - here we use *args to assign an argument to each attribute.
The update method is later updated to also use **kwargs in assinging a key
and value to the attributes
"""


from models.base import Base


class Rectangle(Base):
    """
    This class defines a rectangle with 4 private attributes
    @property
    self.__width
    self.__height
    self.__x
    self.__y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the private attributes of the class rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x attribute"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y attribute"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This defines the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """this displays the rectangle with the # character"""
        if self.width == 0 or self.height == 0:
            print("")
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """overrides the str method and returns a new string"""
        return "[{}] ({}) {}/{} - {}/{}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def update(self, *args):
        """this function assigns an argument to each attribute"""
