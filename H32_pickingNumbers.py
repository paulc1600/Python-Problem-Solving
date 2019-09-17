#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Given an array of integers, find and print the maximum
#           number of integers you can select from the array such that
#           the absolute difference between any two of the chosen
#           integers is less than or equal to 1. For example, if your
#           array is a = [1, 1, 2, 2, 4, 4, 5, 5, 5], you can create
#           two subarrays meeting the criterion: [1, 1, 2, 2] and
#           [4, 4, 5, 5, 5]. The maximum length subarray has 5
#           elements. 
#           
#           Function Description 
#           Complete the pickingNumbers function in the editor below.
#           It should return an integer that represents the length of
#           the longest array that can be created. 
# ---------------------------------------------------------------------
#  PPC | 09/16/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys


# Longest array that can be craeted were all members <= 1 away each other?
def pickingNumbers(arr):
    longest = [0 for i in range(50)]
    nbrIdx = 0
    grpIdx = 0           # index of sub-array "longest" containing counts
    sig = 101            # smallest value in each group

    # easier if sorted
    arr.sort()
    prev = arr[0]
    # print(longest)
    print(arr)

    for nbrIdx in range(0, len(arr)):
        if arr[nbrIdx] < sig:
            sig = arr[nbrIdx]
        # print(nbrIdx, arr[nbrIdx], prev, arr[nbrIdx] - prev, sig)
        if (arr[nbrIdx] - prev <= 1) and (arr[nbrIdx] - sig <= 1):
            longest[grpIdx] = longest[grpIdx] + 1
        else:
            grpIdx = grpIdx + 1
            longest[grpIdx] = longest[grpIdx] + 1
            sig = arr[nbrIdx]
        prev = arr[nbrIdx]

    longest.sort(reverse=True)
    result = longest[0]
    print(longest)
    return result


if __name__ == '__main__':
    a = [1, 2, 2, 3, 1, 2]
    result = pickingNumbers(a)
    print(result)
    print()
    a = [1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 13, 13]
    result = pickingNumbers(a)
    print(result)
