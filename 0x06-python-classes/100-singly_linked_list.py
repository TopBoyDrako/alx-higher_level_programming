#!/usr/bin/python3
"""
This Module contains two classes

@properties:
class Node: defines a node of a singly linked list
class SinglyLinkedList: defines a sinly linked list
"""


class Node:
     """
    A class representing a node in a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The next node in the linked list.

    Methods:
        data (property): Retrieve the data stored in the node.
        data (setter): Set the data stored in the node.
        next_node (property): Retrieve the next node in the linked list.
        next_node (setter): Set the next node in the linked list.

    Args:
        data (int): The data to be stored in the node.
        next_node (Node, optional): The next node in the linked list.
        Default is None.
    """

    def __init__(self, data, next_node=None):
         """
        Initializes a node.

        Parameters:
            data: The data of the node.
            next_node: The next node in the linked list. Defaults to None.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    """Retrieve the data of the node."""
    def data(self):
        return self.__data

    @data.setter
     """Set the data of the node."""
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        __head (Node): The head node of the linked list.

    Methods:
        sorted_insert(value): Inserts a new Node into the correct sorted position in the list (increasing order).
        print_list(): Prints the entire list in stdout, one node per line.

    Args:
        None
    """
    def __init__(self):
    """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Parameters:
            value: The value to be inserted.
        """
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def print_list(self):
        current = self.__head
        while current is not None:
            print(current.data)
            current = current.next_node
