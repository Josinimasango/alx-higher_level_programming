#!/usr/bin/python3

from calculator_1 import add, subt, mult, div

if __name__ = "__main__":
a = 10
b = 5
print("{:d} + {:d} = {:d}".format(a, b, add(a, b, add(a, b)))
print("{:d} - {:d} = {:d}".format(a, b, subt(a, b, subt(a, b)))
print("{:d} * {:d} = {:d}".format(a, b, mul(a, b, mult(a, b)))
print("{:d} / {:d} = {:d}".format(a, b, div(a, b, div(a, b)))  
