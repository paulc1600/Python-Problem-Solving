#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: A jail has a number of prisoners and a number of treats to
#           pass out to them. Their jailer decides the fairest way to
#           divide the treats is to seat the prisoners around a
#           circular table in sequentially numbered chairs. A chair
#           number will be drawn from a hat. Beginning with the
#           prisoner in that chair, one candy will be handed to each
#           prisoner sequentially around the table until all have been
#           distributed.
#           
#           The jailer is playing a little joke, though. The last piece
#           of candy looks like all the others, but it tastes awful.
#           Determine the chair number occupied by the prisoner who will
#           receive that candy.
# ---------------------------------------------------------------------
#  PPC | 09/07/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys


# How many total shares
def saveThePrisoner(prisoners, sweets, sChair):
    chairsRem = prisoners - sChair + 1   # Still need a sweet
    sweetsRem = sweets                   # Candies left over
    lastChair = 0
    firstR = 0
    fullR = 0
    lastR = 0

    # Less sweets than remaining chairs
    if sweetsRem <= chairsRem:
        lastChair = sChair + sweetsRem - 1   # Gets bad candy
        sweetsRem = 0                        # Dist rest in this round
    else:
        # More sweets than remaining chairs
        if sChair != 1:
            firstR = chairsRem            
        sweetsRem = sweetsRem - firstR
        
        fullR = sweetsRem // prisoners
        sweetsRem = sweetsRem - (fullR * prisoners)
        
        if sweetsRem != 0:        
            lastR = sweetsRem % prisoners
            sweetsRem = sweetsRem - lastR
            lastChair = lastR
        else:
            lastR = 0
            sweetsRem = 0
            lastChair = prisoners

    # Test Code ----------------
    pStr = ""
    sStr = ""
    for n in range(1, prisoners+1):
        if n <= 9:
            pStr = pStr + "|-" + str(n) + "-"                
        else:
            pStr = pStr + "|-" + str(n) + ""
        if sChair == n:
            sStr = sStr + "****"  
        else:
            sStr = sStr + "    "

    print(pStr)
    print(sStr)
    print("Sweets = ", sweets)
    print()
    print("Rem Sweets = ", sweetsRem, " Chairs rem = ", chairsRem)
    print("firstR fullR lastR = ", firstR, fullR * prisoners, lastR)
    print("lastChair = ", lastChair) 
    # Test Code ----------------
    
    return lastChair

if __name__ == '__main__':
    n = 7
    m = 19
    s = 2
    result = saveThePrisoner(n, m, s)
    print(result)
    n = 3
    m = 7
    s = 3
    result = saveThePrisoner(n, m, s)
    print(result)


