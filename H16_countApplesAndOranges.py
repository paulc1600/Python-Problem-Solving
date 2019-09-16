#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Sam's house has an apple tree and an orange tree that
#           yield an abundance of fruit.
#
#           For example, Sam's house is between s = 7 and t = 10. The
#           apple tree is located at a = 4 and the orange at b = 12.
#           There are m = 3 apples and n = 3 oranges. Apples are thrown
#           apples = [2, 3, -4] units distance from a, and oranges =
#           [3, -2, -4] units distance. Adding each apple distance to
#           the position of the tree, they land at [4 + 2, 4 + 3, 4 + -4]
#           = [6, 7, 0]. Oranges land at [12+3, 12+-2, 12+-4] = [15, 10, 8].
#           One apple and two oranges land in the inclusive range 7 - 10
#           so we print 
#           1
#           2
# ---------------------------------------------------------------------
#  PPC | 08/30/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(houseB, houseT, aTree, ojTree, applesD, orangesD):
    nbrApplesHit = 0
    nbrOrangesHit = 0

    # Check for Apples First
    if len(applesD) > 0:
        for apple in applesD:
            hitLoc = aTree + apple
            if hitLoc >= houseB and hitLoc <= houseT:
                nbrApplesHit = nbrApplesHit + 1
    else:
        # No apples on tree
        nbrApplesHit = 0

    # Check for Oranges
    if len(orangesD) > 0:
        for orange in orangesD:
            hitLoc = ojTree + orange
            if hitLoc >= houseB and hitLoc <= houseT:
                nbrOrangesHit = nbrOrangesHit + 1
    else:
        # No oranges on tree
        nbrOrangesHit = 0
        
    print(nbrApplesHit)
    print(nbrOrangesHit)
    return 

      
if __name__ == '__main__':
    s = 7
    t = 11
    a = 5
    b = 15
    apples = [-2, 2, 1]    # Distance relative to Apple tree 
    oranges = [5, -6]      # Distance relative to Orange tree 
    countApplesAndOranges(s, t, a, b, apples, oranges)


    
