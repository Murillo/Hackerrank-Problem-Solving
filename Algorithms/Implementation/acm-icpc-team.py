# ACM ICPC Team
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/acm-icpc-team/problem

import itertools
import math
import os
import random
import re
import sys

def acmTeam(topic):
    max = total = 0
    for item in itertools.combinations(topic, 2):
        conv = bin(int(item[0], 2) | int(item[1], 2))
        result = conv[2:].count('1')
        if result > max:
            total = 1
            max = result  
        elif result == max:
            total += 1      
    return [max, total]

fptr = open(os.environ['OUTPUT_PATH'], 'w')
nm = input().split()
topic = [input() for _ in range(int(nm[0]))]
fptr.write('\n'.join(map(str, acmTeam(topic))))
fptr.write('\n')
fptr.close()