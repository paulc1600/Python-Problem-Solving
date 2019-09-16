#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: Practice
#  Purpose: Convert all array elements to binary
#
# ---------------------------------------------------------------------
#  PPC | 08/20/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# File is formatarray.py
def bindString(s):       
    for r in range(3):
            for c in range(3):
                element = s[r][c]
                ebin = "{0:08b}".format(element)
                nib = str(ebin[0:4]) + " " + str(ebin[4:8])
                print(nib, "   ", end=" ")
            print()      
    return     

if __name__ == '__main__': 
    arr =[[12, 31, 3], [8, 12, 15], [2, 2, 31]]
    print()
    print(arr)
    result = bindString(arr)
    
