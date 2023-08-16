#!/usr/bin/python3

# this funcction replaces elements in a list without modifying the original

def new_in_list(my_list, idx, element):

    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list.copy()
    my_list[idx] = element
    return my_list
