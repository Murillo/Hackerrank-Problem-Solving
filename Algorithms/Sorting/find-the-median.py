# Find the Median
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/find-the-median/problem
# Median: https://en.wikipedia.org/wiki/Median
# Quicksort: https://en.wikipedia.org/wiki/Quicksort#/media/File:Sorting_quicksort_anim.gif
# big-O notation = O(n log n)

def quicksort(arr):
    if len(arr) > 1:
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
        return quicksort(left) + equals + quicksort(right)
    else:
        return arr

def median(n, ar):
    numbers = quicksort(ar)
    if n % 2 == 0:
        half = (int(n/2) + (int(n/2) + 1)) / 2
    else:
        half = int(n/2) + 1

    return numbers[half - 1]

n = int(input().strip())
ar = [int(ar) for ar in input().strip().split(' ')]
print (median(n, ar))