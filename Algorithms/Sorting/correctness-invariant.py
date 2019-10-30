# Correctness and the Loop Invariant
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/correctness-invariant/problem

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        k = i
        while k > 0 and key < arr[k - 1]:
            arr[k] = arr[k - 1]
            k -= 1
        arr[k] = key

n = int(input().strip())
arr = [int(i) for i in input().strip().split(' ')]
insertion_sort(arr)
print(" ".join(map(str,arr)))