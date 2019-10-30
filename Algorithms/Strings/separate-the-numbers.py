# Separate the Numbers
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem
# Time complexity: O(n²)

import math
import os
import random
import re
import sys


# Each element must be value 1 more than the previous element
def firstCondition(second, first):
    return abs(second - first) == 1

# Find a beatiful string
def separateNumbers(s):
    min_val = 0

    # First verification
    if len(s) <= 1 or s[0] == 0:
        return ("NO")

    for i in range(1, len(s)//2+1):
        val = min_val = int(s[0:i])
        val_str = str(val)
        while len(val_str) < len(s):
            val += 1
            val_str += str(val)
        if val_str == s:
            return ("{} {}".format("YES", min_val)) 

    return ("NO")

if __name__ == '__main__':
    for q_itr in range(int(input())):
        print(separateNumbers(input()))