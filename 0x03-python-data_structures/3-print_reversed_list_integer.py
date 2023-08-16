#!/usr/bin/python3

#  prints all integers in reverse

def print_reversed_list_integer(my_list=[]):

    if my_list is None:
        return None
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
