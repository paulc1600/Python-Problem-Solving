#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: The Utopian Tree goes through 2 cycles of growth every
#           year. Each spring, it doubles in height. Each summer, its
#           height increases by 1 meter.
#           
#           Laura plants a Utopian Tree sapling with a height of 1
#           meter at the onset of spring. How tall will her tree be
#           after n growth cycles?
# ---------------------------------------------------------------------
#  PPC | 09/17/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys


# Tree height calculation
def utopianTree(n):
    height = 0
    heightOld = 0

    for cycle in range(-1, n + 1):
        if cycle % 2 == 0:
            height = heightOld + 1   # Summer or planted before spring
        else:
            height = heightOld * 2   # Spring

        # print(cycle, height)
        heightOld = height

    return height


if __name__ == '__main__':
    n = 0
    result = utopianTree(n)
    print(result)
    n = 1
    result = utopianTree(n)
    print(result)
    n = 4
    result = utopianTree(n)
    print(result)
    n = 58
    result = utopianTree(n)
    print(result)




          
          
