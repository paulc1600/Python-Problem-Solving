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
    for i in range(5):
        print(i)
        
    # --------------------------------------------
    results = [[0,0,0]] 

    for i in range(1,101):
        results.append([i,0,0])

    print(results)

    
# I want that 4th carrier.
# This is not the main body 
if __name__ == '__main__':	
    result = myControl()

