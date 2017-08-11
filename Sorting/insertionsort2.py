# Insertion Sort - Part 2
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/insertionsort2/problem

def insertion_sort(arr, i):
    key = arr[i]
    k = i
    while k > 0 and key < arr[k - 1]:
        arr[k] = arr[k - 1]
        k -= 1
    arr[k] = key
    return ' '.join([str(it) for it in arr])

n = int(input().strip())
arr = [int(ar) for ar in input().strip().split(' ')]

for i in range(1, len(arr)):
    print (insertion_sort(arr, i))
