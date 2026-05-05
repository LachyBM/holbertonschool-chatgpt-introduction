#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial number using recursion

    Parameters:
    a (int): a non-negative interger whose factorial is to be calced

    Return:
    int: the factorial of the given number
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
