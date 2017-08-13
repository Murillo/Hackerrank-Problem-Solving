# Quicksort 1 - Partition
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/quicksort1/problem

def quicksort(arr):
    equals = []
    left = []
    right = []
    for i in range(len(arr)):
        if i == 0:
            equals.append(arr[i])
        elif i > 0 and arr[i] > arr[0]:
            right.append(arr[i])
        elif i > 0 and arr[i] < arr[0]:
            left.append(arr[i])
        else:
            equals.append(arr[i])

    final = left + equals + right
    return ' '.join([str(item) for item in final])

n = int(input().strip())
arr = [int(ar) for ar in input().strip().split(' ')]
print (quicksort(arr))