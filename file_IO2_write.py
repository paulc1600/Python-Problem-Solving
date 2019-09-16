#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: Prctice
#  Purpose: Simple text file writer
#
# ---------------------------------------------------------------------
#  PPC | 08/21/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# File is file_IO2_write.py
def makeArray(my_start):
    data_out = []
    rvalue = len(my_start)
    cvalue = len(my_start[0])
    
    for r in range(rvalue):
        nibLine = ""
        for c in range(cvalue):
            element = my_start[r][c]
            ebin = "{0:08b}".format(element)
            nib = str(ebin[0:4]) + " " + str(ebin[4:8])
            if c == 0: 
                nibline = nib
            else:
                nibline = nibline + "   " + nib
        # Otherwise when written to file, 2nd line up adjacent to first 
        data_out.append(nibline + "\n")
    # print(data_out)
    # print()
    return data_out
                
if __name__ == '__main__':
    # Create data in an array so can write to file
    dataLines = []
    start_arr = [[12, 31, 3, 16, 0], [8, 12, 15, 16, 0], [2, 2, 31, 16, 0], [125, 0, 0, 1, 255]]
    dataLines = makeArray(start_arr)
    print()
    
    print("Append to file -------------------")
    with open('workfile.txt', 'a') as fw:
        widx = 0
        bw = 0
        # Otherwise append places new text next to last character in file
        btot = fw.write("\n")
        for writeData in dataLines:
            widx = widx + 1
            bw = fw.write(writeData)
            btot = btot + bw
        fw.closed   

    print(btot, " bytes appended to file.")
