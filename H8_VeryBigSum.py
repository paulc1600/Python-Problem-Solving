#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Calculate and print the sum of the elements in an array,
#           keeping in mind that some of those integers may be quite
#           large.
#
#           Function Description
#           Complete the aVeryBigSum function in the editor below. It
#           must return the sum of all array elements. aVeryBigSum has
#           the following parameter(s):
#              o ar: an array of integers .
#
#           Input Format
#           The first line of the input consists of an integer . 
#           The next line contains  space-separated integers contained
#           in the array.
# 
# as long as you have version 2.5 or better, just perform
# standard math operations and any number which exceeds the
# boundaries of 32-bit math will be automatically (and
# transparently) converted to a bignum.
# 
# You can find all the gory details in PEP 0237.
# ---------------------------------------------------------------------
#  PPC | 08/26/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# Sum All very big Elements in an array
def aVeryBigSum(ar):
    sum = 0
    for element in ar:
        sum = sum + element
             
    return sum 
  
if __name__ == '__main__': 
    arr = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    print()
    print(arr)
    result = aVeryBigSum(arr)
    print(str(result) + '\n')
    
