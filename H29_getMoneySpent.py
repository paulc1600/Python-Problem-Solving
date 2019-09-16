#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Monica wants to buy a keyboard and a USB drive from her
#           favorite electronics store. The store has several models
#           of each. Monica wants to spend as much as possible for the
#           2 items, given her budget. Given the price lists for the
#           store's keyboards and USB drives, and Monica's budget, find
#           and print the amount of money Monica will spend. If she
#           doesn't have enough money to both a keyboard and a USB
#           drive, print -1 instead. She will buy only the two required
#           items. 
#           
#           For example, suppose she has b = 60 to spend. Three types
#           of keyboards cost [40, 50, 60]. Two USB drives cost drives
#           [5, 8, 12]. She could purchase a 40 keyboard + 12 USB drive
#           = 52, or a 50 keyboard + 8 USB drive = 58. She chooses the
#           latter. She can't buy more than 2 items so she can't spend
#           exactly 60. 
# ---------------------------------------------------------------------
#  PPC | 09/09/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys


# How much can she spend on two items or nothing
def getMoneySpent(keyboards, drives, b):
    spent = -1                   # total money spent
    lenK = len(keyboards)
    pn = 0                       # purchase number

    keyboards.sort(reverse=True)
    drives.sort(reverse=True)

    print(keyboards, drives)
    done_shop = False
    big_p = 0                    # Biggest purchase so far
    
    for pn in range(0, lenK):
        k = keyboards[pn]
        print("PN = ", pn, " Keyboard = ", k)

        if done_shop == False:
            for d in drives:
                print("  Keyboard = ", k, " Drive = ", d, " Budget = ", b)
                if k + d == b:
                    big_p = b
                    done_shop = True
                    print("    Big P = ", big_p, "Done ? ", done_shop)
                    break
                elif k + d > b:
                    pass
                elif k + d < b:
                    if k + d > big_p:
                        big_p = k + d
                    if pn == lenK - 1:
                        done_shop = True
                        print("    Big P = ", big_p, "Done ? ", done_shop)
                        break
                    else:
                        print("    Big P = ", big_p, "Done ? ", done_shop)                       
                                
    if done_shop:
        spent = big_p

    print(spent)                
    return


if __name__ == '__main__':
    keyboards = [3, 1]
    drives = [5,2,8]
    b = 10
    result = getMoneySpent(keyboards, drives, b)
    print()
    
    keyboards = [4]
    drives = [5]
    b = 5
    result = getMoneySpent(keyboards, drives, b)
    print()
    
    keyboards = [40, 60, 50]
    drives = [5, 8, 12]
    b = 60
    result = getMoneySpent(keyboards, drives, b)


