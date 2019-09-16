#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: You are given an array of n integers,
#           ar = [ar[0], ar[1], ... , ar[n - 1], and a positive
#           integer, k.
#           
#           Find and print the number of (i, j) pairs where i < j
#           and ar[i] + ar[j] is divisible by k. 
#           
#           For example, ar = [1, 2, 3, 4, 5, 6] and k = 5. Our three
#           pairs meeting the criteria are [1, 4], [2, 3] 
#           and [4, 6] 
# ---------------------------------------------------------------------
#  PPC | 09/02/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# Divisible Sum Pairs
def divisibleSumPairs(Myn, Myk, MyArr):
    nbrWays = 0
    
    for i in range(0, Myn):
        for j in range(Myn - 1, i, -1):
            if i < j and ((MyArr[i] + MyArr[j]) % Myk) == 0:
                nbrWays = nbrWays + 1
                          
    return nbrWays

      
if __name__ == '__main__':
    n = 6
    k = 3
    ar = [1, 3, 2, 6, 1, 2]
    
    result = divisibleSumPairs(n, k, ar)
    print(result)


    
