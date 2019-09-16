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

    words = ['cat', 'window', 'defenestrate']

    for w in words:
        if len(w) < 12: 
            print(w, "\t\t", len(w))
        else:
            print(w, "\t", len(w))

    # --------------------------------------------
    for i in range(5):
        print(i)
        
    # --------------------------------------------
    a = ['Mary', 'had', 'a', 'little', 'lamb']

    # Create range that covers entire list 
    for i in range(len(a)):
        if len(a[i]) < 6:
            print(i, a[i], "\t\t", len(a[i]))
        else:
            print(i, a[i], "\t", len(a[i]))
    
# I want that 4th carrier. This is not the main body 
if __name__ == '__main__':	
    result = myControl()

