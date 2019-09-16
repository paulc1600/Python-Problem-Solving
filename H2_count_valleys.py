#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Gary is an avid hiker. He tracks his hikes meticulously,
#           paying close attention to small details like topography.
#           During his last hike he took exactly n steps. For every
#           step he took, he noted if it was an uphill, U, or a 
#           downhill, D step. Gary's hikes start and end at sea level
#           and each step up or down represents a unit change in
#           altitude. We define the following terms:
#
# 	    -- A mountain is a sequence of consecutive steps above
#              sea level, starting with a step up from sea level
#              and ending with a step down to sea level.
#           -- A valley is a sequence of consecutive steps below 
#              sea level, starting with a step down from sea level
#              and ending with a step up to sea level.
#
#           Given Gary's sequence of up and down steps during his last
#           hike, find and print the number of valleys he walked through.
#
# ---------------------------------------------------------------------
#  PPC | 08/16/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys
import matplotlib.pyplot as plt

amap = []                # Altitude Map

# Complete the countingValleys function below.
def countingValleys(n, s):
    altitude = 0         # Altitude in "height units"
    my_amap = []         # Altitude Map
    nMtns = 0            # Total mountains this hike
    nValleys = 0         # Total valleys this hike
    locate = 0           # "State" of the hike 

    def seaLevel(mystep):
        mylocate = locate
        myaltitude = altitude

        print("Altitude: ", myaltitude, end = ' ')
        
        if mystep == "U":
            myaltitude = myaltitude + 1
            mylocate = 1   # Start up a mountain 
        elif mystep == "D":
            myaltitude = myaltitude - 1
            mylocate = 2   # Start down into valley
            
        return mylocate, myaltitude 
     
    def onMountain(mystep):
        mylocate = locate
        myaltitude = altitude
        mymountains = nMtns

        print("Altitude: ", myaltitude, end = ' ')
        
        if mystep == "U":
            myaltitude = myaltitude + 1
            mylocate = 1   # On the mountain 
        elif mystep == "D":
            myaltitude = myaltitude - 1         # Climbing down off mountain
            if myaltitude == 0:
                mylocate = 0   
                mymountains = mymountains + 1   # Completed the Mountain
            else:
                mylocate = 1                    # Need to descend further
        else:
            print("Undefined step type: ", step)
            mylocate = 1
            
        return mylocate, myaltitude, mymountains
     
    def inValley(mystep):
        mylocate = locate
        myaltitude = altitude
        myvalleys = nValleys

        print("Altitude: ", myaltitude, end = ' ')
       
        if mystep == "U":
            myaltitude = myaltitude + 1
            if myaltitude == 0:
                mylocate = 0   
                myvalleys = myvalleys + 1   # Completed the valley
            else:
                mylocate = 2                # Need to climb further
        elif mystep == "D":
            myaltitude = myaltitude - 1     # In the valley
        else:
            print("Undefined step type: ", step)
            mylocate = 2
            
        return mylocate, myaltitude, myvalleys
    
    # -------------------------------------------------
    #  Take the hike
    # -------------------------------------------------
    my_amap.append(0)
    for step in s:
        # Location 0 = seaLevel
        # Location 1 = onMountain
        # Location 2 = inValley
        
        if locate == 0:
            # Ground level
            locate, altitude = seaLevel(step)
            my_amap.append(altitude)
            print("Step ", step, "  ", end = ' ')
            print("At ground level.  Next is ", locate)
        elif locate == 1:
            # On the mountain
            locate, altitude, nMtns = onMountain(step)
            my_amap.append(altitude)
            print("Step ", step, "  ", end = ' ')
            print("On mountain.  Next is ", locate, " Total M = ", nMtns)
        elif locate == 2:
            # In the valley
            locate, altitude, nValleys = inValley(step)
            my_amap.append(altitude)
            print("Step ", step, "  ", end = ' ')
            print("In a valley.  Next is ", locate, " Total V = ", nValleys)
        else:
            print("Step ", step, "  ", end = ' ')
            print("You are lost: ", locate)
            locate = 0
            nValleys = 0
            break
            
    return nValleys, my_amap    

if __name__ == '__main__': 
    n = 8
    s = ["U", "D", "D", "D", "U", "D", "U", "U"]
    print(n)
    print(s)
    result, amap = countingValleys(n, s)
    print(str(result) + '\n')
    plt.plot(amap)
    plt.ylabel('Hike Altitude Elements')
    plt.show()
    
