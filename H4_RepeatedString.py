#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Lilah has a string, s, of lowercase English letters that
#           she repeated infinitely many times. Given an integer,n,
#           find and print the number of letter a's in the first n 
#           letters of Lilah's infinite string. For example, if the
#           string s='abcac' and n = 10, the substring we consider is 
#           abcacabcac, the first 10 characters of her infinite string.
#           There are 4 occurrences of a in the substring.
#
#           Function Description
#           Complete the repeatedString function in the editor below.
#           It should return an integer representing the number of
#           occurrences of a in the prefix of length n  in the
#           infinitely repeating string.
#           
#           repeatedString has the following parameter(s):
#	    >>> s: a string to repeat
#           >>> n: the number of characters to consider
#
# ---------------------------------------------------------------------
#  PPC | 08/20/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys

# Complete the repeated string function below.
def repeatedString(s, n):
          
    # -------------------------------------------------
    #  Get total 'a' in string of n length filled in
    #    by repeating sub-string s
    # -------------------------------------------------
    #  How many occurences of 'a' in 1 input string?
    inputCnt = s.count('a')
    #  How many even multiples of input string in n length
    inputSize = len(s)
    inputMult = n // inputSize
    inputRemainder = n % inputSize
    totalA = inputCnt * inputMult
    print("String s is: ", s, "Size s = ", inputSize)
    print("s fits in ", n, " space repeated string ", inputMult, " times.")
    print("Remainder string partial is ", inputRemainder, " long.")
    print("Partial remainder string will be ", s[0:inputRemainder]) 

    # How many a's in remaining partial substring
    if inputRemainder != 0:
        partial = s[0:inputRemainder]
        totalA = totalA + partial.count('a')
             
    return totalA    

if __name__ == '__main__': 
    n = 999
    s = 'a'
    print()
    print(s)
    print(n)
    result = repeatedString(s, n)
    print(str(result) + '\n')
    
