#!/usr/bin/python3
"""Module defining MyList class."""


class MyList(list):
    """Inherits from list and adds a method to print sorted list."""

    def print_sorted(self):
        """Prints the list in sorted order."""
        print(sorted(self))
