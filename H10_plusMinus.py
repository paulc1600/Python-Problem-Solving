#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Given an array of integers, calculate the fractions of its
#           elements that are positive, negative, and are zeros. Print
#           the decimal value of each fraction on a new line rounded to
#           six decimals.
#
#           Output Format
#           You must print the following  lines:
#           1. A decimal representing of the fraction of positive 
#              numbers in the array compared to its size.
#           2. A decimal representing of the fraction of negative 
#              numbers in the array compared to its size.
#           3. A decimal representing of the fraction of zeros in
#              the array compared to its size.
#
# ---------------------------------------------------------------------
#  PPC | 08/26/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# Print 3 float ratios for positive, negative and zero array elements.
def plusMinus(MyArray):
    cntPos = 0
    cntZero = 0
    cntNeg = 0
    ecnt = len(MyArray)

    fpos = 0.0
    fzero = 0.0
    fneg = 0.0
    
    for element in MyArray:
        if element < 0:
            cntNeg = cntNeg + 1
        elif element > 0:
            cntPos = cntPos + 1
        else:
            cntZero = cntZero + 1

    # round(.1 + .1 + .1, 10)
    # format(0.1, '.17f')
    
    fpos = round(cntPos/ecnt, 6)
    fzero = round(cntZero/ecnt, 6)
    fneg = round(cntNeg/ecnt, 6)

    print(format(fpos, '.6f'))
    print(format(fneg, '.6f'))
    print(format(fzero, '.6f'))
    return 
  
if __name__ == '__main__': 
    arr = [-4, 3, -9, 0, 4, 1]
    print()
    print(arr)
    result = plusMinus(arr)

    
