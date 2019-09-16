#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: geeksforgeeks
#  Purpose: Python zip demo
# ---------------------------------------------------------------------
#  PPC | 09/06/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# Python code to demonstrate the working of  
# zip()
mapped_list = []
  
# initializing lists 
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 
  
# printing resultant values as set conversion
mapped = zip(name, roll_no, marks)
mapped2 = set(mapped)
print("The zipped result as a set: ")
for n in mapped2:
    print(n)

# printing resultant values as list conversion 
mapped3 = zip(name, roll_no, marks)
print("The zipped result as a list: ")
for m in mapped3:
    mapped_list.append(m)
print(mapped_list)
print(mapped_list[2])
print(mapped_list[2][0])

# Can you zip a string and numbers
strLow = "abcdefghijklmnopqrstuvwxyz"
strHigh = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
newStrM = zip(strLow, strHigh)
newStr = ""
for c in newStrM:
    newStr = newStr + str(c[0])+ str(c[1])
print(newStr)







