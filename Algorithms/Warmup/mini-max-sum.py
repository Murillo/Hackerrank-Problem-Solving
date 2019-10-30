# Given five positive integers, find the minimum and 
# maximum values that can be calculated by summing 
# exactly four of the five integers. Then print the 
# respective minimum and maximum values as a single 
# line of two space-separated long integers.

# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/mini-max-sum

import sys

# Get data
arr = list(map(int, input().strip().split(' ')))
n = len(arr)
values = []

# Get the minimum and maximum values
for i in range(n):
    val = 0
    for j in range(n):
        if i != j:
            val += arr[j]
    values.append(val)

# Show the results
print (str(min(values)) + " " + str(max(values))) 