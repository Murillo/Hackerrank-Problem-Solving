# Big Sorting
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/big-sorting/problem

def bubble_sort(arr):
    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        k = i
        while k > 0 and key < arr[k - 1]:
            arr[k] = arr[k - 1]
            k -= 1
        arr[k] = key
    return arr

n = int(input().strip())
unsorted = []
for unsorted_i in range(n):
   unsorted_t = int(input().strip())
   unsorted.append(unsorted_t)

unsorted = bubble_sort(unsorted)
for i in range(len(unsorted)):
    print (unsorted[i])