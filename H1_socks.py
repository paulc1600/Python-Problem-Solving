#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: John works at a clothing store. He has a large pile of socks  
#           that he must pair by color for sale. Given an array of 
#           integers representing the color of each sock, determine how 
#           many pairs of socks with matching colors there are.
#
#           For example if there are n = 7 socks in the box and they have
#           colors ar = [1,2,1,2,1,3,2], then there are one pair of color 
#           1 and one pair of color 2 and three odd socks left. So the 
#           number of pairs for sale is 2.   
#
#  Testcase File:    input\input00.txt, or input\input08.txt
#  Results File:     output\output00.txt, or output\output08.txt
#
# ---------------------------------------------------------------------
#  PPC | 08/15/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

ar = []
n = 0

# Complete the sockMerchant function below.
def sockMerchant(size, pile):
    # Initialize Socks Inventory List sil[total]
    sil = [0]
    for i in range(1,101):
        sil.append(0)

    # Examine pile / box contents and determine inventory
    color = 0
    
    # Check for valid sock colors
    if size > 0 and size <= 100:
        # Update inventory counts
        for color in pile:
            sil[color] = sil[color] + 1
            
        # Calculate total pairs
        tpairs = 0
        for j in range(1,101):
            if sil[j] >= 1:
                tpairs = tpairs + (sil[j] // 2) 
                print("Color ", j, " total ", sil[j], " pairs: ", sil[j] // 2)
    else:
        print("Pile size of ", size, " is invalid!")
        tpairs = 0

    # Dump Inventory -- debug code purposes
    # print(sil)

    return tpairs

# Read input testcase file data 
if __name__ == '__main__':
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    print(n)
    print(ar)
    npairs = sockMerchant(n, ar)
    print(npairs)

	
