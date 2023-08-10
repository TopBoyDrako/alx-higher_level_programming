#!/usr/bin/python3

def islower(c):
    return ord('a') <= ord(c) <= ord('z')

def check_case(c):
    case_dict = {
        'lower': True,
        'upper': False
    }
    return case_dict['lower' if islower(c) else 'upper']

# Test cases
characters = ['a', 'H', 'A', '3', 'g']

for char in characters:
    print("{} is {}".format(char, "lower" if check_case(char) else "upper"))

