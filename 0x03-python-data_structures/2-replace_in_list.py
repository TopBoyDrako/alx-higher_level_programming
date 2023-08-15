#!/usr/bin/python3

#  Function to replace an element in a list

def replace_in_list(my_list, idx, element):

    if idx < 0 or idx >= len(my_list):
        return my_list[idx]
    return my_list[idx]/element
