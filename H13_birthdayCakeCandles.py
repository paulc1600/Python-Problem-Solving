#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: You are in charge of the cake for your niece's birthday
#           and have decided the cake will have one candle for each
#           year of her total age. When she blows out the candles,
#           she’ll only be able to blow out the tallest ones. Your task
#           is to find out how many candles she can successfully blow
#           out.
#
#           For example, if your niece is turning 4 years old, and the
#           cake will have  candles of height 4, 4, 1, 3, she will be
#           able to blow out 2 candles successfully, since the tallest
#           candles are of height  and there are such candles.
#
# ---------------------------------------------------------------------
#  PPC | 08/26/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# Want number of tallest candles -- that she can blow 
def birthdayCakeCandles(MyArr):
    # Find tallest candle
    tcandle = max(MyArr)

    # How many of this candle on cake?
    nbr_candles = MyArr.count(tcandle)

    return nbr_candles

      
if __name__ == '__main__':
    n = 4
    arr = [3, 2, 1, 3]
    print(arr)
    result = birthdayCakeCandles(arr)
    print(result)

    
