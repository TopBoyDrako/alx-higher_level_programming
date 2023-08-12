#!/usr/bin/python3

# function that prints alphabets in reverse

for i in range(122, 64, -1):
    char1 = chr(i)       # Lowercase letter
    char2 = chr(i - 32)  # Uppercase letter
    print("{}{}".format(char1, char2), end="")
