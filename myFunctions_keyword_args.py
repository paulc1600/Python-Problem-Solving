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
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print()

# main body 
parrot(1000)                                           # 1 positional argument
parrot(voltage=1000)                                   # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')              # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
parrot(120, 'deep-fried', action='sing', type='Singed-Tail Short-Lived Smoked Parrot')

        


