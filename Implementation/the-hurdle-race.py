# The Hurdle Race
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/the-hurdle-race/problem

n,k = list(map(int, input().strip().split(' ')))
height = list(map(int, input().strip().split(' ')))
if max(height) > k:
    print (max(height) - k)
else:
    print (0)