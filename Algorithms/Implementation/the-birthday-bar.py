# Lily has a chocolate bar consisting of a row of n squares where 
# each square has an integer written on it. She wants to share it 
# with Ron for his birthday, which falls on month m and day d. 
# Lily wants to give Ron a piece of chocolate only if it contains m 
# consecutive squares whose integers sum to d.

# Given m, d, and the sequence of integers written on each square of 
# Lily's chocolate bar, how many different ways can Lily break off 
# a piece of chocolate to give to Ron?

# For example, if m = 2, d = 3 and the chocolate bar contains n 
# rows of squares with the integers [1, 2, 1, 3, 2] written on them 
# from left to right, the following diagram shows two ways to 
# break off a piece:

# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/the-birthday-bar

def solve(n, s, d, m):
    total = 0
    for i in range((n - m) + 1):
        if sum(s[i:i+m]) == d:
            total += 1
    return total

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = list(map(int, input().strip().split(' ')))
print(solve(n, s, d, m))
