#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Find the number of ways that a given integer, X, can be
#           expressed as the sum of the Nth powers of unique, natural
#           numbers. 
#
#           For example, if X = 13 and N = 2, we have to find all
#           combinations of unique squares adding up to 13. The only
#           solution is 2^2 +  3^2
#
#           Function Description 
#           Complete the powerSum function in the editor below. It should return an integer that represents the 
#           number of possible combinations. 
#           
#           powerSum has the following parameter(s): 
#           	o  X: the integer to sum to 
#           	o  N: the integer power to raise numbers to 
#
# ---------------------------------------------------------------------
#  PPC | 08/27/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

from multiprocessing import *

global nbrWays
global sSetLimit

# This code splits 1 huge range into mostly even partions  
# ---------------------------------------------------------------------
def rangeSplitter(myTotal, nbrSplits, rem2end):
    job_ranges = []
    bIdx = 0
    eNbr = 0
    delta = round(myTotal // nbrSplits)
    lint = myTotal % nbrSplits

    # Handle all but last partial split here    
    for bIdx in range(nbrSplits):
        one_range = []
        sNbr = eNbr + 1
        
        if bIdx == 0 and rem2end == False:
            eNbr = eNbr + delta + lint     # First split has extra records
        else:
            eNbr = eNbr + delta
            
        one_range = [sNbr, eNbr + 1]       # Adjust for Python
        job_ranges.append(one_range)

    # Handle myTotal not splitting evenly / create last partial group
    if rem2end == True and eNbr < myTotal:
        sNbr = eNbr + 1
        eNbr = myTotal                     # Last split has extra records
        one_range = [sNbr, eNbr + 1]       # Adjust for Python
        job_ranges.append(one_range)        

    return job_ranges
    
    
# This code based on the original work of vibhu4agarwal
# https://www.geeksforgeeks.org/find-distinct-subsets-given-set/
# ---------------------------------------------------------------------
def processSubsets(myNbr, myJobQueue, myStart, myEnd, myArray, myX):
    global nbrWays

    sizePower = len(myArray)

    jvector = []
    
    # Prepare vector Array One Time
    oneVector = 0b00000000000000000000000000000000
    for jIdx in range(sizePower):
        myVector = oneVector + (2**jIdx)
        jvector.append(myVector)

    print()
    print("Call: ", myNbr, " -------------------------------------")
    print("                Range: ", myStart, myEnd)
    print("       Target for Sum: ", myX)   
    
    for i in range(myStart, myEnd): 
        # consider each element in the set (n = length arr)
        # Example of n = 3, i = 0:7, j = 0:2
        #                   (1 << j) = 001, 010, 100 
        #   i = 0    000    ___
        #   i = 1    001    __C
        #   i = 2    010    _B_ 
        #   i = 3    011    _BC
        #   i = 4    100    A__
        #   i = 5    101    A_C
        #   i = 6    110    AB_
        #   i = 7    111    ABC

        subsetSum = 0
        for j in range(sizePower):  
            # Check if jth bit in the i is set.  
            # If the bit is set, we consider jth element from arrPowers
            #  and sum up it's value into a subset total
            if (i & jvector[j]) != 0:
                subsetSum = subsetSum + myArray[j]

        # Once finish with any subset -- just sum it and check it  
        if subsetSum == myX:
            nbrWays = nbrWays + 1

    myJobQueue.put([myNbr, nbrWays])
    print("Call: ", myNbr, " ---- completed. NbrWays = ", nbrWays)  
    return nbrWays

# ---------------------------------------------------------------------
# Python3 program to find all subsets of given set. Any repeated subset
# is considered only once in the output
#
def powerSum(myX, myN):
    global nbrWays
    global sSetLimit
    
    arrPowers = []
    myJobRanges = []

    # Create Array of all powers of myN smaller than myX
    #  for myN value 2 and myX value 13 would be  [1, 4, 9] 
    pos = 1
    while pos ** myN <= myX:
        arrPowers.append(pos ** myN)
        pos = pos + 1

    # Calculate all possible subsets
    print(arrPowers)
    sizePower = len(arrPowers)
    print("Need bit vector width =", sizePower)
    
    # Number subsets that give you X
    nbrWays = 0
        
    # Run counter i from 000..0 to 111..1 (2**n)
    # For sets of unique numbers the number unique subsets
    #  (including NULL) always 2**n. Python range statement will
    #  drops the null subset from count.
    totSS = 2**sizePower
    print("Will create ", totSS, " subsets of Power array.")

    result = 0
    
    # Parallel process above 4M subsets
    nbrJobs = (totSS // sSetLimit) + 1
    print("Will run as ", nbrJobs, " job.")
    nbrCPU = cpu_count()
    print("System has ", nbrCPU, " cpu.")

    # Build queue to gather results from every subsets job (results multiple subsets)
    qJobResults = Queue()

    if nbrJobs == 1:
        # One job (typically X < 500) probably faster without multiprocessing
        print("Will run as 1 job.")
        ssStart = 0
        ssEnd = totSS
        callNbr = 1
        processSubsets(callNbr, qJobResults, ssStart, ssEnd, arrPowers, myX)
        result = nbrWays
    else:
        # More than one job (typically X > 500 or > 4M subsets) 
        procs = []
        callNbr = 0
        
        # Must be false if nbrJobs == number of unique ranges
        myJobRanges = rangeSplitter(totSS, nbrJobs, False)
      
        print(myJobRanges)
        for oneJob in myJobRanges:
            callNbr = callNbr + 1
            # Build Out range job parameters
            MyStart = oneJob[0]          # Start Range
            MyEnd = oneJob[1]            # End Range
        
            proc = Process(target=processSubsets, args=(callNbr, qJobResults,
                                                         MyStart, MyEnd,
                                                         arrPowers, myX))
            # proc = Process(target=print("hi"))
            
            procs.append(proc)
            proc.start()
            print("Job ", callNbr, ": ", proc, proc.is_alive())

        # Waite for all jobs to complete
        jobDone = 0
        print("Job completed count = ", jobDone)
        while jobDone != myJobRanges:
            result = []
            print("In loop ..")
            for proc in procs:
                print(jobDone, " | ", result, " | ", proc, proc.is_alive())
            result = qJobResults.get()
            print("Polled Q ..")
            for proc in procs:
                print(jobDone, " | ", result, " | ", proc, proc.is_alive())
            if len(result) != 0:
                print("Job Completed: ", result)
                jobDone = jobDone + 1
                print("Job completed count = ", jobDone)
        
        # complete the processes 
        for proc in procs:
            proc.join()
            print(proc, proc.is_alive())
    
    return

# --------------------------------------------------  
# Driver Code
# --------------------------------------------------
if __name__ == '__main__':
    global sSetLimit
    global nbrWays
    sSetLimit = 1024 * 8            # Test Value
    # sSetLimit = 1024 * 1024 * 4   # Normal Value
    X = 180
    N = 2    
    TotWays = powerSum(X, N)
    print("X = ", X, " N = ", N, " Result = ", nbrWays)
