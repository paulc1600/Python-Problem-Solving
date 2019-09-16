#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: Prctice
#  Purpose: Simple text file reader
#
# ---------------------------------------------------------------------
#  PPC | 08/21/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# File is file_IO1.py 
def readMe():
    print("In Lines -------------------")
    with open('workfile.txt', 'r') as f:
        lidx = 0
        for line in f:
            lidx = lidx + 1
            # Suppress print() LF else get LF from file data itself
            #  Use NULL string end instead of space or lines are squeued
            print("Line ", lidx, " = ", line, end = "")
        f.closed   

    print()
    print()
    print("In Chunks -------------------")
    with open('workfile.txt', 'r') as f:
        cidx = 0
        chunk = " "
        while chunk != "":
            cidx = cidx + 1

            chunk = f.read(20)
            print("Chunk ", cidx, " = ", chunk)
        f.closed

    print()
    print()
    print("Using readline() -------------------")
    with open('workfile.txt', 'r') as f:
        cidx = 1
        line = f.readline()
        while line != "":
            # Suppress print() LF else get LF from file data itself
            #  Use NULL string end instead of space or lines are squeued
            print("Line ", cidx, " = ", line, end = "")
            # Stop before null line, since last read data line has no LF! 
            cidx = cidx + 1
            line = f.readline()
        f.closed   
    return
                
if __name__ == '__main__':
    print()
    res = readMe()

