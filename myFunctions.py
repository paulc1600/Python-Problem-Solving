#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Functions
#
# ---------------------------------------------------------------------
#  PPC | 08/13/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

aglobal = 1

# We can create a function that writes the Fibonacci series to an arbitrary boundary.
def fib(n):    # write Fibonacci series up to n
        """Print a Fibonacci series up to n."""
        fiblist = []
        a, b = 0, 1
        while a < n:
            # end parm changes default eol \n to space
            print(a, end=' ')    # print to terminal
            fiblist.append(a)    # capture fib series in list
            bt = b
            b = a + b
            a = bt
            # a, b = b, a+b
        print()
        return fiblist
    
# I want that 4th carrier.
# This is not the main body 
if __name__ == '__main__':	
    fibrslt = fib(2000)
    print(fibrslt)

