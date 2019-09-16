#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Maria plays college basketball and wants to go pro. Each
#           season she maintains a record of her play. She tabulates
#           the number of times she breaks her season record for most
#           points and least points in a game. Points scored in the
#           first game establish her record for the season, and she
#           begins counting from there.
#           
#           For example, assume her scores for the season are
#           represented in the array  scores = [12, 24, 10, 24]. 
#           Max Tot = 1, Min Tot = 1
# ---------------------------------------------------------------------
#  PPC | 08/31/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# INtegers between array
def breakingRecords(Myscores):
    MinTot = 0
    MaxTot = 0
    MinVal = 0
    MaxVal = 0
    
    # Lists have at least one element
    gameCnt = 0
    for score in Myscores:
        gameCnt = gameCnt + 1
        if gameCnt == 1:
            MinVal = score
            MaxVal = score
        elif score < MinVal:
            # Maria hits a new low for season!   
            MinVal = score
            MinTot = MinTot + 1
        elif score > MaxVal:
            # Maria achieves an all time best!
            MaxVal = score
            MaxTot = MaxTot + 1
        else:
            pass
          
    return [MaxTot, MinTot]

      
if __name__ == '__main__':
    # n = 10
    # scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
    n = 9
    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    result = breakingRecords(scores)
    print(result)


    
