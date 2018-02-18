# Funny String
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/funny-string/problem

# Import library
import string

# Time complexity: O(n)
def funnyString(arr):
    s = list([string.ascii_lowercase.index(i) for i in arr])
    r = list([string.ascii_lowercase.index(i) for i in arr[::-1]])
    for i in range(1, len(arr) - 1):
        if abs(s[i] - s[i - 1]) != abs(r[i] - r[i - 1]):
            return "Not Funny"
    return "Funny"

# It starts the program calling the function funnyString
q = int(input().strip())
for a0 in range(q):
    print(funnyString(input().strip()))
