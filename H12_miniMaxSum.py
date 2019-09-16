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
    group_arr = [0, 0, 0, 0, 0]
    group_sums = [0, 0, 0, 0, 0]

    # Silly now, but needed later
    min_sum = simpleArraySum(MyArr)
    max_sum = 0
    
    # Create all possible groups of 4
    for idx in range(5):
        if idx == 0:
            lside = []
            rside = MyArr[1:5]
            # print(idx)
            group_arr[0] = rside
            # print(group_arr[0])
        elif idx > 0 and idx <4:
            lside = MyArr[0:idx]
            rside = MyArr[idx+1:5]
            # print(idx)
            group_arr[idx] = lside + rside
            # print(group_arr[idx])
        elif idx == 4:
            lside = MyArr[0:4]
            rside = []
            # print(idx)
            group_arr[4] = lside
            # print(group_arr[4])

        # For each group array, find it's sum
        group_sums[idx] = simpleArraySum(group_arr[idx])
        # print(group_sums[idx])

        # Scan all the sums to find the min and max sum
        if group_sums[idx] >= max_sum:
            max_sum = group_sums[idx]
        if group_sums[idx] <= min_sum:
            min_sum = group_sums[idx]

    print(min_sum, max_sum)

      
if __name__ == '__main__':
    n = 5
    arr = [1, 3, 5, 7, 9]
    print(arr)
    result = miniMaxSum(arr)

    
