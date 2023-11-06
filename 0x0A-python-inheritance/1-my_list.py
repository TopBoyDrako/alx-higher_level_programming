#!/usr/bin/python3

"""
This module defines a class which inherits from another class.
It also defines a function inside the calss that prints a sorted list in
alphabetical order.
"""


class MyList(list):
    """
    This class defines a function that prints from the list in sorted ascending
    order.
    """

    def print_sorted(self):
        """
        This functons prints a sorted list in ascending order
        """
        print(sorted(list(self)))
