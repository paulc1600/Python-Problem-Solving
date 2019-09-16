#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: For each array, perform a number of right circular
#           rotations and return the value of the element at a given
#           index.
#           
#           For example, array a = [3, 4, 5], number of rotations,
#           k = 2 and indices to check, m = [1, 2).  First we perform
#           the two rotations: 
#              [3, 4, 5] --> [5, 3, 4] --> [4, 5, 3]
#           
#           Now return the values from the zero-based indices 1 and 2
#           as indicated in the m array. 
#              a[1] = 5 
#              a[2] = 3 
# ---------------------------------------------------------------------
#  PPC | 09/07/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys


# Find index after rotation
def circularArrayRotation(a, k, queries):
    myIdx = 0                    # not rotated yet
    myZero = 0                   # New index
    lenA = len(a)                # Element count of rotation array
    myAnswer = []

    partSpin = k % lenA
    myZero = myZero - partSpin + lenA           # New 0 index
    
    for q in queries:
        if myZero + q < lenA:
            myIdx = myZero + q
        else:
            myIdx = myZero + q - lenA
        myAnswer.append(a[myIdx])
    
    return myAnswer

if __name__ == '__main__':
    a = [3, 4, 5]
    k = 2
    queries = [1, 2]
    result = circularArrayRotation(a, k, queries)
    print(result)
    print()
    
    a = [1, 2, 3]
    k = 2
    queries = [0, 1, 2]
    result = circularArrayRotation(a, k, queries)
    print(result)

