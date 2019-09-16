#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Two cats and a mouse are at various positions on a line.
#           You will be given their starting positions. Your task is
#           to determine which cat will reach the mouse first, assuming
#           the mouse doesn't move and the cats travel at equal speed.
#           If the cats arrive at the same time, the mouse will be
#           allowed to move and it will escape while they fight. 
#           
#           You are given q queries in the form of x, y, and z
#           representing the respective positions for cats A and B,
#           and for mouse C.
# ---------------------------------------------------------------------
#  PPC | 09/10/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys


# Who got the mouse?
def catAndMouse(x, y, z):
    catAdist = abs(z - x)                  
    catBdist = abs(z - y)
    result = ""
    
    if catAdist < catBdist:
        result = "Cat A"
    elif catAdist > catBdist:
        result = "Cat B"
    elif catAdist == catBdist:
        result = "Mouse C"

    return result


if __name__ == '__main__':
    x, y, z = [1, 2, 3]
    result = catAndMouse(x, y, z)
    print(result)
    
    x, y, z = [1, 3, 2]
    result = catAndMouse(x, y, z)
    print(result)
    


