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

# Any label preceeded by * collects positional arg values
# Any label preceeded by ** collects keyword pairs / tuples 
def cheeseshop(kind, *xarguments, **xkeywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in xarguments:
        print(arg)
        
    # Makes the line in output
    print("-" * 40)
    
    for kw in xkeywords:
        print(kw, ":", xkeywords[kw])


# main body 
cheeseshop("Steering Wheels", "They are very stiff, sir.",
           "They are really quite impossible to turn, sir.",
           catalog="1972 Pinto Parts",
           part="Steering Assembly",
           maker="Ford")


        


