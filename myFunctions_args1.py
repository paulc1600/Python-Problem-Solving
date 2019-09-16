#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
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
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

    
# I want that 4th carrier.
# This is not the main body 
if __name__ == '__main__':
    # giving only the mandatory argument
    ask_ok('Do you really want to quit?')
    # giving one of the optional arguments
    ask_ok('OK to overwrite the file?', 2)
    # giving all arguments:
    ask_ok('OK to erase the server?', 2, 'Come on, only yes or no!') 
    
    


