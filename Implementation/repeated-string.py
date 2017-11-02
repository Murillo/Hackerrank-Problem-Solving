# Repeated String
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/repeated-string/problem
# Time Complexity = O(n)

import math 

def repeated_string(text, total):
    if len(text) == 1 and text == 'a':
        return total

    if text.find('a')!=-1:
        add_value = len([text[i] for i in range(len(text)) if text[i] == 'a'])
        excess = text[:total % len(text)]
        return add_value * (total // len(text)) + len([excess[i] for i in range(len(excess)) if excess[i] == 'a'])
    return 0

s = input().strip()
n = int(input().strip())
print (repeated_string(s, n))