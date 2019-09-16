#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Simple if
#
# ---------------------------------------------------------------------
#  PPC | 08/12/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def myControl():

    x = int(input("Please enter an integer: "))

    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')
    
# Read input testcase file 
if __name__ == '__main__':	
    result = myControl()

