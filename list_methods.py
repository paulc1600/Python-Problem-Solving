#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: Python 3.7.4 Help
#  Purpose: List Methods
#
# ---------------------------------------------------------------------
#  PPC | 08/14/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# We can create a function that messes with bunch of fruit.
def listChanges():    # write Fibonacci series up to n
    """Illustrate list methods."""
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    print(fruits)
    print("Count apples is: ", fruits.count('apple'))
    print("Count of tangerines is: ", fruits.count('tangerine'))
    print("Banana index is: ", fruits.index('banana'))
    print("Next Banana is: ", fruits.index('banana', 4))  # Find next banana starting a position 4
    print("Reverse entire list.")
    fruits.reverse()
    print(fruits)
    print("Add grapes.")
    fruits.append('grape')
    print(fruits)
    print("Sort entire list.")
    fruits.sort()
    print(fruits)
    print("Pop one out: ", fruits.pop())

    
# I want that 4th carrier.
# This is not the main body 
if __name__ == '__main__':	
    listChanges()
    print("The End")

