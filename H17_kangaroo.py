#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: You are choreographing a circus show with various animals.
#           For one act, you are given two kangaroos on a number line
#           ready to jump in the positive direction (i.e, toward
#           positive infinity).
#           	o The first kangaroo starts at location x1 and moves
#                  at a rate of v1 meters per jump.
#           	o The second kangaroo starts at location x2 and moves
#                  at a rate of v2 meters per jump.
#           
#           You have to figure out a way to get both kangaroos at the
#           same location at the same time as part of the show. If it
#           is possible, return YES, otherwise return NO.
# ---------------------------------------------------------------------
#  PPC | 08/30/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# J = (x2 - x1) / (v1 - v2)
#   where J is positive jump where kangaroos are together
#   if J is negative then starting conditions mean never catch up
def kangaroo(x1, v1, x2, v2):
    if (v1 != v2):
        jump = (x2 - x1) // (v1 - v2)
        rem = (x2 - x1) % (v1 - v2)
        print("Kangaroo 1 starts at ", x1, " and jumps ", v1, " m/j.")
        print("Kangaroo 2 starts at ", x2, " and jumps ", v2, " m/j.")
        print("Magic jump is ", jump, rem)
    elif (x1 == x2):
        jump = 0
        rem = 0
        # Kangaroos jump in synch, and both start from same spot
        print("Kangaroo 1 starts at ", x1, " and jumps ", v1, " m/j.")
        print("Kangaroo 2 starts at ", x2, " and jumps ", v2, " m/j.")
        print("Magic jump is ", jump, rem)
    else:
        jump = -1
        rem = 0
        # Kangaroos jump in synch, and start from different spots
    
    # No jumping backward, and No partial jumps allowed
    if jump >= 0 and rem == 0:
        print("YES")
    else:
        print("NO")
        
    return 

      
if __name__ == '__main__':
    x1 = 0
    v1 = 2
    x2 = 5
    v2 = 3

    result = kangaroo(x1, v1, x2, v2)


    
