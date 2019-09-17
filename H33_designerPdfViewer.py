#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: In this challenge, you will be given a list of letter
#           heights in the alphabet and a string. Using the letter
#           heights given, determine the area of the rectangle
#           highlight in mm assuming all letters are 1mm wide. 
#           
#           For example, the highlighted word = torn. Assume the
#           heights of the letters are t = 2, o = 1, r = 1 and n = 1.
#           The tallest letter is 2 high and there are 4 letters. The 
#           hightlighted area will be 2 * 4 = 8mm2 so the answer is 8. 
# ---------------------------------------------------------------------
#  PPC | 09/16/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys


# Longest array that can be craeted were all members <= 1 away each other?
def designerPdfViewer(h, word):
    heights = {}
    result = 0
    c = ''
    tallest = 0

    # Create letter height lookup dictionary
    for Idx in range(26):
        heights[chr(Idx + 97)] = h[Idx]

    # Find tallest character in word
    for c in word:
        myHeight = heights[c]
        if myHeight > tallest:
            tallest = myHeight

    # Area
    result = tallest * len(word)

    return result


if __name__ == '__main__':
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5,
         5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
    word = "zaba"
    result = designerPdfViewer(h, word)
    print(result)

