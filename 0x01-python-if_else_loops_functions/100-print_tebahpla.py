#!/usr/bin/python3

for i in range(122, 96, -2):
    char1 = chr(i)
    char2 = chr(i-33).upper()
    print("{}{}".format(char1, char2), end="")
