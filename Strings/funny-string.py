# Funny String
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/funny-string/problem

import string

# ca - xz
# xc - cx
# zx - ac

#acxz - 3
#acxza

def funnyString(s):
    str_inverted = s[::-1]
    for i in range(len(s) - 1):
        print(s[i])

    return ""

q = int(input().strip())
for a0 in range(q):
    print(funnyString(input().strip()))
