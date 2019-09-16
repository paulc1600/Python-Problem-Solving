#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: You have been asked to help study the population of birds
#           migrating across the continent. Each type of bird you are
#           interested in will be identified by an integer value. Each
#           time a particular kind of bird is spotted, its id number
#           will be added to your array of sightings. You would like
#           to be able to find out which type of bird is most common
#           given a list of sightings. Your task is to print the type
#           number of that bird and if two or more types of birds are
#           equally common, choose the type with the smallest ID
#           number.
# ---------------------------------------------------------------------
#  PPC | 09/02/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# migration
def migratoryBirds(myArr):
    migStats = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    maxBird = 0
    maxCount = 0
    
    for birdType in myArr:
        migStats[birdType] = migStats[birdType] + 1
        
        if migStats[birdType] > maxCount:
            maxBird = birdType
            maxCount = migStats[birdType]
        elif migStats[birdType] == maxCount and birdType < maxBird:
            maxBird = birdType
                          
    return maxBird

      
if __name__ == '__main__':
    n = 6
    # ar = [1, 4, 4, 4, 5, 3]
    # result = migratoryBirds(ar)
    ar = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
    result = migratoryBirds(ar)
    # ar = [5, 5, 2, 2, 1, 1]
    # result = migratoryBirds(ar)    
    print(result)


    
