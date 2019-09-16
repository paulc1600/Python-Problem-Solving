#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Lily has a chocolate bar that she wants to share it with
#           Ron for his birthday. Each of the squares has an integer
#           on it. She decides to share a contiguous segment of the
#           bar selected such that the length of the segment matches
#           Ron's birth month and the sum of the integers on the
#           squares is equal to his birth day. 
#
#           You must determine how many ways she can divide the
#           chocolate.
#               s: an array of integers, the numbers on each of the
#                  squares of chocolate
#               d: an integer, Ron's birth day (sum of ints)
#               m: an integer, Ron's birth month (length segment)
# ---------------------------------------------------------------------
#  PPC | 09/02/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# How to chop a chocolate bar so Ron is happy
def birthday(s, d, m):
    nbrWays = 0
    seg = []

    # range (start, stop[, step])
    # Lists have at least one element
    rStart = 0
    rEnd = len(s)
    newSlice = m 
    for idx in range(rStart,rEnd):
        seg = s
        sliceN = seg[idx:newSlice]
        if len(sliceN) >= m:
            if sum(sliceN) == d:
                nbrWays = nbrWays + 1
        else:
            # Remaining chocolate wont make large enough gift
            break
        
        # print(seg, " idx = ", idx, " Slice = ", sliceN,
        #     " Length want = ", m, "Status = ", nbrWays)
        newSlice = newSlice + 1
          
    return nbrWays

      
if __name__ == '__main__':
    n = 5
    s = [1, 2, 1, 3, 2]
    d = 3
    m = 2
    result = birthday(s, d, m)
    print(result)


    
