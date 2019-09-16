#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Given five positive integers, find the minimum and maximum
#           values that can be calculated by summing exactly four of
#           the five integers. Then print the respective minimum and
#           maximum values as a single line of two space-separated long
#           integers.
#
# ---------------------------------------------------------------------
#  PPC | 08/26/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys


# Sum up all elements of an array
def simpleArraySum(MyArr):
    sum = 0
    for element in MyArr:
        sum = sum + element      
    return sum   

# The array always has most 5 integers. Which set of 4 gives min / max sum?
# Print the min sum, and max sum only separated by space 
def miniMaxSum(MyArr):
    MyArr.sort()

    # Silly now, but needed later
    min_sum = simpleArraySum(MyArr[0:4])
    max_sum = simpleArraySum(MyArr[1:5])

    print(MyArr)
    print(min_sum, max_sum)

      
if __name__ == '__main__':
    n = 5
    arr = [3, 1, 5, 7, 9]
    print(arr)
    result = miniMaxSum(arr)

    
