#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Simple for
#
# ---------------------------------------------------------------------
#  PPC | 08/12/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys


# Do not be a control freak.
def myControl():

        
    # --------------------------------------------
    primes = [1]
    
    for n in range(2, 10):
        for x in range(2, n):
            # print("Checking on number:", n, " factor is ", x, " and remainder is ", n%x) 
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
            primes.append(n)

    print(primes)
    
# I want that 4th carrier.
# This is not the main body 
if __name__ == '__main__':	
    result = myControl()

