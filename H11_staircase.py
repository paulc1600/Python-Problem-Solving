#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Consider a staircase of size n:
#               #
#              ##
#             ###
#            ####
#
#           Observe that its base and height are both equal to n, and
#           the image is drawn using # symbols and spaces. The last
#           line is not preceded by any spaces.
#
#           Write a program that prints a staircase of size n.
#
#           Function Description
#           Complete the staircase function in the editor below. It
#           should print a staircase as described above. staircase has
#           the following parameter(s):
#                  o  n: an integer
#
# ---------------------------------------------------------------------
#  PPC | 08/26/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# Print a staircase where the image is drawn using # symbols and spaces.
def staircase(MySteps):
    air_fill = ' '
    for step in range(MySteps):
        step_len = step + 1 
        wood_step = step_len * '#' 
        whole_step = wood_step.rjust(MySteps, air_fill)
        print(whole_step)
  
if __name__ == '__main__':
    n = 15
    result = staircase(n)

    
