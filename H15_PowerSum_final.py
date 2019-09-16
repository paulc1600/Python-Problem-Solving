#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Find the number of ways that a given integer, X, can be
#           expressed as the sum of the Nth powers of unique, natural
#           numbers. 
#
#           For example, if X = 13 and N = 2, we have to find all
#           combinations of unique squares adding up to 13. The only
#           solution is 2^2 +  3^2
#
#           Function Description 
#           Complete the powerSum function in the editor below. It should return an integer that represents the 
#           number of possible combinations. 
#           
#           powerSum has the following parameter(s): 
#           	o  X: the integer to sum to 
#           	o  N: the integer power to raise numbers to 
#
# ---------------------------------------------------------------------
#  PPC | 08/27/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# --------------------------------------------------
# Sum All elements in an array
def arraySum(MyArr):
    sum = 0
    for element in MyArr:
        sum = sum + element  
    return sum 

# --------------------------------------------------
# Convert subsetsOfSet string to list of lists
def subsetsOfSetConverter(MyList):    
    NewList = []
    
    for subset in MyList: 
        # split the subset create a subset list from elements 
        ssList = subset.split('|')
        NewSubset = []
        for ssListItem in ssList:
            if ssListItem != '':
                NewSubset.append(int(ssListItem))
        NewList.append(NewSubset)

    return NewList
    
# ---------------------------------------------------------------------
# Python3 program to find all subsets of given set. 
# This code is contributed by vibhu4agarwal
# https://www.geeksforgeeks.org/find-distinct-subsets-given-set/
def subsetsOfSet(arr, n): 
    # Any repeated subset is considered only once in the output 
    _list = []
  
    # Run counter i from 000..0 to 111..1 (2**n)
    for i in range(2**n): 
        subset = "" 

        for j in range(n): 
            if (i & (1 << j)) != 0: 
                subset += str(arr[j]) + "|"

        if subset not in _list and len(subset) > 0: 
            _list.append(subset) 
  
    return _list

# ------------------------------------------------------------
# Code to determine all possible sum of powers that result in N
def powerSum(myX, myN):
    arrPowers = []
    all_subsets = []
    all_subsetsList = []
    all_subsetsSum = []

    # Create Array of all powers of myN smaller than myX
    pos = 1
    while pos ** myN <= myX:
        arrPowers.append(pos ** myN)
        pos = pos + 1

    # Calculate all possible subsets
    sizePower = len(arrPowers)
    all_subsets = subsetsOfSet(arrPowers, sizePower)
    
    # Convert list of strings to List of Lists 
    all_subsetsList = subsetsOfSetConverter(all_subsets)

    # Create the list of all subset sums
    ssIdx = 0
    nbrWays = 0
    for subset in all_subsetsList:
        all_subsetsSum.append(arraySum(subset))
        # print(ssIdx, " = ", all_subsetsSum[ssIdx], myX)
        if all_subsetsSum[ssIdx] == myX:
            nbrWays = nbrWays + 1
        ssIdx = ssIdx + 1
   
    return nbrWays

# --------------------------------------------------  
# Driver Code
# --------------------------------------------------
if __name__ == '__main__': 
    X = 100
    N = 2
    result = powerSum(X, N)
    print(result)

