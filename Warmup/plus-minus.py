# Given an array of integers, calculate which fraction of its 
# elements are positive, which fraction of its elements are 
# negative, and which fraction of its elements are zeroes, 
# respectively. Print the decimal value of each fraction on a new line.

# Developer: Murillo Grubler

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pos = 0
neg = 0
zer = 0
for i in range(n):
    if arr[i] > 0:
        pos += 1
    elif arr[i] < 0:
        neg += 1
    else:
        zer += 1

print (pos/n)
print (neg/n)
print (zer/n)