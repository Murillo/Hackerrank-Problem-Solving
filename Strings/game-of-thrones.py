# Game of Thrones - I
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/game-of-thrones/problem
# Time complexity: O(n²)

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    chars = []
    for i in range(len(s)):
        if s[i] in chars:
            chars.remove(s[i])
        else:
            chars.append(s[i])
    return "YES" if len(chars) <= 1 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    fptr.write(gameOfThrones(s) + '\n')
    #print (gameOfThrones(s) + '\n')
    fptr.close()
