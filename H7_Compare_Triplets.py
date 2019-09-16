#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Alice and Bob each created one problem for HackerRank. A
#           reviewer rates the two challenges, awarding points on a
#           scale from 1 to 100 for three categories: problem clarity,
#           originality, and difficulty. 
#
#           We define the rating for Alice's challenge to be the triplet
#           a = (a[0], a[1], a[2]), and the rating for Bob's challenge
#           to be the triplet b = (b[0], b[1], b[2])
#
#           Your task is to find their comparison points by comparing
#           with b[O], all] with b[l], and a[2] with 
#
#           o If a[i] > b[i], then Alice is awarded 1 point. 
#           o If a[i] < b[i], then Bob is awarded 1 point. 
#           o If a[i] = b[i], then neither person receives a point. 
#
#           Comparison points is the total points a person earned. 
#
#           Given a and b, determine their respective comparison
#           points. 
#
#           For example, a = [1, 2, 3] and b = [3, 2, 1]. For elements
#           0, Bob is awarded a point because a[0] < b[0]. For the
#           equal elements a[1] and b[1], no points are earned.
#           Finally, for elements 2, a[2] > b[2] so Alice receives a
#           point. Your return array would be [1, 1] with Alice's
#           score first and Bob's second. 
#
# ---------------------------------------------------------------------
#  PPC | 08/26/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# Sum All Elements in an array
def simpleArraySum(ar):
    sum = 0
    for element in ar:
        sum = sum + element
             
    return sum 

# Complete the compareTriplets function below.
def compareTriplets(t1, t2):
    scoret1 = [0, 0, 0]
    scoret2 = [0, 0, 0]
    scTot = [0, 0]

    for tIdx in range(3):
        if t1[tIdx] > t2[tIdx]:
            scoret1[tIdx] = 1
        elif t2[tIdx] > t1[tIdx]:
            scoret2[tIdx] = 1

    scTot[0] = simpleArraySum(scoret1)
    scTot[1] = simpleArraySum(scoret2)
    return scTot    

if __name__ == '__main__': 
    a = [17, 28, 30]
    b = [99, 16, 8]
    result = [0, 0]
    print()
    print(a)
    print(b)
    result = compareTriplets(a, b)
    print(str(result) + '\n')
    
