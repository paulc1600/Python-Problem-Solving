#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: You are given an unordered array consisting of consecutive
#           integers  E [1, 2, 3, ..., n] without any duplicates. You
#           are allowed to swap any two elements. You need to find the
#           minimum number of swaps required to sort the array in
#           ascending order.
#
#           For example, given the array  arr = [7, 1, 3, 2, 4, 5, 6]
#           we perform the following steps:
#
#           i   arr                     swap (indices)
#           
#           0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)       
#           1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)      
#           2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)        
#           3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)        
#           4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)          
#           5   [1, 2, 3, 4, 5, 6, 7]
#
#           It took 5 swaps minimum to sort the array.
#
#           It must return an integer representing the minimum number of
#           swaps to sort the array.
#
# ---------------------------------------------------------------------
#  PPC | 08/21/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

global totalSwaps
totalSwaps = 0
global unsorted
unsorted = []

# Complete the minimumSwaps function below.
def minimumSwaps(my_arr):
    # Run quicksort on a list of integers
    #   sIdx l is list starting index (initially 0)
    #   eIdx r is list ending index (initially len(arr) - 1
    global unsorted
    global sIdx
    global eIdx
    global totalSwaps

    unsorted = my_arr
    sIdx = 0
    eIdx = len(unsorted) - 1

    # quicksort pivot always last element in list ... because
    pivotIdx = eIdx
    pivot = unsorted[pivotIdx]

    # Reorder array around original pivot point
    loopNbr = 0 
    nbrSwaps = 0
    while nbrSwaps == 0:
        for chkIdx in range(sIdx, eIdx):
            # Elements to left of pivot: check less than pivot value
            # Elements to right of pivot: check greater than pivot value
            if chkIdx < pivotIdx:
                side = "left"
            elif chkIdx > pivotIdx:
                side = "right"
            else:
                side = "pivot"

            # Depending on where you are, check accordingly against current pivot value
            if (side == "left" and unsorted[chkIdx] >= pivot) or \
               (side == "right" and unsorted[chkIdx] < pivot):
                # If an element greater than or equal to the pivot is found left of
                # pivot location, or an element is less than pivot and is found right of
                # pivot then swap unsorted[pivotIdx] and unsorted[chkIdx] so that the
                # smaller elements are always to the left of pivot and greater elements
                # are on the right
                temp = unsorted[chkIdx]
                unsorted[chkIdx] = unsorted[pivotIdx]
                unsorted[pivotIdx] = temp
                nbrSwaps = nbrSwaps + 1

                # Move pivot location
                pivotIdx = chkIdx
                pivot = unsorted[pivotIdx]

        # Increment big loop (number of scans through array)
        loopNbr = loopNbr + 1
        
        # Continue sorting if swap happened, otherwise need new pivot and new array
        if nbrSwaps > 0:
            # For this big loop, total up the swaps
            totalSwaps = totalSwaps + nbrSwaps  
            nbrSwaps = 0    # Reset to go again
        else:
            break           # stop big loop
        
    # After looping, create sub-arrays for left and right side that may still
    # need more sorting.
    if pivotIdx >= 2:
        larr = unsorted[0:pivotIdx]       # Excludes pivot itself
        minimumSwaps(larr)                # Recursively sort the left sub-array

    if len(unsorted[pivotIdx + 1:]) >= 2:
        rarr = unsorted[pivotIdx + 1:]    # All elements after pivot
        minimumSwaps(rarr)                # Recursively sort the right sub-array
      
    return totalSwaps
                

if __name__ == '__main__': 
    arr = [2, 3, 4, 1, 5]
    n = 5
    print(arr)
    res = minimumSwaps(arr)
    print(str(res) + '\n')

