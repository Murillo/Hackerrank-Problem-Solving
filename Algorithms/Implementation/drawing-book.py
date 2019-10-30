# Drawing Book 
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/drawing-book/problem

n = int(input().strip())
p = int(input().strip())
print(min(p//2, n//2 - p//2))