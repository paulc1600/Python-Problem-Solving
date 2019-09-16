#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: John works at a clothing store. He has a large pile of socks  
#           that he must pair by color for sale. Given an array of 
#           integers representing the color of each sock, determine how 
#           many pairs of socks with matching colors there are.
#
#           For example if there are n = 7 socks in the box and they have
#           colors ar = [1,2,1,2,1,3,2], then there are one pair of color 
#           1 and one pair of color 2 and three odd socks left. So the 
#           number of pairs for sale is 2.   
#
# ---------------------------------------------------------------------
#  PPC | 08/16/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    altitude = 0         # Altitude in "height units"
    nMtns = 0            # Total mountains this hike
    nValleys = 0         # Total valleys this hike
    locate = 0           # "State" of the hike 

    def seaLevel(mystep):
        mylocate = locate
        myaltitude = altitude
        myvalleys = nValleys
        
        if mystep == "U":
            myaltitude = myaltitude + 1
            mylocate = 1   # Start up a mountain 
        elif mystep == "D":
            myaltitude = myaltitude - 1
            mylocate = 2   # Start down into valley
        return mylocate, myvalleys 
     
    def onMountain(mystep):
        mylocate = locate
        myaltitude = altitude
        myvalleys = nValleys
        
        if mystep == "U":
            myaltitude = myaltitude + 1
            mylocate = 1   # On the mountain 
        elif mystep == "D":
            myaltitude = myaltitude - 1   # Climbing down off mountain
            if myaltitude == 0:
                mylocate = 0   
                # nMtns = nMtns + 1     # Completed the Mountain
            else:
                mylocate = 1          # Need to descend further
        else:
            print("Undefined step type: ", step)
            mylocate = 1
        return mylocate, myvalleys
     
    def inValley(mystep):
        mylocate = locate
        myaltitude = altitude
        myvalleys = nValleys
       
        if mystep == "U":
            myaltitude == myaltitude + 1
            if myaltitude == 0:
                mylocate = 0   
                myvalleys = myvalleys + 1   # Completed the valley
            else:
                mylocate = 2              # Need to climb further
        elif mystep == "D":
            myaltitude = myaltitude - 1       # In the valley
        else:
            print("Undefined step type: ", step)
            mylocate = 2
        return mylocate, myvalleys
     
    switcher = {
            0: seaLevel,
            1: onMountain,
            2: inValley
        }

    def get_state(mylocate, mystep):
        flocate = switcher.get(mylocate, "nothing")
        # Depending on locate, can be seaLevel, onMountain, or InValley
        mylocate, myValleys = flocate(mystep)
        return mylocate, myValleys

    # Start Hike at seaLevel
    locate = get_state(0, "S")
    
    # Take the hike
    for step in s:
        newlocate, newValleys = get_state(locate, step)
        locate = newlocate
        nValleys = newValleys
            
    return nValleys    

if __name__ == '__main__': 
    n = 8
    s = ["U", "D", "D", "D", "U", "D", "U", "U"]
    print(n)
    print(s)
    result = countingValleys(n, s)
    print(str(result) + '\n')
    
