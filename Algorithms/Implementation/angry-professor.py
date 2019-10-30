# Angry Professor
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/angry-professor/problem
# Time complexity: O(n²)

t = int(input().strip())
for a0 in range(t):
    n,k = list(map(int, input().strip().split(' ')))
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    early = 0
    for i in range(n):
        if a[i] <= 0:
            early += 1
    
    print ("NO" if early >= k else "YES")