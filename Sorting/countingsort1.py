# Counting Sort 1
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/countingsort1/problem

def counting_sort(arr, k):
    results = [0] * k if k <= 100 else [0] * 100
    for i in range(len(arr)):
        results[arr[i]] += 1
    return results

n = int(input().strip())
arr = [int(ar) for ar in input().strip().split(' ')]
print (*counting_sort(arr, n))
