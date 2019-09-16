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

# We can create a function variable number of argtuments (using deaults)
i = 5

def f(arg=i):
    # ignore argument input
    i = 99      # not override -- evaluated when function defined!
    # arg = 99    does override value 
    print(arg)


# main body 
if __name__ == '__main__':
    # giving no argument (5 or 99?)
    f()
        


