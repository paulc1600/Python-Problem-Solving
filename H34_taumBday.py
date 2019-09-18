#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Taum is planning to celebrate the birthday of his friend,  
#           Diksha. There are two types of gifts that Diksha wants
#           from Taum: one is black and the other is white. To make
#           her happy, Taum has to buy b black gifts and w white
#           gifts. 
#           
#           -- The cost of each black gift is bc units. 
#           -- The cost of every white gift is wc units. 
#           -- The cost of converting each black gift into white gift
#              or vice versa is z units. 
#           
#           Help Taum by deducing the minimum amount he needs to spend
#           on Diksha's gifts.
# ---------------------------------------------------------------------
#  PPC | 09/17/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys


# Optimize for least cost given gift payload / all costs
def taumBday(b, w, bc, wc, z):
    tWc = 1000000000        # Total white cost
    tBc = 1000000000        # Total black cost
    result = 1000000000

    # 3 possible paths -- black is cheaper, or white or neither
    if bc + z < wc:
        # black cost is cheaper
        tWc = (bc + z) * w
        tBc = bc * b
    elif wc + z < bc:
        # white gifts are cheaper
        tBc = (wc + z) * b
        tWc = wc * w
    else:
        tWc = wc * w
        tBc = bc * b

    result = tBc + tWc
    return result


if __name__ == '__main__':
    b = 10
    w = 10
    bc = 1
    wc = 1
    z = 1
    result = taumBday(b, w, bc, wc, z)
    print(result)
    b = 5
    w = 9
    bc = 2
    wc = 3
    z = 4
    result = taumBday(b, w, bc, wc, z)
    print(result)
    b = 3
    w = 6
    bc = 9
    wc = 1
    z = 1
    result = taumBday(b, w, bc, wc, z)
    print(result)
    b = 7
    w = 7
    bc = 4
    wc = 2
    z = 1
    result = taumBday(b, w, bc, wc, z)
    print(result)
    b = 3
    w = 3
    bc = 1
    wc = 9
    z = 2
    result = taumBday(b, w, bc, wc, z)
    print(result)



          
          
