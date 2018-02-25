# Alternating Characters
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/alternating-characters/problem

# Time complexity: O(n)
def alternatingCharacters(s):
    sumChars = 0
    for i in range(len(s)):
        if i == 0 or tempChar != s[i]:
            tempChar = s[i]
            continue
        if tempChar == s[i]:
            sumChars += 1
    return sumChars

q = int(input().strip())
for a0 in range(q):
    print(alternatingCharacters(input().strip()))