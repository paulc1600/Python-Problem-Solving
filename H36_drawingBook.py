#!/bin/python3
# ---------------------------------------------------------------------#
#  Source: HackerRank
#  Purpose: Brie’s Drawing teacher asks her class to open their books
#           to a page number. Brie can either start turning pages from
#           the front of the book or from the back of the book. She
#           always turns pages one at a time. When she opens the book,
#           page 1 is always on the right side:
#           
#           When she flips page 1, she sees pages 2 and 3. Each page
#           except the last page will always be printed on both 
#           sides. The last page may only be printed on the front,
#           given the length of the book. If the book is n pages long,
#           and she wants to turn to page p, what is the minimum number
#           of pages she will turn? She can start at the beginning or
#           the end of the book. 
# ---------------------------------------------------------------------
#  PPC | 09/18/2019 | Original code.
# ---------------------------------------------------------------------
import math
import os
import random
import re
import sys


# Count minimum number of page turns
def pageCount(n, p):
    fwdPgTurns = 0
    bakPgTurns = 0
    result = 0

    fwdPgTurns = p // 2
    bakPgTurns = (n // 2) - (p // 2)

    if fwdPgTurns < bakPgTurns:
        result = fwdPgTurns
    else:
        result = bakPgTurns

    return result


if __name__ == '__main__':
    n = 5
    p = 4
    result = pageCount(n, p)
    print(result)
    n = 6
    p = 2
    result = pageCount(n, p)
    print(result)





          
          
