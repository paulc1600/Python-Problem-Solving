#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Find lowest cost solution (elements need minimum changes
#           to create magic square from input 3 x 3 array integers.
#           
# ---------------------------------------------------------------------
#  PPC | 09/12/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

global magicSolutions

# Load a single 3 x 3 square into solutions array
def loadSquare(sinput, n):
    global magicSolutions
    usedIdx = n

    for ridx in range(3):
        for cidx in range(3):
            magicSolutions[n][ridx][cidx] = sinput[cidx + (3 * ridx)]

    return usedIdx


# Total up all sides
def squareChecker(sinput, n):
    # Sums r0, r1, r2, c0, c1, c2, dlr, drl
    ssums = 0
    IsMagic = False
    
    for ridx in range(3):
        if (sinput[n][ridx][0] + sinput[n][ridx][1] + sinput[n][ridx][2]) == 15:            
            ssums = ssums + 1
    for cidx in range(3):
        if (sinput[n][0][cidx] + sinput[n][1][cidx] + sinput[n][2][cidx]) == 15:
            ssums = ssums + 1
    if (sinput[n][0][0] + sinput[n][1][1] + sinput[n][2][2]) == 15:
        ssums = ssums + 1
    if (sinput[n][0][2] + sinput[n][1][1] + sinput[n][2][0]) == 15:
        ssums = ssums + 1
    if ssums == 8:
        IsMagic = True

    return IsMagic


# Cost calculator. Lowest cost will be best solution
def costCalculator(sinput):
    global magicSolutions
    snbr = 0
    lowCost = 999
    print()
    
    for snbr in range(8):
        eCost = 0
        for ridx in range(3):
            for cidx in range(3):
                eCost = eCost + abs(sinput[ridx][cidx] - magicSolutions[snbr][ridx][cidx])

        if eCost < lowCost:
            lowCost = eCost
        print("Solution ", snbr, " has cost ", eCost)
        
    return lowCost


# What does it take to restore array back to 3 x 3 magic square 
def formingMagicSquare(s):
    global magicSolutions
    chkIdx = 0
    result = 0
    testme = False

    # 3D Array of 8 x 3 x 3 -- will hold all possible 3 x 3 magic squares
    magicSolutions = [[[0 for k in range(3)] for j in range(3)] for i in range(9)]

    if testme:
        print("Input square is: ", s)
        print()

    # Load up all magic square 3 x 3 solutions
    onePattern = [8, 1, 6, 3, 5, 7, 4, 9, 2]
    loadSquare(onePattern, 0)
    onePattern = [6, 1, 8, 7, 5, 3, 2, 9, 4]
    loadSquare(onePattern, 1)
    onePattern = [4, 3, 8, 9, 5, 1, 2, 7, 6]
    loadSquare(onePattern, 2)
    onePattern = [2, 7, 6, 9, 5, 1, 4, 3, 8]
    loadSquare(onePattern, 3)
    onePattern = [4, 9, 2, 3, 5, 7, 8, 1, 6]
    loadSquare(onePattern, 4)
    onePattern = [2, 9, 4, 7, 5, 3, 6, 1, 8]
    loadSquare(onePattern, 5)
    onePattern = [8, 3, 4, 1, 5, 9, 6, 7, 2]
    loadSquare(onePattern, 6)
    onePattern = [6, 7, 2, 1, 5, 9, 8, 3, 4]
    loadSquare(onePattern, 7)

    # Verify 3D solution array
    if testme:
        for chkIdx in range(8):
            if squareChecker(magicSolutions, chkIdx) != True:
                print("Error: solution array contains non-magic square at index ", chkIdx)
            else:
                print(magicSolutions[chkIdx])
                print("                 Solution element ", chkIdx, " is valid.")


    result = costCalculator(s)
    if testme:
        if result == 0:
            print("Input square is already magic! Cost = 0")
            
    return result


if __name__ == '__main__':
    #s = [[8, 3, 4],    8   1   6
    #     [1, 5, 9],    3   5   7
    #     [6, 7, 2]]    4   9   2
    s = [[4, 8, 2],
         [4, 5, 7],
         [6, 1, 6]]
    result = formingMagicSquare(s)
    print(result)
    
    


