#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: HackerLand Enterprise is adopting a new viral advertising
#           strategy. When they launch a new product, they advertise it
#           to exactly  people 5 on social media. On the first day,
#           half of those  people (i.e., 5 // 2 = 2  ) like the
#           advertisement and each shares it  with 3 of their friends.
#           At the beginning of the second day, 2 x 3  people receive
#           the advertisement.
#
#           For example, assume you want to know how many have liked
#           the ad by the end of the 5th day.
#
#           The cumulative number of likes is 24 .
# ---------------------------------------------------------------------
#  PPC | 09/05/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys


# How many total shares
def viralAdvertising(campDays):
    totShares = 5   # Initial ad distribution
    totCum = 0      # Cum Likes
    dayNlikes = 0

    for dayI in range(1, campDays+1):
        dayNlikes = totShares // 2   # Only half of dist likes Ad
        totCum = totCum + dayNlikes
        print(dayI, "\t", totShares, "\t", dayNlikes, "\t", totCum)
        totShares = dayNlikes * 3    # Likers always share with 3 friends


    return totCum

if __name__ == '__main__':
    n = 50
    result = viralAdvertising(n)
    print(result)



