# Missing Numbers
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/missing-numbers/problem
# Time complexity: O(n)

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    m = max(arr + brr) + 1
    list = [0 for _ in range(m)]
    for i in arr:
        list[i] += 1
    for i in brr:
        list[i] -= 1
    return sorted([item for item in range(len(list)) if list[item] != 0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    m = int(input())
    brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    #print (' '.join(map(str, result)))
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
