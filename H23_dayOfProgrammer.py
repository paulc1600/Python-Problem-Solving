#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Marie invented a Time Machine and wants to test it by
#           time-traveling to visit Russia on the Day of the 
#           Programmer (the 256th day of the year) during a year in the
#           inclusive range from 1700 to 2700. From 1700 to 1917,
#           Russia's official calendar was the Julian calendar; since
#           1919 they used the Gregorian calendar system. The transition
#           from the Julian to Gregorian calendar system occurred in 
#           1918, when the next day after January 31s was February 14th.
#           This means that in 1918, February 14th was the 32nd day of
#           the year in Russia. 
#           
#           In both calendar systems, February is the only month with a
#           variable amount of days; it has 29 days during a leap year,
#           and 28 days during all other years. In the Julian calendar,
#           leap years are divisible by 4; in the Gregorian calendar,
#           leap years are either of the following: 
#               o  Divisible by 400. 
#               o  Divisible by 4 and not divisible by 100. 
#           
#           Given a year, y, find the date of the 256th day of that year
#           according to the official Russian calendar during that year.
#           Then print it in the format dd.mm.yyyy, where dd is the
#           two-digit day, mm is the two-digit month, and yyyy is y. 
# ---------------------------------------------------------------------
#  PPC | 09/03/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys
import datetime
# The calendar module automatically takes into account leap years.
from calendar import monthrange

# Years can be any number 1700 - 2700
def dayOfProgrammer(myYear):
    num_days = 0

    if myYear >= 1700 and myYear <= 1917:
        # Pure Julian: leap year is only divisible by 4
        if myYear % 4 == 0:
            num_days = 31 + 29
        else:
            num_days = 31 + 28
        for mIdx in range(3, 9):
            num_days = num_days + monthrange(myYear, mIdx)[1]
            
    elif myYear == 1918:
        # 1918 was Russian Julian / Gregorian transition year 
        #  and was not a leap year
        num_days = 31 + 15
        for mIdx in range(3, 9):
            num_days = num_days + monthrange(myYear, mIdx)[1]   # days in month
    
    elif myYear > 1918:
        # Pure Gregorian: just call month range
        for mIdx in range(1, 9):
            num_days = num_days + monthrange(myYear, mIdx)[1]   # days in month
        
    dop = 256 - num_days
    myDate = '{num:02d}'.format(num = dop) + ".09." + str(myYear)

    
    # timeStr = str(myYear) + " " + "256"                    # 256th day of year
    # myTime = datetime.datetime.strptime(timeStr, '%Y %j')
    # fmTime = myTime.strftime('%d.%m.%Y')                   # 13.09.2001                    
    return myDate
      
if __name__ == '__main__':
    # year = 1984                         
    # year = 1800                        
    year = 1918                           
    result = dayOfProgrammer(year)
    print(result)


    
