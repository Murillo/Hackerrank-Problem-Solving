# Counting Sort 2
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/countingsort2/problem

def counting_sort(arr, k):
    results = [0] * k if k <= 100 else [0] * 100
    for i in range(len(arr)):
        results[arr[i]] += 1
    return results

def ordered(arr):
    for i in range(len(arr)):
        for j in range(arr[i]):
            print(i, end=' ')

n = int(input().strip())
arr = [int(ar) for ar in input().strip().split(' ')]
ordered(counting_sort(arr, n))
