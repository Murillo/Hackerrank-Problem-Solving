# Jumping on the Clouds: Revisited
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
# Time complexity: O(n)

n,k = list(map(int, input().strip().split(' ')))
arr = [int(c_temp) for c_temp in input().strip().split(' ')]

energy = 100
for i in range(0, n, k):
    energy = energy - 1 if arr[i] == 0 else energy - 3

print (energy)