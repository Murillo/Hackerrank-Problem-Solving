# Permuting Two Arrays
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/two-arrays/problem

import itertools

def permute(inputs, k):
    list_a = sorted(inputs[0], key=int, reverse=False)
    list_b = sorted(inputs[1], key=int, reverse=True)
    for i in range(len(list_a)):
        if list_a[i] + list_b[i] < k:
            return "NO"
    return "YES"

total_arrays = 2
samples = int(input().strip())
for i in range(samples):
    n, k = map(int, input().strip().split(' '))
    inputs = []
    for j in range(total_arrays):
        inputs.append(list(map(int, input().strip().split(' '))))
    print(permute(inputs, k))
    