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
#  Typical Input:   ['1|', '4|', '1|4|', '9|', '1|9|', '4|9|', '1|4|9|']
#  Produces Output: [[1], [4], [1,4], [9], [1,9], [4,9], [1,4,9]]
def subsetsOfSetConverter(MyList):
    # print()
    # print(MyList)
    
    NewList = []
    
    for subset in MyList: 
        # split the subset create a subset list from elements 
        ssList = subset.split('|')
        NewSubset = []
        for ssListItem in ssList:
            if ssListItem != '':
                NewSubset.append(int(ssListItem))
        NewList.append(NewSubset)

    # print(NewList)
    return NewList
    
# ---------------------------------------------------------------------
# Python3 program to find all subsets of given set. Any repeated subset
# is considered only once in the output
#
# This code is contributed by vibhu4agarwal
# https://www.geeksforgeeks.org/find-distinct-subsets-given-set/
def subsetsOfSet(arr, n): 
    # Any repeated subset is considered only once in the output 
    _list = []
  
    # Run counter i from 000..0 to 111..1 (2**n)
    # For sets of unique numbers the number unique subsets
    #  (including NULL) always 2**n. Python range statement will
    #  drops the null subset from count. 
    
    for i in range(2**n): 
        subset = "" 
        
        # consider each element in the set (n = length arr)
        # Example of n = 3, i = 0 - 7, j = 0 - 2
        #            (1 << j) = 001, 010, 100 
        #   i = 0    000    ___
        #   i = 1    001    __C
        #   i = 2    010    _B_ 
        #   i = 3    011    _BC
        #   i = 4    100    A__
        #   i = 5    101    A_C
        #   i = 6    110    AB_
        #   i = 7    111    ABC
        for j in range(n): 
  
            # Check if jth bit in the i is set.  
            # If the bit is set, we consider  
            # jth element from set 
            if (i & (1 << j)) != 0: 
                subset += str(arr[j]) + "|"

        # Any repeated subset is considered only once in the output
        # if subset is encountered for the first time 
        # If we use set<string>, we can directly insert 
        if subset not in _list and len(subset) > 0: 
            _list.append(subset) 
  
    # consider every subset
    # print(_list)
    # print()
    # for subset in _list: 
    #   # split the subset and print its elements 
    #   arr = subset.split('|') 
    #   for string in arr: 
    #      print(string, end = " ") 
    #   print()

    return _list

# ------------------------------------------------------------
# Code to determine all possible sum of powers that result in N
def powerSum(myX, myN):
    arrPowers = []
    all_subsets = []
    all_subsetsList = []
    all_subsetsSum = []

    # Create Array of all powers of myN smaller than myX
    #  for myN value 2 and myX value 13 would be  [1, 4, 9] 
    pos = 1
    while pos ** myN <= myX:
        arrPowers.append(pos ** myN)
        pos = pos + 1

    # Calculate all possible subsets
    print(arrPowers)
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
        
    print(all_subsetsSum, nbrWays)
   
    return nbrWays

# --------------------------------------------------  
# Driver Code
# --------------------------------------------------
if __name__ == '__main__': 
    X = 800
    N = 2
    print("X = ", X, " N = ", N)
    all_subsets = powerSum(X, N)

