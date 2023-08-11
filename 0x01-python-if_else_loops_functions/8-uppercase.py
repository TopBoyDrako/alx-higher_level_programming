#!/usr/bin/python3

# function to print strings in uppercase

def uppercase(str):

    uppercase_str = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            uppercase_str += uppercase_char
        else:
            uppercase_str += char

    print("{}".format(uppercase_str))
