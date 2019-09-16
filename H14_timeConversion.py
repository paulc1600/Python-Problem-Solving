#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Convert input string of 12 H time to military 24 hour time
#
# ---------------------------------------------------------------------
#  PPC | 08/26/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# Convert time to military time 
def timeConversion(MyTime):
    #             0123456789
    # str_time = "07:05:45PM"
    MilTime = ""
    
    ohour = MyTime[0:2]
    omas = MyTime[2:8]
    amPM = MyTime[8:]

    if amPM == "AM":
        if ohour == "12":            
            MilTime = "00" + omas        # 12 Hour -- Midnight
        else:
            MilTime = ohour + omas       # 12 Hour -- in Morning -- strip AM/PM     
    else:
        if ohour == "12":
            MilTime = ohour + omas       # 12 Hour -- Noon -- strip out AM/PM
        else:
            MilHour = str(int(ohour) + 12)
            MilTime = MilHour + omas     # 12 Hour -- afternoon / night (+12)

    return MilTime

      
if __name__ == '__main__':
    str_time = "11:59:00PM"
    print(str_time)
    result = timeConversion(str_time)
    print(result)

    
