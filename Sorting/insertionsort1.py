# Insertion Sort - Part 1
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/insertionsort1/problem

n = int(input().strip())
arr = [int(ar) for ar in input().strip().split(' ')]
k = len(arr) - 1
key = arr[k]
while k > 0 and key < arr[k - 1]:
    arr[k] = arr[k - 1]
    k -= 1
    print (' '.join([str(it) for it in arr]))
arr[k] = key
print (' '.join([str(it) for it in arr]))