# Intro to Tutorial Challenges
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/tutorial-intro/problem

v = int(input().strip())
n = int(input().strip())
arr = [int(ar) for ar in input().strip().split(' ')]

for i in range(n):
    if arr[i] == v:
        print (i)