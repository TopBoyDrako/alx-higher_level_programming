#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    a = 10
    b = 5

result = add(a, b), sub(a, b), mul(a, b), div(a, b)

print("{:d} + {:d} = {:d}".format(a, b, result[0]))
print("{:d} - {:d} = {:d}".format(a, b, result[1]))
print("{:d} * {:d} = {:d}".format(a, b, result[2]))
print("{:d} / {:d} = {:d}".format(a, b, result[3]))
