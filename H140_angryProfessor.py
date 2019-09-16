#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: The first line of input contains t, the number of test cases. 
#           Each test case consists of two lines. The first line has
#           two space-separated integers, n and k, the number of
#           students (size of a) and the cancellation threshold. The
#           second line contains n space-separated integers
#           (a[1], a[2], .. a[n]) describing the arrival times for each
#           student. 
#           
#           Note: Non-positive arrival times (a[ i] <= 0) indicate the
#           student arrived early or on time; positive arrival times
#           (a[ i] > O) indicate the student arrived a[i] minutes late.  
# ---------------------------------------------------------------------
#  PPC | 09/05/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys


# Will class be held ?
def angryProfessor(minStud, myTimes):
    classCancel = "YES"
    ontime = 0

    for stud in myTimes:
        if stud <= 0:
            ontime += 1
    if ontime >= minStud:
        classCancel = "NO"
            
    return classCancel
      
if __name__ == '__main__':
    k = 2                         
    a = [0, -1, 2, 1]                        
    # k = 3
    # a = [-1, -3, 4, 2]
    result = angryProfessor(k, a)
    print(result)


    
