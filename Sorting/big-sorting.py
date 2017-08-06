# Big Sorting
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/big-sorting/problem

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

unsorted = insertion_sort(unsorted)
for i in range(len(unsorted)):
    print (unsorted[i])