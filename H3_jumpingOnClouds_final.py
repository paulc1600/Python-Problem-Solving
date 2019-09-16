#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Emma is playing a new mobile game that starts with
#           consecutively numbered clouds. Some of the clouds are
#           thunderheads and others are cumulus. She can jump on any
#           cumulus cloud having a number that is equal to the number
#           of the current cloud plus 1 or 2. She must avoid the 
#           thunderheads.
#
#           Determine the minimum number of jumps it will take Emma to
#           jump from her starting postion to the last cloud. It is
#           always possible to win the game.
#
#           For each game, Emma will get an array of clouds numbered 0
#           if they are safe or 1 if they must be avoided. For example,
#           c = [0, 1, 0, 0, 0, 1, 0] indexed from 0 ... 6. The number
#           on each cloud is its index in the list so she must avoid
#           the clouds at indexes 1 and 5. She could follow the following
#           two paths: 0 -> 2 -> 4 -> 6 or 0 -> 2 -> 3 -> 4 -> 6. 
#
#           The first path takes 3 jumps while the second takes 4.
#           In this case module should return 3.
#
# ---------------------------------------------------------------------
#  PPC | 08/19/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    global sky                 
    global nJumps 
    global locate 

    sky = c              # All clouds in sky   
    nJumps = 0           # Total jumps this game
    locate = 0           # Which cloud user is on
          
    def checkRadar(myLocate):
        global sky                 
        tclouds = len(sky)      # Total Clouds in sky
        c2ndLast = tclouds - 2  # Index 2nd to last cloud
        snjump = 0              # Safe maximum next jump is unknown 
        
        if myLocate == c2ndLast:
            # 1 cloud from end, one jump from end (end cannot be thundercloud)
            snjump = 1
        else:
            # Check cloud 2 over
            if sky[myLocate + 2] == 0:
                snjump = 2
            else:
                # Cannot have back-to-back thunderclouds 
                snjump = 1
                
        return snjump
    
    # -------------------------------------------------
    #  Start the Game
    # -------------------------------------------------
    while locate < len(sky) - 1:
        nJumps = nJumps + 1
        njsize = checkRadar(locate) # Uses locate global
        locate = locate + njsize
        
    return nJumps    

if __name__ == '__main__': 
    n = 7
    c = [0, 0, 1, 0, 0, 1, 0]
    print()
    print(n)
    print(c)
    result = jumpingOnClouds(c)
    print(str(result) + '\n')
    
