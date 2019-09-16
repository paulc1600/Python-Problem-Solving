#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: Python 3.6.4
#  Purpose: Functions
#
# ---------------------------------------------------------------------
#  PPC | 08/13/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# the following function accumulates the arguments passed to it on
#    subsequent calls:
def facc(a, L=[]):
    L.append(a)
    return L


# main body 
if __name__ == '__main__':
    print(facc(1))
    print(facc(2))
    print(facc(3))

        


