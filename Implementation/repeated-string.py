# Repeated String
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/repeated-string/problem
# Time Complexity = O(n)

import math 

def repeated_string(text, total):
    if len(text) == 1 and text == 'a':
        return total

    add_value = 0
    if text.find('a')!=-1:
        add_value = len([text[i] for i in range(len(text)) if text[i] == 'a'])
    amount_str = math.ceil((total / len(text)) * add_value)
    return amount_str

s = input().strip()
n = int(input().strip())
print (repeated_string(s, n))