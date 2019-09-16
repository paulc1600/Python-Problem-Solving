#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Lilah has a string, s, of lowercase English letters that
#           she repeated infinitely many times. Given an integer,n,
#           find and print the number of letter a's in the first n 
#           letters of Lilah's infinite string. For example, if the
#           string s='abcac' and n = 10, the substring we consider is 
#           abcacabcac, the first 10 characters of her infinite string.
#           There are 4 occurrences of a in the substring.
#
#           Function Description
#           Complete the repeatedString function in the editor below.
#           It should return an integer representing the number of
#           occurrences of a in the prefix of length n  in the
#           infinitely repeating string.
#           
#           repeatedString has the following parameter(s):
#	    >>> s: a string to repeat
#           >>> n: the number of characters to consider
#
# ---------------------------------------------------------------------
#  PPC | 08/20/2019 | Original code.
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
global sorted_arr
sorted_arr = []

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

    print("New Call: ========================================================")
    print(len(unsorted), " element array is ===> ", unsorted)

    # quicksort pivot always last element in list ... because
    pivotIdx = eIdx
    pivot = unsorted[pivotIdx]
    print("pivot index = ", eIdx)
    print("pivot value = ", pivot)

    # Reorder array around original pivot point) 
    loopNbr = 0 
    nbrSwaps = 0
    while nbrSwaps == 0:
        print("------ Starting big loop nbr = ", loopNbr)
        for chkIdx in range(sIdx, eIdx):
            print("inner loop at ", chkIdx, " of ", eIdx)
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
                print("   Old array: ", unsorted, " Pivot point idx / value = ", pivotIdx, pivot)
                print("   Checking on the ", side, " side.")
                # If an element greater than or equal to the pivot is found left of
                # pivot location, or an element is less than pivot and is found right of
                # pivot then swap unsorted[pivotIdx] and unsorted[chkIdx] so that the
                # smaller elements are always to the left of pivot and greater elements
                # are on the right
                temp = unsorted[chkIdx]
                unsorted[chkIdx] = unsorted[pivotIdx]
                unsorted[pivotIdx] = temp
                nbrSwaps = nbrSwaps + 1
                # print("   Swapping indexes ", chkIdx, " with ", pivotIdx) 
                print("   Swapping values ", unsorted[chkIdx], " with ", unsorted[pivotIdx])
                # Move pivot location
                pivotIdx = chkIdx
                pivot = unsorted[pivotIdx]
                print("   New array: ", unsorted, " Pivot point idx / value = ", pivotIdx, pivot) 
                print()
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

    print("==================================================================")        
    return totalSwaps
                

if __name__ == '__main__': 
    arr = [1, 3, 5, 2, 4, 6, 7]
    n = 7
    print()
    res = minimumSwaps(arr)
    sorted_arr = unsorted
    print("Unsorted: ", arr)
    print("Sorted:   ", sorted_arr)
    print(str(res) + '\n')
    if res == 3:
        print("*****************************")
        print("***                       ***")
        print("*** Passed :-)    > 3 <   ***")
        print("***                       ***")
        print("*****************************")

    sorted_arr = []
    unsorted = []
    totalSwaps = 0
    arr = [2, 3, 4, 1, 5]
    n = 5
    print()
    res = minimumSwaps(arr)
    sorted_arr = unsorted
    print("Unsorted: ", arr)
    print("Sorted:   ", sorted_arr)
    print(str(res) + '\n')
    if res == 3:
        print("*****************************")
        print("***                       ***")
        print("*** Passed :-)    > 3 <   ***")
        print("***                       ***")
        print("*****************************")
