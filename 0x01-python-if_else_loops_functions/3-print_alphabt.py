#!/usr/bin/python3

for i in range (97, 123):
    if (i == 103 or i ==113):
        print(end="")
    else:
        output = "{}".format(chr(i))
        print(output, end="")
