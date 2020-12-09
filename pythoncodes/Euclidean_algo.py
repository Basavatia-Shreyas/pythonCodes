from math import *


def euclid_algo(x, y, verbose=True):
    if x < y:  # We want x >= y
        return euclid_algo(y, x, verbose)
    print()
    while y != 0:
        if verbose: print('%s = %s * %s + %s' % (x, floor(x / y), y, x % y))
        (x, y) = (y, x % y)

    if verbose: print('gcd is %s' % x)
    return x
#prompt for numbers
num_one = input("Enter an integer")
num_two = input("Enter another integer")

euclid_algo(int(num_one), int(num_two))








