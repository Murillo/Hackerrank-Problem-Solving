# Making Anagrams
# Link: https://www.hackerrank.com/challenges/making-anagrams/problem

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    copy = list(s2)
    for i in s1:
        if i in copy:
            copy.remove(i)
    no_common = len(s2)-len(copy)
    return len(s1)+len(s2)-2*no_common

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s1 = input()
    s2 = input()
    result = makingAnagrams(s1, s2)
    #print (str(result) + '\n')
    fptr.write(str(result) + '\n')
    fptr.close()