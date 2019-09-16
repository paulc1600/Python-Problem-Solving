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


# How many beautiful days - so can go to the movies
def beautifulDays(sDay, eDay, myDiv):
    totDays = 0

    for dayI in range(sDay, eDay+1):
        strDayI = str(dayI)
        lenSD = len(strDayI)
        strDayF = strDayI[lenSD::-1]
        dayF = int(strDayF)
        # Is it beautiful ?
        if abs(dayI - dayF) % myDiv == 0:
            totDays += 1
        
            
    return totDays
      
if __name__ == '__main__':
    i = 13
    j = 45                    
    k = 3
    result = beautifulDays(i, j, k)
    print(result)


    
