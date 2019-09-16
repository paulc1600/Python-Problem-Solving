#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Given a square matrix, calculate the absolute difference
#           between the sums of its diagonals.
#
#           For example, the square matrix arr is shown below: 
#           
#                  1   2   3       0,0  .,.  0,2
#                  4   5   6       .,.  1,1  .,. 
#                  9   8   9       2,0  .,.  2,2
#           
#           The left-to-right diagonal = 1 + 5 + 9 = 15
#           The right-to-left diagonal = 3 + 5 + 9 = 17 
#           
#           The absolute difference is then |15 - 17| = 2 
#           
#           Function description 
#           Complete the diagonalDifference function in the editor below.
#           It must return an integer representing the absolute diagonal
#           difference. 
#           
#           diagonalDifference takes the following parameter: 
#           o  arr: an array of integers . 
# 
# ---------------------------------------------------------------------
#  PPC | 08/26/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# return an integer representing the absolute diagonal difference.
def diagonalDifference(MyArray):
    ddiff = 0
    dleft = 0
    dright = 0
    col_left = 0
    col_right = 0
    ecnt = len(MyArray)         # Only works if square!
    for row in range(ecnt):
        col_left = row
        col_right = ecnt - 1 - row
        # print("Left = [", row, col_left, "]  Right = [", row, col_right,"]")
        dleft = dleft + MyArray[row][col_left]
        dright = dright + MyArray[row][col_right]

    ddiff = abs(dleft - dright)
    return ddiff 
  
if __name__ == '__main__': 
    arr = [[1,2,3], [4,5,6], [9,8,9]]
    print()
    print(arr)
    result = diagonalDifference(arr)
    print(str(result) + '\n')
    
