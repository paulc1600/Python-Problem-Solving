#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Given an array of integers, find the sum of its elements. 
#           For example, if the array
#               ar = [1, 2, 3], 1 +2 +3 = 6, so return 6. 
# 
#           Array elements never > 1000
# ---------------------------------------------------------------------
#  PPC | 08/26/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    sum = 0
    for element in ar:
        sum = sum + element
             
    return sum    

if __name__ == '__main__': 
    n = 6
    ar = [1, 2, 3, 4, 10, 11]
    print()
    print(ar)
    result = simpleArraySum(ar)
    print(str(result) + '\n')
    
