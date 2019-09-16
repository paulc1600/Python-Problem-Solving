#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: You will be given two arrays of integers and asked to
#           determine all integers that satisfy the following two
#           conditions:
#           
#           	1. The elements of the first array are all
#                    factors of the integer being considered
#           	2. The integer being considered is a factor of all
#                    elements of the second array
#           	
#           These numbers are referred to as being between the two
#           arrays. You must determine how many such numbers exist.
# ---------------------------------------------------------------------
#  PPC | 08/30/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# INtegers between array
def getTotalX(arrA, arrB):
    total = 0
    
    # Lists have at least one element
    for candInt in range(max(arrA), min(arrB) + 1):
        # all of array A is a factor?
        goodA = True
        for itemA in arrA:
            if (candInt % itemA) !=0:
                goodA = False
                break
            else:
                pass
        
        # Candidate number factor in all of B?
        goodB = True
        if goodA:
            for itemB in arrB:
                if (itemB % candInt) !=0:
                    goodB = False
                    break
                else:
                    pass            
        else:
            # Don't check B if A test already failed
            goodB = False
            pass

        if goodA and goodB:
            total = total + 1    
  
    return total

      
if __name__ == '__main__':
    n = 2
    m = 3
    # arr = [2, 4]
    # brr = [16, 32, 96]
    arr = [2, 6]
    brr = [24, 36]

    result = getTotalX(arr, brr)
    print(result)


    
